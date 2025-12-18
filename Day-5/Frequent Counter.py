fruit = "banana"
freq = {}

for i in fruit:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)