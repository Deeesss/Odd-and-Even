def cislo(num):

    if num % 2 == 0:

        return "even"

    return "odd"
while True:
    num = int(input('Enter the number: '))
    print(cislo(num))