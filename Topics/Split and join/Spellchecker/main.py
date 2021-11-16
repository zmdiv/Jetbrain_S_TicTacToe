dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
new_words = input().split()
counter = 0
for word in new_words:
    if word not in dictionary:
        print(word)
        counter += 1
if counter == 0:
    print("OK")
