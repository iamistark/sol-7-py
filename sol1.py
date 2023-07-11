def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    char_map = {}  # Mapping of characters from s to t
    used_chars = set()  # Set to keep track of characters already mapped
    
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        if char_s in char_map:
            if char_map[char_s] != char_t:
                return False
        else:
            if char_t in used_chars:
                return False
            char_map[char_s] = char_t
            used_chars.add(char_t)
    
    return True

#Driver code
s = "egg"
t = "add"
print(is_isomorphic(s, t))  # Output: True
