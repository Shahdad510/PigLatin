sentence = input('Enter your sentence...')

c = ["c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z", "y"]

words = sentence.split()

new_sentence = ''
for word in words:
    
    if word[0] in c:
        count = 0
        while word[0] in c and len(word) != count:
            word += word[0]
            word = word[1:]
            count += 1
        new_sentence += word
        new_sentence += 'ay'
        new_sentence += ' '
    else:
        new_sentence += word
        new_sentence += 'way'
        new_sentence += ' '
print(new_sentence)