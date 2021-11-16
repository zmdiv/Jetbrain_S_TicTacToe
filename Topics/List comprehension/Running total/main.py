int_list = [int(a) for a in input()]
final_list = []
x = 0

for b in int_list:
    final_list.append(x + b)
    x += b
print(final_list)
