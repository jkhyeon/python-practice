"""
students= ['고 상 호', '양 서 연','이 승 훈','이 원 희']
print(students)
print(students[0])
print(students[1:4])
print(students[:])
print(students[:2])
print(students[1:])


#print(dir(list))
#dir은 method를 보고싶을때 쓴다
a = ['eat', 'please', 'spam']
a.append('please')
print(a)


#print(dir(tuple))
tuple_ex = (1, 2)
tuple_ex = 1, 2
#print(type(tuple_ex))
a = (1,)
print(type(a))


tuple_ex = 1, 2, 3
tuple_ex[1]= 2
print(tuple_ex)
#tuple은 변하지 않는 자료값

"""

print(list(range(5)))
print(list(range(5, 8)))
print(list(range(1, 10, 2)))
