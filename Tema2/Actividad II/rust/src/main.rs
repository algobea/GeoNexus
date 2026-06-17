use std::time::Instant;

// Conjetura de Collatz para todos los números menores que N

fn collatz(mut n: u64) -> u64 {
    let mut pasos: u64 = 0;
    while n != 1 {
        n = if n % 2 == 0 { n / 2 } else { 3 * n + 1 };
        pasos += 1;
    }
    pasos
}

fn main() {
    let n: u64 = 1_000_000;
    let inicio = Instant::now();

    let total: u64 = (2..n).map(collatz).sum();

    println!("Pasos totales : {}", total);
    println!("Tiempo        : {:.2} ms", inicio.elapsed().as_secs_f64() * 1000.0);
    // Para memoria usar: /usr/bin/time -v ./target/release/collatz
}
