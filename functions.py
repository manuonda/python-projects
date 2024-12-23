def say_hello():
    print("hola mindo")


def count_to(number):
    for i in range(1,number):
        print(i)

def multiply(number1, number2):
    result = number1 * number2
    print(f'El resultaod es {result}')

def full_name(first_name , last_name):
    full_name = first_name + last_name
    print(f'El full_name es : {full_name}')

count_to(10)
multiply(1,2)
full_name('David','Garcia')


def foo():
    return 1, 'david garcia',45


print(type(foo()))
numero, nombre, edad = foo()
print(numero, nombre, edad)

def calculate_total(price, tax = 0.0 , discount = 0):
    total = price + (price * tax) - discount
    return total

total = calculate_total(100,0.0,10)
print(total)

total = calculate_total(23,3)
print(total)


def show_info(username, email, *scopes):
    print(username)
    print(email)

    average = sum(scopes) /len(scopes)
    print(average)

show_info(
    "cody","manuonda@gmail.com",
    10,10,10,23
)