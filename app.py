def reverse_string(s):
    """
    Reverses the given string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == "__main__":
    # Example usage
    original = "Kadappa"
    reversed_str = reverse_string(original)
    print(f"Original: {original}")
    print(f"Reversed: {reversed_str}")