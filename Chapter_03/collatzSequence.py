def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    try:
        number = int(input())
        break
    except ValueError:
        print('Input must be an integer.')
while number != 1:
    number = collatz(number)
