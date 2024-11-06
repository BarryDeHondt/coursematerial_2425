def split_in_two(xs):
    n = len(xs)
    if n % 2 == 0:
        n // 2
    if n % 2 != 0:
        links = xs[:n // 2 + 1]
    else:
        links = xs[:n // 2]
    if n % 2 != 0:
        rechts = xs[n // 2 + 1: ]
    else:
        rechts = xs[n // 2: ]
    return (links,rechts)
    
        
             
        

        