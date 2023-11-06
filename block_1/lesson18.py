text = input()
text = text.lower()
x = [",", "!", "?", ".", ":"]
for i in x:
    text = text.replace(i, "")
print(text)
words = text.split()
count_words = len(words)
print(count_words)
unique_words = []
for i in words:
    if i not in unique_words:
        unique_words.append(i)
print(unique_words)
k = set(words)
print(k)
longest_word = words[0]
small_word = words[0]
for i in words:
    if len(i) > len(longest_word):
        longest_word = i
    if len(i) < len(small_word):
        small_word = i
print(longest_word)
print(small_word)


