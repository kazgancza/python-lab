nums = list(map(int, input().split()))
nums.pop(-1)

nums_count = {}

for num in nums:
    if num not in nums_count.keys():
        nums_count[num] = 1
    else:
        nums_count[num] += 1
    
highest = max(nums_count.values())

winners = [k for k in nums_count.keys() \
           if nums_count[k] == highest]

print(max(winners))

"""Wyznacz najpopularniejszy element ciągu (to znaczy taki,
który występuje w nim największą
liczbę razy). W przypadku, gdy w ciągu jest więcej niż
jeden najpopularniejszy element, podaj największy z nich.

Wejście
W jednej linii znajduje się ciąg liczb całkowitych zakończony
liczbą 0. Możesz założyć, że liczb
jest co najmniej dwie i nie więcej niż 1000000,
zaś ich wartość mieści się w przedziale [-1018,1018].

Wyjście
Najpopularniejszy element ciągu."""