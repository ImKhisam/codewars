def top_words(text):
    res = {}
    textf = ''.join(char.lower() if char.isalpha() or char == ' ' or char == "'" else ' ' for char in text).split(' ')
    for word in textf:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    if '' in res:
        res.pop('')
    elif "'" in res:
        res.pop("'")
    elif "'''" in res:
        res.pop("'''")
    return sorted(res, key=res.get, reverse=True)[:3]

text = "'"
print(top_words(text))

