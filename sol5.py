def reverse_string(s, k):
    chars = list(s)
    n = len(chars)
    
    for i in range(0, n, 2*k):
        left = i
        right = min(i + k - 1, n - 1)  # Check if there are fewer than k characters left
        
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    
    return ''.join(chars)

#Driver code
s = "abcdefg"
k = 2
print(reverse_string(s, k))  # Output: "bacdfeg"

