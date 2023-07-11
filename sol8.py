def check_straight_line(coordinates):
    n = len(coordinates)
    

    if n == 2:
        return True
    
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    initial_slope = (y1 - y0) / (x1 - x0) if (x1 - x0) != 0 else float('inf')
    
    
    for i in range(2, n):
        x0, y0 = coordinates[i - 1]
        x1, y1 = coordinates[i]
        slope = (y1 - y0) / (x1 - x0) if (x1 - x0) != 0 else float('inf')
        
        
        if slope != initial_slope:
            return False
    
    return True

#Driver ocde
coordinates = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(check_straight_line(coordinates))  
