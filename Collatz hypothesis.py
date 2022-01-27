sp = []
def input_valid():
    while True:
        x = int(input("Введите переменную x = "))
        if x > 0:
            collatz(x)
            break
        print("Неверное число, попробуйте другое")
    return x

def x2():
    pass #Кирилл

def x3_1():
    pass #Максим

def collatz():
    while x != 1:
        if x % 2 == 0:
            return x2(x)
        else:
            return x3_1(x)
    print('Список имеет вид:', sp)

input_valid()