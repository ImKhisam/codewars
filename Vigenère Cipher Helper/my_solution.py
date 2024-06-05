class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def func(self, text, operation):
        res = ''
        for index, symbol in enumerate(text):
            if symbol not in self.alphabet:
                res += symbol
            else:
                sc = self.alphabet.index(symbol)
                if index > (len(self.key) - 1):
                    diff = self.alphabet.index(self.key[index % len(self.key)])
                else:
                    diff = self.alphabet.index(self.key[index])

                ind = sc + diff if operation == '+' else sc - diff
                res += self.alphabet[ind % len(self.alphabet)]
            print(res)
        return res

    def encode(self, text):
        return self.func(text, '+')

    def decode(self, text):
        return self.func(text, '-')


alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'    # 16 0 19 19 23 15 18 3


c = VigenereCipher(key, alphabet);

print(c.encode("it's a shift cipher!"))
#print(c.decode('laxxhsj'))
