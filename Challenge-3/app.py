# Function to calculate the highest value of consonant substrings in a given word
def solve(word):
    vowels = "aeiou"
    
    # Helper function to calculate the value of a consonant substring
    def value_of_consonant(substring):
        return sum(ord(char) - ord('a') + 1 for char in substring)
    
    # Create a list of consonant substrings by splitting the word at each occurrence of 'a'
    consonant_substrings = [substring for substring in word.split('a') if substring]

    # Initialize the maximum value to 0
    max_value = 0

    # Iterate through each consonant substring
    for substring in consonant_substrings:
        # Calculate the value of the current substring
        substring_value = value_of_consonant(substring)
        # Update the maximum value if the current substring has a higher value
        max_value = max(max_value, substring_value)

    # Return the highest value among consonant substrings
    return max_value

# Example usage
result1 = solve("zodiacs")
print(result1)  # Should print 26

result2 = solve("muthomi")
print(result2)  # Should print 112
