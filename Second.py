s = input()
counts = {'k': 0, 'a': 0, 's': 0, 'p': 0, 'e': 0, 'r': 0, 'y': 0}
for c in s:
    if c in counts:
        counts[c] += 1
max_words = min(counts['k'], counts['a'], counts['s'] // 2, counts['p'], counts['e'], counts['r'], counts['y'])
print(max_words)