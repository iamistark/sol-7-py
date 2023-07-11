def backspace_compare(s, t):
    def process_string(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)
    
    return process_string(s) == process_string(t)
 

 #Driver code
 s = "ab#c"
t = "ad#c"
print(backspace_compare(s, t))  # Output: True
