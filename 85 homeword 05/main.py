class Cable:
    def __init__(self, wire, battery):
        self.wire = wire
        self.battery = battery

    def __lt__(self, other):
        return (self.wire - self.battery) < (other.wire - other.battery)

n = int(input().strip())

cables = []
for _ in range(n):
    wire, battery = map(int, input().split())
    cables.append(Cable(wire, battery))
cables.sort()

sum_wire = 0
sum_battery = 0
count = 0

for cable in cables:
    sum_wire += cable.wire
    sum_battery += cable.battery
    if sum_battery <= sum_wire:
        count += 1
    else:
        break

print(count)


