# ESPECIFICACIÓN FORMAL DEL LENGUAJE L
# DSL para Sistema de Gestión de Microredes Eléctricas (ECO-GRID)

---

## 1. ESPECIFICACIÓN DEL ALFABETO Y REGLAS LÉXICAS

El analizador léxico de Lenguaje L reconoce los siguientes tipos de tokens:

### 1.1 Palabras Clave (KEYWORD)
Reservadas — no pueden usarse como identificadores:

| Token             | Propósito                                      |
|-------------------|------------------------------------------------|
| init_grid         | Marca el inicio del programa                   |
| fin_grid          | Marca el fin del programa                      |
| declarar          | Declara e inicializa una variable              |
| si                | Inicio de estructura condicional               |
| entonces          | Cuerpo rama verdadera del condicional          |
| sino              | Cuerpo rama falsa del condicional              |
| fin_si            | Cierre de estructura condicional               |
| mientras          | Inicio de estructura repetitiva                |
| ejecutar          | Cuerpo del bucle mientras                      |
| fin_mientras      | Cierre del bucle mientras                      |
| verdadero         | Literal booleano positivo                      |
| falso             | Literal booleano negativo                      |
| y                 | Operador lógico AND                            |
| o                 | Operador lógico OR                             |
| no                | Operador lógico NOT                            |

### 1.2 Primitivas de Dispositivo (DEVICE_KEYWORD)
Comandos directos de control físico:

| Token                        | Acción sobre el sistema ECO-GRID              |
|------------------------------|------------------------------------------------|
| leer_temperatura(bateria_id) | Lee temperatura de un banco de baterías (°C)  |
| estado_carga(bateria_id)     | Lee nivel de carga de una batería (%)         |
| leer_flujo(dispositivo_id)   | Lee flujo eléctrico de un sensor (kW)         |
| conmutar_linea(origen, dest) | Redirige energía entre sectores o redes       |
| activar(dispositivo_id)      | Enciende un sistema auxiliar                  |
| desactivar(dispositivo_id)   | Apaga una línea o sistema                     |
| inyectar_red(kW)             | Exporta excedente hacia la red pública        |
| aislar_sector(sector_id)     | Desconecta un sector de consumo               |
| emitir_alerta(mensaje)       | Envía un mensaje de alerta al operador        |

### 1.3 Identificadores (IDENTIFIER)
Regla de formación:
- Primer carácter: letra minúscula (a–z) o guion bajo (_)
- Caracteres siguientes: letras, dígitos (0–9) o guion bajo (_)
- Los identificadores de dispositivos físicos se escriben en MAYÚSCULAS
  (ej: BATERIA_01, SECTOR_MEDICO, PANEL_SOLAR)

Ejemplos válidos:   carga_actual, temp_sensor, banco_id
Ejemplos inválidos: 1variable, init_grid (es palabra clave)

### 1.4 Literales Numéricos (NUM_LITERAL)
- Enteros:   [0-9]+                  → Ejemplo: 10, 55, 200
- Decimales: [0-9]+ "." [0-9]+       → Ejemplo: 55.0, 90.5, 20.0

### 1.5 Literales de Cadena (STR_LITERAL)
Texto encerrado entre comillas dobles:
- Ejemplo: "ALERTA TERMICA: Temperatura critica"

### 1.6 Operadores
| Tipo         | Símbolos                        |
|--------------|---------------------------------|
| Comparación  | >  <  >=  <=  ==  !=            |
| Asignación   | <-                              |
| Aritméticos  | +  -  *  /                      |
| Lógicos      | y  o  no  (palabras clave)      |

### 1.7 Delimitadores
( ) ,

### 1.8 Comentarios
Líneas que comienzan con #. Son ignoradas por el analizador léxico.
Ejemplo:  # Este es un comentario

### 1.9 Espacios e Indentación
El lenguaje NO es sensible a la indentación (a diferencia de Python).
Los bloques de código están delimitados por palabras clave de cierre
(fin_si, fin_mientras, fin_grid). La indentación es opcional y sirve
únicamente para mejorar la legibilidad humana.

---

## 2. GRAMÁTICA SINTÁCTICA ABSTRACTA (BNF Simplificada)

```
programa       ::= "init_grid" IDENTIFIER bloque "fin_grid"

bloque         ::= sentencia*

sentencia      ::= declaracion
                 | asignacion
                 | estructura_si
                 | estructura_mientras
                 | llamada_dispositivo
                 | emision_alerta

declaracion    ::= "declarar" IDENTIFIER "<-" expresion

asignacion     ::= IDENTIFIER "<-" expresion

estructura_si  ::= "si" condicion "entonces"
                       bloque
                   [ "sino"
                       bloque ]
                   "fin_si"

estructura_mientras ::= "mientras" condicion "ejecutar"
                            bloque
                        "fin_mientras"

condicion      ::= expresion OP_COMP expresion
                 | condicion OP_LOG condicion

expresion      ::= NUM_LITERAL
                 | STR_LITERAL
                 | BOOL_LITERAL
                 | IDENTIFIER
                 | expresion OP_ARIT expresion
                 | llamada_lectura

llamada_lectura     ::= "leer_temperatura" "(" IDENTIFIER ")"
                      | "estado_carga"     "(" IDENTIFIER ")"
                      | "leer_flujo"       "(" DEVICE_ID  ")"

llamada_dispositivo ::= "activar"         "(" DEVICE_ID ")"
                      | "desactivar"      "(" DEVICE_ID ")"
                      | "aislar_sector"   "(" DEVICE_ID ")"
                      | "inyectar_red"    "(" expresion  ")"
                      | "conmutar_linea"  "(" DEVICE_ID "," DEVICE_ID ")"

emision_alerta ::= "emitir_alerta" "(" STR_LITERAL ")"

OP_COMP  ::= ">" | "<" | ">=" | "<=" | "==" | "!="
OP_LOG   ::= "y" | "o"
OP_ARIT  ::= "+" | "-" | "*" | "/"
BOOL_LITERAL ::= "verdadero" | "falso"
```

---


