from .ambiguidad import print_section


def left_factoring():
    print_section("3) Factorización por la izquierda")
    print("Gramática original:")
    print("S ::= if E then S else S | if E then S | a")

    print("\nPrefijo común:")
    print("if E then S")

    print("\nGramática factorizada:")
    print("S ::= if E then S S' | a")
    print("S' ::= else S | ε")
