
WORDS = []

with open("IELTS Word List.txt", "r", encoding="utf-8") as f:
    line = ""
    while "EOF" not in line:
        line = f.readline()
        if "Word List" in line or line == '\n':
            continue
        WORDS.append(line.split(" "))

# for word in WORDS:
#     print(word)

with open("IELTS Word List - formated.txt", "w", encoding="utf-8") as f:
    for word in WORDS:
        f.write(word[0])
        f.write('\t')
        for item in word[1:]:
            if item and item != '\n':
                f.write(' ')
                f.write(item)


