n = int(input())
out = ""

roman = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
    }

while n:
    for key in roman:
        while key <= n:
            out += roman[key]
            n -= key
            
print(out)
