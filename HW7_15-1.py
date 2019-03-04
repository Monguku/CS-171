def gcd(a, b):
    remainder = (a % b)
    if remainder == 0:
        return b
    else:
        return gcd(b, remainder)

def main():
    print('Welcome to Fraction Simplifier')
    print('Type "exit" to quit.')
    fraction = input('Enter Fraction (Int/Int):\n')
    while fraction.lower() != 'exit':
        if '/' in fraction:
            num = int(fraction.split('/')[0])
            den = int(fraction.split('/')[1])
        common = gcd(num, den)

        new_num = int(num / common)
        new_den = int(den / common)
        if new_den != 1:
            new_fraction = (str(new_num) + '/' + str(new_den))
        else:
            new_fraction = (str(new_num))
        print('Simplified Fraction\n' + new_fraction)
        fraction = input('Enter Fraction (Int/Int):\n')
    print('Bye.')
main()
