sentence = input("Enter sentence: ")
sentence = sentence.lower()
words = sentence.split()
lengths = []
for word in words:
    lengths.append(len(word))

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if len(words[i]) > len(words[j]):
            words[i], words[j] = words[j], words[i]

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if len(words[i]) == len(words[j]):
            if words[i] > words[j]:
                words[i], words[j] = words[j], words[i]

for word in words:
    print(word, "-", len(word), "letters")
