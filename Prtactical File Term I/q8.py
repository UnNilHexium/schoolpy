punct = "'/.,;:><?{}[]_+-=\\|()*&^%$#@!~\""

with open("mails.txt", "r") as f:
    for line in f:
        cleanline = line.lower()
        for p in punct:
            cleanline = cleanline.replace(p, "")
        words = cleanline.split()
word_counts = {}
for w in words:
    if w in word_counts:
        word_counts[w] = word_counts[w] + 1 
    else:
        word_counts[w] = 1
max_count = max(word_counts.values())  
winners = []
for word in word_counts:
    if word_counts[word] == max_count:
        winners.append(word)
print("Highest Count:", max_count)
print("Most Common Word(s):", winners)