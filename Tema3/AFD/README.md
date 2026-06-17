# Validador de Ajedrez PGN (AFD)

Este script en Python implementa un Autómata Finito Determinista (AFD) para validar los movimientos básicos del ajedrez en notación PGN (Portable Game Notation). 

## Lógica del Algoritmo

El validador procesa cada cadena de texto carácter por carácter. En lugar de depender de librerías de expresiones regulares, el algoritmo utiliza una máquina de estados explícita:

* **Estado inicial (`q0`):** Punto de inicio. Evalúa si el primer carácter es una pieza (`K`, `Q`, `R`, `B`, `N`), la columna de un peón (`a-h`), o la letra `O` para iniciar un enroque.
* **Transiciones de estado:** Dependiendo del carácter evaluado, el programa avanza lógicamente (ej. de una pieza al indicador de captura `x`, y luego a la columna de destino). Si el autómata recibe un carácter no esperado para su estado actual, la evaluación falla inmediatamente y retorna `False`.
* **Estados de aceptación:** El movimiento se considera válido si, al terminar de leer toda la cadena, el programa se detiene en un estado de aceptación:
    * `q4`: Movimiento estándar completado.
    * `q5`: Movimiento completado con jaque (`+`) o mate (`#`).
    * `q7`: Enroque corto validado (`O-O`).
    * `q8`: Enroque largo validado (`O-O-O`).

## Requisitos y Ejecución

El script está escrito en Python estándar y no requiere dependencias externas. Para ejecutarlo desde la terminal, utiliza:

```bash
python3 validador_pgn.py #por mi SO, ejecuto python3 