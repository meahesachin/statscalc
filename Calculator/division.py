def division(a, b):
    if float(b) == 0:
        raise ZeroDivisionError('Unable to divide by Zero.')  # Don't actually have to do this, but for the assignment.
    c = float(a)/float(b)
    return format(c, '.9f')
    # return c
