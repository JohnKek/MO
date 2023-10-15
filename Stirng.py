s = input().split()
n = int(input())
words = set()
for i in range(n):
    words.add(input().strip().lower())

for word in s:
    stripped_word = word.strip(',.!?')
    if stripped_word.lower() in words:
        print(word, end=' ')
    else:
        print('~' * len(stripped_word), end=' ')
print('\n' + '.'.join(['~' * len(word.strip(',.!?')) for word in s]))