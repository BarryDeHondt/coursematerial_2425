def heatwave(temperatures):
    
    count_25 = 0
    count_30 = 0
    
    for temp in temperatures:
        if temp >= 25:
            count_25 += 1
        if temp >= 30:
            count_30 += 1
        if temp < 25:
            count_25 = 0
            count_30 = 0
        hittegolf = count_25 >= 5 and count_30 >= 3
        if hittegolf:
            return True
    return False
        
    
    