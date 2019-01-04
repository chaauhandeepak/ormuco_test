from twostring import ValueComparsions

if __name__ == '__main__':
    try:
        str1 = input('Enter a string Number 1\n')
        str2 = input('Enter a string Number 2 \n')
        result = ValueComparsions(str1, str2)
        if str1 == str2:
            print(result.equal())
            print('{0} and {1} are not greater or \nlesser to each other'.format(str1, str2))
        else:
            print(result.greater())
            print(result.equal())
            print(result.lesser())

    except ValueError:
        print('\n')
        print('_' * 42)
        print('Characters, strings are not allowed\n'
              "Please Enter only numbers \n{0}".format('_' * 42))
