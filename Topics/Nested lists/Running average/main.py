lst = [int(a) for a in input()]
new_lst = []
ind_count = 0

while ind_count < (len(lst) - 1):
    new_lst.append((lst[ind_count] + lst[ind_count + 1]) / 2)
    ind_count = ind_count + 1
print(new_lst)

