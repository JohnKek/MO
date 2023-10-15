def spell_check(text, dictionary):
    words = text.split()
    result = ''
    for word in words:
        if word.lower() in [w.lower() for w in dictionary]:
            result += '.' * len(word) + ' '
        else:
            result += '~' * len(word) + ' '
    return result.strip()


# Пример использования функции
text = input()
n = int(input())
dictionary = {}
for i in range(n):
    dictionary[i] = input()

print(text)
print(spell_check(text, dictionary))
