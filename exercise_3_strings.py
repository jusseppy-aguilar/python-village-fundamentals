import sys

def slice_string(text: str, a: int, b: int, c: int, d: int) -> str:
    """
    Extracts specific substrings from a given text based on dynamically provided indices.
    Adjusts for inclusive slicing by adding 1 to the end indices.
    """
    first_slice = text[a:b+1]
    second_slice = text[c:d+1]
    
    return f"{first_slice} {second_slice}"

def main() -> None:
    """
    Main execution function.
    Reads multi-line input from sys.stdin: the text string on the first line,
    and the four slicing indices on the second line.
    """
    input_data = sys.stdin.read().strip().split('\n')
    text = input_data[0]
    a, b, c, d = map(int, input_data[1].split())
    result = slice_string(text, a, b, c, d)
    print(result)

if __name__ == "__main__":
    main()
