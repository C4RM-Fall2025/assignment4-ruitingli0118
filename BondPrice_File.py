

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)           
    i = y / ppy                 
    c = face * couponRate / ppy 

    if i == 0:
        return c * n + face

    annuity_pv = sum(1 / ((1 + i) ** t) for t in range(1, n + 1))
    bondPrice = c * annuity_pv + face / ((1 + i) ** n)
    return bondPrice

