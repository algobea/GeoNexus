from .ambiguidad import print_section


def eliminate_left_recursion():
    print_section("2) Eliminación de recursividad por la izquierda")
    print("Gramática original:")
    print("A ::= A a | A b | c")

    print("\nPaso 1: separar producciones recursivas y no recursivas")
    print("Recursivas: A a, A b")
    print("No recursivas: c")

    print("\nPaso 2: crear un nuevo no terminal A'")
    print("A ::= c A'")
    print("A' ::= a A' | b A' | ε")

    print("\nGramática resultante:")
    print("A ::= c A'")
    print("A' ::= a A' | b A' | ε")
