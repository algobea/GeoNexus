def print_section(title: str):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def ambiguous_grammar():
    print_section("1) Gramática ambigua")
    grammar = {
        "E": ["E + E", "E * E", "( E )", "id"]
    }
    for nt, prods in grammar.items():
        print(f"{nt} ::= " + " | ".join(prods))

    print("\nCadena ejemplo: id + id * id")
    print("Derivación 1: id + (id * id)")
    print("Derivación 2: (id + id) * id")

    print("\nÁrbol 1:")
    print("        E")
    print("     /  |   \\")
    print("    E   +    E")
    print("    |       / | \\")
    print("   id      E  *  E")
    print("           |     |")
    print("          id    id")

    print("\nÁrbol 2:")
    print("        E")
    print("     /  |   \\")
    print("    E   *    E")
    print("  / | \\      |")
    print(" E  +  E    id")
    print(" |     |")
    print("id    id")
