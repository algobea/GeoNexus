# Benchmarking - Conjetura de Collatz
## Algoritmo: demostración para todos los números de 2 hasta N=1,000,000

---

## 1. PYTHON

### Requisito
Python 3.8+ (verificar: `python --version`)

### Ejecutar
```bash
python collatz.py
```

### Salida esperada
```
Pasos totales : 8.xxxxxxx
Tiempo        : XXXX.XX ms
Memoria pico  : X.XX MB
```

---

## 2. JAVASCRIPT (Node.js)

### Requisito
Node.js 16+ (verificar: `node --version`)

### Ejecutar
```bash
node collatz.js
```

### Salida esperada
```
Pasos totales : 8.xxxxxxx
Tiempo        : XXX.XX ms
Memoria pico  : X.XX MB
```

---

## 3. RUST

### Requisito
Rust + Cargo (instalar en https://rustup.rs)
Verificar: `cargo --version`

### Compilar y ejecutar (IMPORTANTE: usar --release)
```bash
cd collatz_rust
cargo build --release
./target/release/collatz          # Linux/Mac
target\release\collatz.exe        # Windows
```

### Medir memoria (Linux/Mac)
```bash
/usr/bin/time -v ./target/release/collatz 2>&1 | grep "Maximum resident"
```

### Salida esperada
```
Pasos totales : 8.xxxxxxx
Tiempo        : X.XX ms
```

---

## 4. ZIG

### Requisito
Zig 0.12+ (descargar en https://ziglang.org/download/)
Verificar: `zig version`

### Compilar y ejecutar (IMPORTANTE: usar -O ReleaseFast)
```bash
zig build-exe collatz.zig -O ReleaseFast
./collatz          # Linux/Mac
collatz.exe        # Windows
```

### Medir memoria (Linux/Mac)
```bash
/usr/bin/time -v ./collatz 2>&1 | grep "Maximum resident"
```

### Salida esperada
```
Pasos totales : 8.xxxxxxx
Tiempo        : X.XX ms
```

---

## CÓMO TOMAR LOS DATOS PARA LA TABLA

1. Ejecutar cada programa 3 veces
2. Anotar los 3 tiempos y calcular el promedio
3. Registrar la memoria pico (o estimado del sistema)

### Ejemplo de registro:
| Ejecución | Python | JS | Rust | Zig |
|-----------|--------|----|------|-----|
| Run 1     | XXXX ms| XX | X.X  | X.X |
| Run 2     | XXXX ms| XX | X.X  | X.X |
| Run 3     | XXXX ms| XX | X.X  | X.X |
| **Prom.** | **XX** | ** | **   | **  |

---

## VERIFICACIÓN DE CORRECTITUD
Los 4 programas deben mostrar el MISMO número de "Pasos totales".
Si difieren, hay un error en alguna implementación.
