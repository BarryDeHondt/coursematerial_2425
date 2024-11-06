def goal_amount_dice2(n_sides, goal):
    winning_combinaties = 0
    for dobbelsteen_1 in range(1, n_sides + 1):
        for dobbelsteen_2 in range(1, n_sides + 1):
            if dobbelsteen_1 + dobbelsteen_2 >= goal:
                winning_combinaties += 1
    return winning_combinaties

def goal_amount_dice_3(n_sides, goal):
    winning_combinaties = 0
    for dobbelsteen_1 in range(1, n_sides + 1):
        for dobbelsteen_2 in range(1, n_sides + 1):
            for dobbelsteen_3 in range(1, n_sides + 1):
                if dobbelsteen_1 + dobbelsteen_2 + dobbelsteen_3 >= goal:
                    winning_combinaties += 1
    return winning_combinaties

def rpg2(n_sides, goal):
    winning_combinaties = goal_amount_dice2(n_sides, goal)
    percentage = (winning_combinaties / n_sides**2 ) * 100
    return percentage

def rpg3(n_sides, goal):
    winning_combinaties = goal_amount_dice_3(n_sides, goal)
    percentage = (winning_combinaties / n_sides**3 ) * 100
    return percentage

    
        
    
            
            

        
        