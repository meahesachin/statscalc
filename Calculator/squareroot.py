import math


def squareroot(a):

    c = math.sqrt(float(a))

    fmt = ""
    if c.is_integer():
        fmt = ".1f"
    else:
        fmt = ".8f"
    return format(c, fmt)

    return float(c)