%{
#include <stdio.h>
%}

%option noyywrap

%%

"fn"        { printf("TOKEN: KW_FN, Lexema: %s\n", yytext); }
"let"       { printf("TOKEN: KW_LET, Lexema: %s\n", yytext); }
"mut"       { printf("TOKEN: KW_MUT, Lexema: %s\n", yytext); }
"return"    { printf("TOKEN: KW_RETURN, Lexema: %s\n", yytext); }
"if"        { printf("TOKEN: KW_IF, Lexema: %s\n", yytext); }
"else"      { printf("TOKEN: KW_ELSE, Lexema: %s\n", yytext); }
"i32"       { printf("TOKEN: TYPE_I32, Lexema: %s\n", yytext); }
"f64"       { printf("TOKEN: TYPE_F64, Lexema: %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]* { printf("TOKEN: IDENTIFICADOR, Lexema: %s\n", yytext); }
[0-9]+                  { printf("TOKEN: ENTERO, Lexema: %s\n", yytext); }
[0-9]+\.[0-9]+          { printf("TOKEN: DECIMAL, Lexema: %s\n", yytext); }

"+"         { printf("TOKEN: OP_SUMA, Lexema: %s\n", yytext); }
"-"         { printf("TOKEN: OP_RESTA, Lexema: %s\n", yytext); }
"="         { printf("TOKEN: OP_ASIGNACION, Lexema: %s\n", yytext); }
"=="        { printf("TOKEN: OP_IGUALDAD, Lexema: %s\n", yytext); }

";"         { printf("TOKEN: PUNTO_COMA, Lexema: %s\n", yytext); }
"{"         { printf("TOKEN: LLAVE_ABRE, Lexema: %s\n", yytext); }
"}"         { printf("TOKEN: LLAVE_CIERRA, Lexema: %s\n", yytext); }
"("         { printf("TOKEN: PARENTESIS_ABRE, Lexema: %s\n", yytext); }
")"         { printf("TOKEN: PARENTESIS_CIERRA, Lexema: %s\n", yytext); }
":"         { printf("TOKEN: DOS_PUNTOS, Lexema: %s\n", yytext); }

"//".* { /* Ignorar comentarios de una linea */ }
[ \t\n\r]+  { /* Ignorar espacios en blanco y saltos de linea */ }

.           { printf("ERROR LEXICO: Caracter no reconocido: %s\n", yytext); }

%%

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            perror("Error al abrir el archivo");
            return 1;
        }
        yyin = file;
    }
    yylex();
    return 0;
}