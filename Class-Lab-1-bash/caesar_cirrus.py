print('Please enter your coded message:')
text = input()
if text == 'default' or text == 'Default':
    text = 'Pbatenghyngvbaf, lbh unir fhpprrqrq va qrpelcgvat gur fgevat.'
    shift = 13
else:
    print('Please enter by how many letters you would like to shift the message DOWN:')
    shift = int(input())

deciphered = ''

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for codelet in text:
    if codelet in lowercase:
        letindex = lowercase.index(codelet)
        letshift = letindex - shift
        if letshift > 25:
            letshift -= 26
        if letshift < 0:
            letshift += 26
        deciphered += lowercase[letshift]
    elif codelet in uppercase:
        letindex = uppercase.index(codelet)
        letshift = letindex - shift
        if letshift > 25:
            letshift -= 26
        if letshift < 0:
            letshift += 26
        deciphered += uppercase[letshift]
    else:
        deciphered += codelet
print(deciphered)