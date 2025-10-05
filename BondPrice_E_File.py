

def getBondPrice_E(face, couponRate, yc):
    m = len(yc)
    coupon = face * couponRate
    price = 0.0

    for t, y in enumerate(yc, start=1):
        cf = coupon + (face if t == m else 0)
        price += cf / ((1 + y) ** t)

    return price
