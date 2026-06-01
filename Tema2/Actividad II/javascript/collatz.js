const { performance } = require('perf_hooks');

// Conjetura de Collatz para todos los números menores que N

function collatz(n) {
    let pasos = 0;
    while (n !== 1) {
        n = n % 2 === 0 ? n / 2 : 3 * n + 1;
        pasos++;
    }
    return pasos;
}

const N = 1_000_000;
let total = 0;

const inicio = performance.now();

for (let i = 2; i < N; i++) {
    total += collatz(i);
}

const tiempo = performance.now() - inicio;
const mem = process.memoryUsage();

console.log(`Pasos totales : ${total}`);
console.log(`Tiempo        : ${tiempo.toFixed(2)} ms`);
console.log(`Memoria pico  : ${(mem.heapUsed / 1_048_576).toFixed(2)} MB`);
