

def getBondPrice_E(face, couponRate, yc):
    coupon = face * couponRate
    bondPrice = 0

    # enumerate starts at index 0, so add 1 to get the time period t
    for t, y in enumerate(yc, start=1):
        if t < m:
            cf = coupon
        else:
            # Last period gets coupon + face
            cf = coupon + face
        pv_factor = 1 / ((1 + y) ** t)
        bondPrice += cf * pv_factor

    return bondPrice
