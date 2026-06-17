import sys

def validador_afd_pgn(cadena):
    # Alfabetos
    piezas = {'K', 'Q', 'R', 'B', 'N'}
    columnas = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
    filas = {'1', '2', '3', '4', '5', '6', '7', '8'}
    modificadores = {'+', '#'}
    
    # Definición de transiciones del AFD
    estado_actual = 'q0'
    
    for char in cadena:
        if estado_actual == 'q0':
            if char in piezas: estado_actual = 'q1'
            elif char in columnas: estado_actual = 'q3'
            elif char == 'O': estado_actual = 'q6'
            else: return False
            
        elif estado_actual == 'q1':
            if char == 'x': estado_actual = 'q2'
            elif char in columnas: estado_actual = 'q3'
            else: return False
            
        elif estado_actual == 'q2':
            if char in columnas: estado_actual = 'q3'
            else: return False
            
        elif estado_actual == 'q3':
            if char in filas: estado_actual = 'q4'
            else: return False
            
        elif estado_actual == 'q4':
            if char in modificadores: estado_actual = 'q5'
            else: return False
            
        elif estado_actual == 'q6':
            if char == '-': estado_actual = 'q6a'
            else: return False
            
        elif estado_actual == 'q6a':
            if char == 'O': estado_actual = 'q7'
            else: return False
            
        elif estado_actual == 'q7':
            if char == '-': estado_actual = 'q7a'
            else: return False
            
        elif estado_actual == 'q7a':
            if char == 'O': estado_actual = 'q8'
            else: return False
            
        elif estado_actual == 'q5' or estado_actual == 'q8':
            return False # No debe haber más caracteres después del estado final
            
    # q4 (movimiento normal), q5 (con jaque/mate), q7 (enroque corto), q8 (enroque largo)
    estados_aceptacion = {'q4', 'q5', 'q7', 'q8'}
    return estado_actual in estados_aceptacion

# Pruebas de ejecución
if __name__ == "__main__":
    casos_prueba = ["e4", "Nf3", "Bxc4", "O-O", "O-O-O", "Qh5+", "exd5#", "Z9", "O-O-O-O", "Nfx3"]
    print("Evaluando movimientos PGN:")
    for caso in casos_prueba:
        resultado = "Válido" if validador_afd_pgn(caso) else "Inválido"
        print(f"{caso.ljust(10)} -> {resultado}")
