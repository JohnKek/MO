def spell_check(text, dictionary):
    words = text.split()
    result = ''
    for word in words:
        if word.strip(',.!?').lower() in [w.lower() for w in dictionary if w]:
            result += '.' * len(word) + '.'
        else:
            result += '~' * len(word) + '.'
    return result[:-1]


# Пример использования функции
text = input()
n = int(input())
dictionary = []
for i in range(n):
    dictionary.append(input())

print(text)
print(len(text))
print(spell_check(text, dictionary))
print(len(spell_check(text, dictionary)))
#%%
