from src.ambiguidad import ambiguous_grammar
from src.left_recursion import eliminate_left_recursion
from src.left_factoring import left_factoring


def main():
    ambiguous_grammar()
    eliminate_left_recursion()
    left_factoring()


if __name__ == "__main__":
    main()
