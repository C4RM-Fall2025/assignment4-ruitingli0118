
def getBondDuration(y, face, couponRate, m, ppy = 1):
    n = int(m * ppy)              
    i = y / ppy                    
    c = face * couponRate / ppy   

    price = 0
    weighted_pvcf_sum = 0

    for t in range(1, n + 1):
        pv_factor = 1 / ((1 + i) ** t)

        cf = c if t < n else (c + face)

        pvcf = cf * pv_factor
        price += pvcf

        weighted_pvcf_sum += (t / ppy) * pvcf

    bondDuration = weighted_pvcf_sum / price
    return bondDuration
