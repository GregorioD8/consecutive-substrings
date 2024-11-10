def consecutive_substrings(s):
    """
    Generates all consecutive substrings of a given string.

    Consecutive substrings are formed by taking each character and 
    extending it to include the following characters in sequence. 
    For example, given the input 'abc', the consecutive substrings 
    would be ['a', 'ab', 'abc', 'b', 'bc', 'c'].

    Args:
        s (str): The input string to generate consecutive substrings from.

    Returns:
        list: A list of all consecutive substrings in the order they appear.

    Example:
        >>> consecutive_substrings('abc')
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
    """
    
    # Initialize an empty list to store all consecutive substrings
    substrings = []
    
    # Outer loop: iterate over each starting character in the string
    for start in range(len(s)):
        # Inner loop: generate substrings starting at 'start' and ending at each position up to the end
        for end in range(start + 1, len(s) + 1):
            substrings.append(s[start:end])  # Append substring from 'start' to 'end' (inclusive start, exclusive end)
    
    return substrings


# Test cases
print(consecutive_substrings('abc'))  # Expected output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
print(consecutive_substrings('a'))    # Expected output: ['a']
print(consecutive_substrings(''))     # Expected output: []
print(consecutive_substrings('xyz'))  # Expected output: ['x', 'xy', 'xyz', 'y', 'yz', 'z']