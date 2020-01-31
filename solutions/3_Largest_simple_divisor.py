'''
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
'''

n = 600851475143
denominator = 1

while denominator < n:
    # Number is odd, then the factor must be odd (!)
    denominator += 2
    while n % denominator == 0:
        n = n / denominator

print(denominator)
