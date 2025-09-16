def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend - (quotient * divisor)
    print("Quotient: " + str(quotient) + " Remainder: " + str(remainder))
    return quotient


x = 14
y = 6
divide(x, y)
result = divide(14, 2)
