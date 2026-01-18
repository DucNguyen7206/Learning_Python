# Given a binary string X.
# Converting X into a number in base-b (b is one of these bases: 2, 4, 8, 16).
# For example: X = "10010100010010101", b = 8 -> Output: 224225 (since 10010100010010101 is 224225 in base-8).

def convert_to_base_4(n):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(str(n % 4))
        n //= 4
    result = "".join(digits[::-1])
    return result

def convert(base, n):
    dec = int(n, 2) # convert to decimal
    
    if base == 2:
        return bin(dec)[2:]
    elif b == 4:
        return convert_to_base_4(dec)
    elif b == 8:
        return oct(dec)[2:]
    elif b == 16:
        return hex(dec)[2:].upper() # remember to always use uppercase in base-16

test = int(input())
for _ in range(test):
    b = int(input())
    x = input() # binary string
    print(convert(b, x))