

def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    bondPrice = 0.0

    for t, y in zip(times, yc):

        cf = coupon if t != times[-1] else coupon + face
        pv_factor = 1 / ((1 + y) ** t)
        bondPrice += cf * pv_factor

    return bondPrice