def election_winner(votes):
    if not votes:
        return None
    
    stemmen = {}
    
    for stem in votes:
        if stem in stemmen:
            stemmen[stem] += 1
        else:
            stemmen[stem] = 1
    winnaar = max(stemmen, key=stemmen.get)
    return winnaar
            









































        