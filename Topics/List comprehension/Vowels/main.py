vowels = 'aeiou'
text = input()
out_list = [vow for vow in text if vow in vowels]
print(out_list)