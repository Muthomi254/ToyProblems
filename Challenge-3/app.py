def solve(word):
    vowels = "aeiou"
    
    def value_of_consonant(substring):
        return sum(ord(char) - ord('a') + 1 for char in substring)
    
    consonant_substrings = [substring for substring in word.split('a') if substring]

    max_value = 0
    for substring in consonant_substrings:
        substring_value = value_of_consonant(substring)
        max_value = max(max_value, substring_value)

    return max_value


result1 = solve("zodiacs")
print(result1)  

result2 = solve("muthomi")
print(result2)  
