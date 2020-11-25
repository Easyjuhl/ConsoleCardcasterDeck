def CardlistReset(CardcasterLvl):
    Cardlist = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant"]
    Cardlist2 = ["The Lovers", "The Chariot"]
    Cardlist3 = ["Justice", "The Hermit"]
    Cardlist4 = ["Wheel of Fortune", "Strength"]
    Cardlist5 = ["The Hanged Man", "Death"]
    Cardlist6 = ["Temperance", "The Devil"]
    Cardlist7 = ["The Tower", "The Star"]
    Cardlist8 = ["The Moon", "The Sun"]
    Cardlist9 = ["Judgment", "The World"]
        
    if CardcasterLvl > 2:
        Cardlist.extend(Cardlist2)

    if CardcasterLvl > 4:
        Cardlist.extend(Cardlist3)

    if CardcasterLvl > 6:
        Cardlist.extend(Cardlist4)

    if CardcasterLvl > 8:
        Cardlist.extend(Cardlist5)

    if CardcasterLvl > 10:
        Cardlist.extend(Cardlist6)
        
    if CardcasterLvl > 12:
        Cardlist.extend(Cardlist7)
    
    if CardcasterLvl > 14:
        Cardlist.extend(Cardlist8)

    if CardcasterLvl > 16:
        Cardlist.extend(Cardlist9)
    
    return Cardlist