const std = @import("std");

// Conjetura de Collatz para todos los números menores que N

fn collatz(n: u64) u64 {
    var num = n;
    var pasos: u64 = 0;
    while (num != 1) {
        if (num % 2 == 0) {
            num /= 2;
        } else {
            num = 3 * num + 1;
        }
        pasos += 1;
    }
    return pasos;
}

pub fn main() !void {
    const N: u64 = 1_000_000;
    const stdout = std.io.getStdOut().writer();

    var timer = try std.time.Timer.start();

    var total: u64 = 0;
    var i: u64 = 2;
    while (i < N) : (i += 1) {
        total += collatz(i);
    }

    const ns = timer.read();
    const ms: f64 = @as(f64, @floatFromInt(ns)) / 1_000_000.0;

    try stdout.print("Pasos totales : {d}\n", .{total});
    try stdout.print("Tiempo        : {d:.2} ms\n", .{ms});
    // Para memoria usar: /usr/bin/time -v ./collatz
}
