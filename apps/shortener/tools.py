CHARACTERS = list(
    map(chr, range(97, 123))) + list(
        map(chr, range(65, 91))) + list(map(str, range(0, 10)))


def shorten_url(pk):
    pk = int(pk)
    digits = []
    while pk > 0:
        digit = int(pk % 62)
        digits.append(digit)
        pk = int(pk // 62)
    digits.reverse()
    result = ''
    for digit in digits:
        result += CHARACTERS[digit]
    return result
