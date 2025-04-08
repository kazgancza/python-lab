old = input()
new = input()

with open("tekst.txt", "r") as file:
    text = file.read()

after_change = text.replace(old, new)

with open("zamieniony.txt", "w") as file:
    file.write(after_change)

