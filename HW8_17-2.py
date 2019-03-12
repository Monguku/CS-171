def rev(text):
    return text[::-1]

if __name__ == "__main__":
    print("Welcome to Digit Flipper")
    userIn = str(input("Enter Some Text:\n"))
    newString = ''
    int_list = []
    int_list.append([])
    digits = "0123456789"
    count = 0
    for c in range(len(userIn)): #get 2d array of integers in the input
        if c + 1  < len(userIn):
            next_char = userIn[c + 1]
            if userIn[c] in digits:
                int_list[count].append(userIn[c])
                if next_char not in digits:
                    int_list.append([])
                    count += 1

        elif userIn[c] in digits:
            int_list[count].append(userIn[c])


    for i in range(len(int_list)):
        for ii in range(len(int_list[i])):
            newString += int_list[i][ii]
        newString += '.'

    int_list = newString.split('.')
    int_list.pop()

    for i in range(len(int_list)):
        userIn = userIn.replace(int_list[i], rev(int_list[i]))
    print("Revised String:")
    print(userIn)
