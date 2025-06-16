# def sum(x, y):
#     result = x + y
#     return result


# print('My first calculator ')

# number1 = int(input('Enter the first number: '))
# number2 = int(input('Enter the secund number: '))

# add = sum(number1, number2)

# print(f'The sum of number {number1} and the number {number2} = {add} ')

print("Calculator your BMI")

weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))

def bmiCalculator(weight, height):    
    result = weight / (height ** 2)
    
    if result < 19.1:
        print(f'Seu BMI = {result:.2f}')
        return "Até 19.1 você esta baixo do peso"
    elif result > 19.2 and result <= 25.8:
        print(f'Seu BMI = {result:.2f}')
        return "Entre 19.2 e 25.8: Peso normal"
    elif result > 25.9 and result < 27.3:
        print(f'Seu BMI = {result:.2f}')
        return "Entre 25.9 e 27.3: Pouco acima do peso"
    elif result > 27.4 and result < 32.3:
        print(f'Seu BMI = {result:.2f}')
        return "Entre 27.4 e 32.3: Acima do peso"
    else:
        print(f'Seu BMI = {result:.2f}')
        return "Acima de 32.4: Obesidade"
    

print(bmiCalculator(weight, height))
