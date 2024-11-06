def election_winner(votes):
    
    common_element = ''
    
    for vote in range(len(sorted(votes))):
        
        if votes[vote] == votes[vote] + 1:
            common_element.insert(vote)
    return common_element