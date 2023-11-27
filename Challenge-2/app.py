# Function to check if exactly two out of three numbers are positive
def twoPositives(a, b, c):
    positiveCount = 0
    
    # Check if 'a' is positive
    if a > 0:
        positiveCount += 1
    
    # Check if 'b' is positive
    if b > 0:
        positiveCount += 1
    
    # Check if 'c' is positive
    if c > 0: 
        positiveCount += 1
    
    # Return True if exactly two numbers are positive, otherwise False
    return positiveCount == 2

# Example usage
print(twoPositives(1, -15, 10))  # Should print True
print(twoPositives(1, -15, 0))   # Should print False
print(twoPositives(1, 5, 2))      # Should print True
