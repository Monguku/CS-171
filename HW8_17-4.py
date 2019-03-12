bars = {'1' : ':::||', '2' : '::|:|', '3' : '::||:', '4' : ':|::|', '5' : ':|:|:', '6' : ':||::', '7' : '|:::|', '8' : '|::|:', '9' : '|:|::', '0' : '||:::'}

def checksum(zip):
    sum = 0
    for x in zip:
        sum += int(x)
    str_sum = str(sum)
    if sum % 10 ==0:
        check = 0
    elif sum >= 10:
        initial_digit = str_sum[0]
        initial_digit = int(initial_digit)
        check = (initial_digit+1)*10 - sum
    else:
        check = 10-sum
    return str(check)
def barcode(zip):
    bar_string = ''
    bar_string += '|'
    for x in zip:
        bar_string += bars[x]
    bar_string += bars[checksum(zip)]
    bar_string += '|'
    return bar_string
if __name__ == "__main__":
    print('Welcome to Bar Code Generator')
    userIn = input("Enter Zip Code (exit to quit):\n")
    while userIn.lower() != 'exit':
        print("Bar Code:")
        print(barcode(userIn))
        userIn = input("Enter Zip Code (exit to quit):\n")
    print("Thanks for using me.")
