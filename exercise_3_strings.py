import sys

def extract_substrings(text: str) -> tuple[str, str]:
    """
    Extract specific substrings from a given text based on fixed indices.
    Args:
        text (str): Input string.
    Returns:
        tuple[str, str]: Extracted substrings.
    """
    first_substring = text[79:89]
    second_substring = text[149:157]
    return first_substring, second_substring

def main() -> None:
    text = sys.stdin.read().strip()
    first, second = extract_substrings(text)
    print(first, second)

if __name__ == "__main__":
    main()
