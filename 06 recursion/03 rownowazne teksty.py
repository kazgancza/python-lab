def divide(s):

    if len(s) % 2 == 1:
        return s 
    mid = len(s) // 2
    left, right = divide(s[:mid]), divide(s[mid:])
    
    return min(left + right, right + left) 

def program(text1, text2):
    return divide(text1) == divide(text2)

t1 = input().strip()
t2 = input().strip()

if program(t1, t2):
    print("TAK")
else:
    print("NIE")