
def encrypt(text, shift, key2=None):
    result = ""
    text = text.upper()
    alpha = [chr(65 + i) for i in range(26)]
    if key2:
        key2 = key2.upper()
        alphabet = list(key2)
        alphabet += alpha
        res = []
        [res.append(x) for x in alphabet if x not in res]
        alpha = res

    trans = {}
    alphabet = [chr(65 + i) for i in range(26)]

    print("\n Полученный алфавит: \n")
    for i in range(26):
        if i + shift < 26:
            trans[alphabet[i]] = alpha[i + shift]
        else:
            trans[alphabet[i]] = alpha[i + shift - 26]

    print(alpha)
    print(list(trans.values()))
    for char in text:
        result += trans[char]

    return result


def decrypt(text, shift, key2=None):
    result = ""
    text = text.upper()
    alpha = [chr(65 + i) for i in range(26)]
    if key2:
        key2 = key2.upper()
        alphabet = list(key2)
        alphabet += alpha
        res = []
        [res.append(x) for x in alphabet if x not in res]
        alpha = res


    trans = {}
    alphabet = [chr(65 + i) for i in range(26)]

    print("\n Полученный алфавит: \n")
    for i in range(26):
        if i + shift < 26:
            trans[alpha[i + shift]] = alpha[i + shift] = alphabet[i]
        else:
            trans[alpha[i + shift - 26]] = alphabet[i]

    print(alpha)
    print(list(trans.values()))
    for char in text:
        result += trans[char]

    return result

def caesar(text):
    text = text.split()

    if text[0] == 'e':
        if len(text) == 3:
            return encrypt(text[1], int(text[2]))
        else:
            return encrypt(text[1], int(text[2]), text[3])
    elif text[0] == 'd':
        if len(text) == 3:
            return decrypt(text[1], int(text[2]))
        else:
            return decrypt(text[1], int(text[2]), text[3])


print("\n\nВведите аргументы в следующем формате: ")
print("Первый параметр - 'e' или 'd'")
print("     e - зашифровать")
print("     d - расшифровать")
print("Второй параметр - строка, которую надо обработать")
print("Третий параметр - ключ (сдвиг) шифра")
s = str(input("\nВвод: "))
result = caesar(s)
print("\nРезультат:", result)



