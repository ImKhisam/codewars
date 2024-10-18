def decode(s):
    dictionary = 'abdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqH'
    res = ''
    k = 0
    for i in s:
        k += 1
        if i in "!@#$%^&*()_+-=/":
            res += i
        else:
            x = dictionary.find(i)
            y = (dictionary.find(i) - k) % len(dictionary)
            z = dictionary[(dictionary.find(i) - k) % len(dictionary)]
            res += dictionary[(dictionary.find(i) - k) % len(dictionary)]
        s = s[1::]

    return res

print(decode('=Z8!.vYY9dGC06jjGJc'))

