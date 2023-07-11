def can_shift_string(s, goal):
    if len(s) != len(goal):
        return False
    
    shifted_string = s + s
    
    return goal in shifted_string

#Driver code
s = "abcde"
goal = "cdeab"
print(can_shift_string(s, goal))  
