def twoscomp(num):
    newNum = ''
    for n in num:
        if n == '0':
            newNum += '1'
        elif n == '1':
            newNum += '0'
    reverseNum = reverse(newNum)
    try:
        firstZero = reverseNum.index('0')
    except:
        return num
    reverseNum = reverseNum[:firstZero] + '1' + reverseNum[firstZero + 1:]
    reverseNum = reverseNum.replace('1', '0', firstZero)
    newNum = reverse(reverseNum)
    return newNum

def reverse(s):
    return s[::-1]
if __name__ == "__main__":
    print ("Welcome to Two's Complement Creator")
    userIn = (input('Enter a Binary Value:\n'))
    print("In Two's Complement:\n" + twoscomp(userIn))
