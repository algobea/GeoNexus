import time
import tracemalloc

# Conjetura de Collatz para todos los números menores que N
# Regla: si n es par -> n/2 | si n es impar -> 3n+1, hasta llegar a 1

def collatz(n):
    pasos = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        pasos += 1
    return pasos

N = 1_000_000  # demostrar para todos los números menores que N

tracemalloc.start()
inicio = time.perf_counter()

total = sum(collatz(i) for i in range(2, N))

fin = time.perf_counter()
_, pico = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Pasos totales : {total}")
print(f"Tiempo        : {(fin - inicio) * 1000:.2f} ms")
print(f"Memoria pico  : {pico / 1_048_576:.2f} MB")
