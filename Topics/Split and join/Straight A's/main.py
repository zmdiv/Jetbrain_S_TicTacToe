grades = input().upper().split()
a_list = [a for a in grades if a == "A"]
print(round(len(a_list) / len(grades), 2))