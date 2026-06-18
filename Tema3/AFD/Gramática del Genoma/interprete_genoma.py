import turtle
import time

# 1. Definición del lenguaje derivado de la Gramática Libre de Contexto
# Estas son las sentencias finales (terminales) obtenidas en la fase teórica
GENOMAS_VALIDOS = {
    "Cuadrado": "acacacac",
    "Arbol": "agatccatgt",
    "Cubo": "acacacacacagacacacactctg", # Representación 2D de caras desfasadas
    "Escalera": "acagacagacag",
    "Cruz": "aattcaattcaattcaatt"
}

def configurar_entorno():
    """Inicializa y configura la ventana gráfica y el cursor (tortuga)."""
    pantalla = turtle.Screen()
    pantalla.title("Intérprete de Genoma - Gramáticas Formales UNEG")
    pantalla.setup(width=800, height=600)
    
    cursor = turtle.Turtle()
    cursor.shape("turtle")
    cursor.color("blue")
    cursor.pensize(3)
    
    return pantalla, cursor

def interprete_genoma(cursor, cadena, unidad=60):
    """
    Núcleo del intérprete: lee la cadena de caracteres (tokens)
    y ejecuta la equivalencia geométrica de cada terminal.
    """
    for token in cadena:
        if token == 'a':
            # 'a': Avanzar dibujando
            cursor.forward(unidad)
        elif token == 'c':
            # 'c': Girar 90° a la derecha
            cursor.right(90)
        elif token == 'g':
            # 'g': Girar 90° a la izquierda
            cursor.left(90)
        elif token == 't':
            # 't': Retroceder sin dibujar (para bifurcaciones y retornos)
            cursor.penup()
            cursor.backward(unidad)
            cursor.pendown()
        else:
            # Se reporta el error léxico. Se detiene la función para no imprimir basura
            print(f"Error de Compilación: El token '{token}' no pertenece al alfabeto Σ={{a,c,g,t}}.")
            return   