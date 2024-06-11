import textwrap


def justify(text, width):
    lines = textwrap.wrap(text, width)
    for line in lines:
        space = width - len(line)
        words = line.split()

        # prevent method being applied to last line
        if lines.index(line) == len(lines) - 1:
            break

        if len(words) > 1:
            for i in range(space):
                if i >= len(words) - 1:
                    i = i % (len(words) - 1)

                words[i] = words[i] + ' '

        lines[lines.index(line)] = (' '.join(words))

    return ('\n'.join(lines))


def justify(t, w):
    c = t.rfind(' ', 0, w + 1)
    if c == -1 or len(t) <= w:
        return t
    c = t[:c]
    t = t[len(c) + 1:]
    x = ' '
    if c.count(' ') != 0:
        while len(c) != w:
            if w - len(c) >= c.count(x):
                c = c.replace(x, x + ' ')
                x += ' '
            else:
                c = c.replace(x, x + ' ', w - len(c))
    return c + '\n' + justify(t, w)
