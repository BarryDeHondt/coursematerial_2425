def increase_version(version, breaking_change, new_features):
    if breaking_change:
        version = (version[0] + 1, 0, 0)
    elif new_features:
        version = (version[0], version[1] + 1, 0)
    else:
        version = (version[0], version[1], version[2] + 1)
    return (version)

print(increase_version((6, 5, 2), breaking_change=True, new_features=True))

            
        
def  is_more_recent(v1, v2):
    
    for getallen in v1,v2:
        if v1[0] > v2[0]:
            return True
        elif v1[0] == v2[0]:
            if v1[1] > v2[1]:
                return True
            elif v1[1] == v2[1]:
                if v1[2] > v2[2]:
                    return True
    return False

def is_older(v1, v2):
    return v1 < v2
            
        
    