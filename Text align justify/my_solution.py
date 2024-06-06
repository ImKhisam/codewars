def justify(text, width):
    res = ''''''
    t = text.split()
    k, s, curr_line, next_line_word, words = 0, '', '', '', []
    for x in t:
        if len(curr_line) == 0:
            if next_line_word != '':
                curr_line += next_line_word
                words.append(next_line_word)
                next_line_word = ''
                k = 1
            if len(curr_line + x) + k <= width:
                curr_line += x
                words.append(x)
            else:
                s = curr_line
                next_line_word = x
        else:
            k += 1
            if len(curr_line + x) + k <= width:
                curr_line += x
                words.append(x)
            else:
                next_line_word = x
                if len(words) == 1:
                    s = words[0]
                else:
                    spaces_number = width - len(curr_line)
                    spaces_list = [spaces_number // (len(words) - 1)
                                   + int(i < (spaces_number % (len(words) - 1)))
                                   for i in range(len(words) - 1)] + [0]

                    s = ''.join([(w + ' ' * spaces_number) for w, spaces_number in zip(words, spaces_list)])

        if s != '':
            res += s + '\n'
            k, s, curr_line, words = 0, '', '', []

        if x == t[-1]:
            if next_line_word != '':
                res += next_line_word
            else:
                res += ' '.join(x for x in words)

    return res


a = "123 45 6"
b = 'Lorem  ipsum  dolor  sit amet, consectetur  adipiscing  elit. Vestibulum    sagittis   dolor mauris,  at  elementum  ligula tempor  eget.'
c = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
d = 'nCwkP Qvgawo eVZeQzmp AaqBPaOwz qIefq Ts PwukvVPOLY OiYnU IpyLKQLqWu rE'

print(justify(d, 20))
