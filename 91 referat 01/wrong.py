
"""
Ta wersja znajduje najdłuższy malejący ciągły podciąg
"""

n = int(input().strip())
numbers = []

for _ in range(n):    

    number = int(input().strip())
    numbers.append(number)


current_pos = 0
current_streak = 1

high_pos = 0
high_streak = 1

for i in range(1, n):
    if numbers[i] < numbers[i-1]:
        
        current_streak += 1
        if current_streak > high_streak:
        
            high_streak = current_streak
            high_pos = current_pos
    else:
        
        current_pos = i
        current_streak = 1
        
if high_streak == 1:
    
    print("Brak malejącego podciągu")
else:
    
    print(f"{high_pos+1}-{high_pos+high_streak}")
