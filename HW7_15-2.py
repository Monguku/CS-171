def fractal(length, spaces):
    out = ''
    if length == 1:
        for x in range(spaces):
            out += (' ')
        out += ('*')

    else:
        out += (fractal(length//2, spaces))
        out += ('\n')
        for x in range(spaces):
            out += (' ')
        for y in range(length):
            out += ('*')
        out += ('\n')
        out += (fractal(length//2, spaces + (length//2)))

    return out
def main():
    print('Fractal Generator')
    while True:
        try:
            i = input('Enter an integer > 0:\n')
            i = int(i)
        except:
            continue
        print(fractal(i, 0))
        break
main()
