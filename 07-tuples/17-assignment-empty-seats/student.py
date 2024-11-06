def empty_seats(used_seats):
    lege_stoel = 0
    for seats in range(1, len(used_seats)):
        lege_stoel += used_seats[seats] - used_seats[seats - 1] - 1
    return lege_stoel
        
        