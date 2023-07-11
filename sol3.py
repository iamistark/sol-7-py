def add_strings(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = []
    
    while i >= 0 or j >= 0 or carry > 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        
        # Calculate the sum of digits and the carry
        digit_sum = digit1 + digit2 + carry
        carry = digit_sum // 10
        digit_sum %= 10
        
        # Prepend the sum digit to the result list
        result.insert(0, str(digit_sum))
        
        i -= 1
        j -= 1
    
    return ''.join(result)
 #Driver code
 num1 = "11"
num2 = "123"
print(add_strings(num1, num2))  # Output: "134"
