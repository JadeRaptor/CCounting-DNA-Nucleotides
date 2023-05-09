s = input("Enter a DNA string: ")

count = [0, 0, 0, 0]

for symbol in s:
    if symbol == 'A':
        count[0] += 1
    elif symbol == 'C':
        count[1] += 1
    elif symbol == 'G':
        count[2] += 1
    elif symbol == 'T':
        count[3] += 1
print(' '.join(str(x) for x in count))

