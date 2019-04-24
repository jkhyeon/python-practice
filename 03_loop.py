"""
n = 0
while n < 5:
    print('저의 꿈은 한량입니다')
    n= n + 1

이렇게 끝을 설정해주지 않으면 계속 반복된다
foods = ['pizza', 'pasta']

for food in foods:
    print(food)
    


numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    number1= number * 2
    print(number*2, end = ' ,')
"""
    
numbers = [1, 2, 3, 4, 5, 6]

new_numbers = []

for number in numbers:
    new_numbers.append(number*2)
print(new_numbers)
