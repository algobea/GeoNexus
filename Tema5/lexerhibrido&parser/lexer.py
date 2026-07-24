import re
import difflib

# Definición de tokens básicos para UnegScript
TOKEN_SPECS = [
    ('INT', r'\d+'),
    ('STRING', r'"[^"]*"'),
    ('ASSIGN', r'='),
    ('OP', r'>|<|=='),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('SEMI', r';'),
    ('ID', r'[A-Za-z_][A-Za-z0-9_]*'),
    ('SKIP', r'[ \t\n]+'),
    ('MISMATCH', r'.'),
]

KEYWORDS = ['print', 'if', 'else']

def evaluar_similitud(lexeme):
    """Calcula la similitud contra palabras clave conocidas."""
    mejor_ratio = 0.0
    candidato = None
    for kw in KEYWORDS:
        ratio = difflib.SequenceMatcher(None, lexeme, kw).ratio()
        if ratio > mejor_ratio:
            mejor_ratio = ratio
            candidato = kw
    return candidato, mejor_ratio

def fallback_ia(lexeme):
    """Simula la consulta a un LLM cuando el ratio < 0.8."""
    # En un entorno real, aquí se envía el prompt al LLM
    return f"Sugerencia IA: '{lexeme}' -> 'print' (Contexto de UnegScript evaluado)"

def lexer_hibrido(codigo):
    tokens = []
    sugerencias = []
    
    # Compilar regex
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPECS)
    
    for mo in re.finditer(tok_regex, codigo):
        tipo = mo.lastgroup
        valor = mo.group()
        
        if tipo == 'SKIP':
            continue
        elif tipo == 'MISMATCH':
            raise RuntimeError(f"Carácter inesperado: {valor}")
            
        if tipo == 'ID':
            if valor in KEYWORDS:
                tipo = 'KEYWORD'
            else:
                # Verificar si es un posible error tipográfico de una keyword
                candidato, ratio = evaluar_similitud(valor)
                # Si hay similitud parcial (ej. pront, prnt)
                if 0.5 < ratio < 1.0: 
                    if ratio >= 0.8:
                        sugerencias.append(f"Sugerencia: '{valor}' -> '{candidato}' (Ratio: {ratio:.2f})")
                        valor = candidato
                        tipo = 'KEYWORD'
                    else:
                        respuesta_ia = fallback_ia(valor)
                        sugerencias.append(f"{respuesta_ia} - Umbral {ratio:.2f} < 0.8")
                        valor = 'print' # Asumimos corrección para poder continuar al parser
                        tipo = 'KEYWORD'
        
        tokens.append((tipo, valor))
        
    return tokens, sugerencias

# Código de prueba según las instrucciones
codigo_prueba = 'pront x = 5; if x > 3 prnt(x) else prnt("no")'
tokens, sugerencias = lexer_hibrido(codigo_prueba)

print("--- TOKENS ---")
for t in tokens:
    print(t)
    
print("\n--- SUGERENCIAS / FALLBACK ---")
for s in sugerencias:
    print(s)
