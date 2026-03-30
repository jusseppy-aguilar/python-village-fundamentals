import sys

def sum_of_odd_integers(start: int, end: int) -> int:
    """
    Compute the sum of all odd integers within a closed interval [start, end].
    Args:
        start (int): Lower bound of the interval.
        end (int): Upper bound of the interval.
    Returns:
        int: Sum of all odd integers in the interval.
    """
    return sum(i for i in range(start, end + 1) if i % 2 != 0)

def main() -> None:
    start, end = map(int, sys.stdin.read().split())
    result = sum_of_odd_integers(start, end)
    print(result)

if __name__ == "__main__":
    main()
