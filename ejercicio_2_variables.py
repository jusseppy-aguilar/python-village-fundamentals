import sys

def sum_of_squares(a: int, b: int) -> int:
    """
    Computes the sum of the squares of two integers.
    This modular function can be reused in distance calculations
    or basic computational biology algorithms.
    """
    return a**2 + b**2

def main() -> None:
    """
    Main execution function.
    Designed to receive data directly injected from the standard input (sys.stdin),
    making it ideal for automated pipelines and high-performance computing (HPC).
    """
    # Reads all incoming standard input, splits by whitespace, and maps to integers
    a, b = map(int, sys.stdin.read().split())
    
    # Executes the calculation and prints the final result
    print(sum_of_squares(a, b))

if __name__ == "__main__":
    main()
