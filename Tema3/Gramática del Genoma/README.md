# Módulo 2: Gramática del Genoma para Modelado de Dibujo

Este directorio contiene el código fuente y el intérprete correspondientes al **Bloque 2** de la evaluación del Tema 3 (Lenguajes y Gramáticas Formales). 

El objetivo de este módulo es modelar un sistema de dibujo mediante una Gramática Libre de Contexto (GLC) y ejecutar sus derivaciones a través de un intérprete vectorial (Gráficas de Tortuga).

## El Lenguaje (Alfabeto Σ)

El analizador léxico reconoce un alfabeto estricto de 4 terminales, asignados a acciones espaciales específicas:
* `a`: Avanza una unidad trazando una línea.
* `c`: Gira 90° a la derecha (sentido de las agujas del reloj).
* `g`: Gira 90° a la izquierda (sentido contrario a las agujas del reloj).
* `t`: Retrocede una unidad sin trazar línea (utilizado para el retorno en bifurcaciones).

## Requisitos de Ejecución
El proyecto está desarrollado para ser ligero y de ejecución directa.
* **Python 3.x**
* Módulos `turtle` y `time` (Ambos son componentes nativos de la biblioteca estándar de Python, por lo que **no** es necesario instalar dependencias externas vía `pip`).

## Uso y Demostración
Para inicializar el motor gráfico y visualizar la demostración automatizada de las figuras generadas por las cadenas de la gramática, sitúate en este directorio y ejecuta el siguiente comando en tu terminal:

```bash
python interprete_genoma.py