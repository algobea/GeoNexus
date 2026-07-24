import re
import difflib

# --- FASE 1: LEXER HIBRIDO ---
TOKEN_SPECS = [
    ('INT', r'\d+'), ('STRING', r'"[^"]*"'), ('ASSIGN', r'='), 
    ('OP', r'>|<|=='), ('LPAREN', r'\('), ('RPAREN', r'\)'), 
    ('SEMI', r';'), ('ID', r'[A-Za-z_][A-Za-z0-9_]*'), 
    ('SKIP', r'[ \t\n]+'), ('MISMATCH', r'.')
]
KEYWORDS = ['print', 'if', 'else']

def evaluar_similitud(lexeme):
    mejor_ratio = 0.0
    candidato = None
    for kw in KEYWORDS:
        ratio = difflib.SequenceMatcher(None, lexeme, kw).ratio()
        if ratio > mejor_ratio:
            mejor_ratio = ratio
            candidato = kw
    return candidato, mejor_ratio

def fallback_ia_lexer(lexeme):
    return f"Sugerencia IA: '{lexeme}' -> 'print'"

def lexer_hibrido(codigo):
    tokens = []
    sugerencias = []
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPECS)
    
    for mo in re.finditer(tok_regex, codigo):
        tipo = mo.lastgroup
        valor = mo.group()
        if tipo == 'SKIP': continue
        elif tipo == 'MISMATCH': raise RuntimeError(f"Error léxico: {valor}")
            
        if tipo == 'ID':
            if valor in KEYWORDS:
                tipo = 'KEYWORD'
            else:
                candidato, ratio = evaluar_similitud(valor)
                if 0.5 < ratio < 1.0: 
                    if ratio >= 0.8:
                        sugerencias.append(f"Sugerencia (Lexer): '{valor}' -> '{candidato}'")
                    else:
                        sugerencias.append(f"{fallback_ia_lexer(valor)}")
                    valor = 'print'
                    tipo = 'KEYWORD'
        tokens.append((tipo, valor))
    return tokens, sugerencias

# --- FASE 2: PARSER Y AST ---
class ASTNode:
    def __init__(self, tipo, **kwargs):
        self.tipo = tipo
        self.atributos = kwargs
    def __repr__(self):
        return f"{self.tipo}({', '.join(f'{k}={v}' for k, v in self.atributos.items())})"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None
    def lookahead(self, offset=1):
        idx = self.pos + offset
        return self.tokens[idx] if idx < len(self.tokens) else None
    def match(self, tipo):
        tok = self.peek()
        if tok and tok[0] == tipo:
            self.pos += 1
            return tok
        return None
    def parse(self):
        instrucciones = []
        while self.peek():
            instrucciones.append(self.parse_statement())
        return instrucciones
    def parse_statement(self):
        tok = self.peek()
        if tok[0] == 'KEYWORD' and tok[1] == 'print':
            self.match('KEYWORD')
            if self.peek() and self.peek()[0] == 'ID' and self.lookahead() and self.lookahead()[0] == 'ASSIGN':
                print("[Fallback IA Parser] Sugerencia: Estructura anómala 'print ID ='. Corrigiendo a asignación.")
                var_name = self.match('ID')[1]
                self.match('ASSIGN')
                val = self.match('INT')[1]
                if self.peek() and self.peek()[0] == 'SEMI': self.match('SEMI')
                return ASTNode("PrintAsignacion", var=var_name, val=val)

            tiene_paren = self.match('LPAREN')
            expr = self.parse_expression()
            if tiene_paren: self.match('RPAREN')
            if self.peek() and self.peek()[0] == 'SEMI': self.match('SEMI')
            return ASTNode("Print", expr=expr)

        elif tok[0] == 'KEYWORD' and tok[1] == 'if':
            self.match('KEYWORD')
            cond = self.parse_expression()
            c_if = self.parse_statement()
            c_else = None
            if self.peek() and self.peek()[1] == 'else':
                self.match('KEYWORD')
                c_else = self.parse_statement()
            return ASTNode("If", condicion=cond, cuerpo_if=c_if, cuerpo_else=c_else)

        if tok[0] == 'ID':
            var = self.match('ID')[1]
            self.match('ASSIGN')
            val = self.match('INT')[1]
            self.match('SEMI')
            return ASTNode("Asignacion", var=var, val=val)
        self.pos += 1
        return ASTNode("Error", token=tok)

    def parse_expression(self):
        izq = self.peek()
        if not izq: return None
        self.pos += 1
        if self.peek() and self.peek()[0] == 'OP':
            op = self.match('OP')[1]
            der = self.peek()
            self.pos += 1
            return ASTNode("OpBinaria", izq=izq[1], op=op, der=der[1])
        return izq[1]

# --- EJECUCION PRINCIPAL ---
if __name__ == '__main__':
    codigo_prueba = 'pront x = 5; if x > 3 prnt(x) else prnt("no")'
    print("--- 1. SUGERENCIAS IA ---")
    tokens, sugerencias = lexer_hibrido(codigo_prueba)
    for s in sugerencias: print(s)
    
    print("\n--- 2. TOKENS CORREGIDOS ---")
    print(tokens)
    
    print("\n--- 3. ARBOL DE SINTAXIS ABSTRACTA (AST) ---")
    parser = Parser(tokens)
    ast = parser.parse()
    for nodo in ast: print(nodo)