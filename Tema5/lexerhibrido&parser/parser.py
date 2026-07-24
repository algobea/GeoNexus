class ASTNode:
    def __init__(self, tipo, **kwargs):
        self.tipo = tipo
        self.atributos = kwargs

    def __repr__(self):
        atr_str = ", ".join(f"{k}={v}" for k, v in self.atributos.items())
        return f"{self.tipo}({atr_str})"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        """Devuelve el token actual sin consumirlo."""
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def lookahead(self, offset=1):
        """Observa tokens futuros."""
        index = self.pos + offset
        return self.tokens[index] if index < len(self.tokens) else None

    def match(self, tipo):
        """Consume y devuelve el token si coincide con el tipo esperado."""
        tok = self.peek()
        if tok and tok[0] == tipo:
            self.pos += 1
            return tok
        return None

    def fallback_ia(self, error_msg):
        """Simula la consulta a IA en caso de fallos del parser."""
        print(f"[Fallback IA Parser] {error_msg}")

    def parse(self):
        instrucciones = []
        while self.peek():
            instrucciones.append(self.parse_statement())
        return instrucciones

    def parse_statement(self):
        tok = self.peek()
        
        if tok[0] == 'KEYWORD' and tok[1] == 'print':
            self.match('KEYWORD')
            
            # Lookahead: Detectar anomalía "print x = 5"
            sig = self.peek()
            futuro = self.lookahead(1)
            if sig and sig[0] == 'ID' and futuro and futuro[0] == 'ASSIGN':
                self.fallback_ia("Estructura anómala 'print ID ='. Asumiendo bloque de declaración/asignación.")
                var_name = self.match('ID')[1]
                self.match('ASSIGN')
                val = self.match('INT')[1]
                if self.peek() and self.peek()[0] == 'SEMI':
                    self.match('SEMI')
                return ASTNode("PrintAsignacion", var=var_name, val=val)

            # Estructura Print normal
            tiene_paren = self.match('LPAREN')
            expr = self.parse_expression()
            if tiene_paren:
                if not self.match('RPAREN'):
                    self.fallback_ia("Falta paréntesis de cierre ')'. Autocompletando.")
            
            if self.peek() and self.peek()[0] == 'SEMI':
                self.match('SEMI')
                
            return ASTNode("Print", expr=expr)

        elif tok[0] == 'KEYWORD' and tok[1] == 'if':
            self.match('KEYWORD')
            cond = self.parse_expression()
            cuerpo_if = self.parse_statement()
            cuerpo_else = None
            
            tok_else = self.peek()
            if tok_else and tok_else[0] == 'KEYWORD' and tok_else[1] == 'else':
                self.match('KEYWORD')
                cuerpo_else = self.parse_statement()
                
            return ASTNode("If", condicion=cond, cuerpo_if=cuerpo_if, cuerpo_else=cuerpo_else)

        else:
            # Asignación estándar o nodo no reconocido
            if tok[0] == 'ID':
                var = self.match('ID')[1]
                if not self.match('ASSIGN'):
                    self.fallback_ia(f"Falta operador de asignación '=' después de {var}.")
                val = self.match('INT')[1]
                self.match('SEMI')
                return ASTNode("Asignacion", var=var, val=val)
            else:
                self.pos += 1
                return ASTNode("ErrorSintactico", token=tok)

    def parse_expression(self):
        izq = self.peek()
        if not izq: return None
        self.pos += 1
        
        siguiente = self.peek()
        if siguiente and siguiente[0] == 'OP':
            op = self.match('OP')[1]
            der = self.peek()
            self.pos += 1
            return ASTNode("OpBinaria", izq=izq[1], op=op, der=der[1])
            
        return izq[1]

# Tokens generados por la Fase 1
tokens_fase1 = [
    ('KEYWORD', 'print'), ('ID', 'x'), ('ASSIGN', '='), ('INT', '5'), ('SEMI', ';'),
    ('KEYWORD', 'if'), ('ID', 'x'), ('OP', '>'), ('INT', '3'), 
    ('KEYWORD', 'print'), ('LPAREN', '('), ('ID', 'x'), ('RPAREN', ')'), 
    ('KEYWORD', 'else'), 
    ('KEYWORD', 'print'), ('LPAREN', '('), ('STRING', '"no"'), ('RPAREN', ')')
]

parser = Parser(tokens_fase1)
ast = parser.parse()

print("--- ARBOL DE SINTAXIS ABSTRACTA (AST) ---")
for nodo in ast:
    print(nodo)