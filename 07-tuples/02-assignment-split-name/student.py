def split_name(full_name):
    spatie = full_name.find(' ')
    
    voornaam = full_name[0:spatie]
    achternaam = full_name[spatie + 1:]
       
    return (voornaam,achternaam)