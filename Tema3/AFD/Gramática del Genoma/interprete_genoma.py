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
    cursor.speed(4) # Velocidad moderada para poder apreciar el paso a paso
    
    return pantalla, cursor