def is_strobogrammatic(num):
    strobogrammatic_pairs = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }
    
    left = 0
    right = len(num) - 1
    
    while left <= right:
        if num[left] not in strobogrammatic_pairs or num[right] not in strobogrammatic_pairs:
            return False
        if num[left] != strobogrammatic_pairs[num[right]]:
            return False
        
        left += 1
        right -= 1
    
    return True


#Driver code
num = "69"
print(is_strobogrammatic(num))  # Output: True
