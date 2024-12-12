# i)   
def circle_area(pie,r):
    area=pie*r**2
    print(f'The area of a cicle with radius {r}  is {area}')
circle_area(3.14,4) 



# ii)
integers = [4,7,2,9,12,15]
odd_sum =0
for num in integers:
    if  num % 2 != 0:
     print (num)
    odd_sum+=num
    print(odd_sum)

    #iii
num_one = int (input('Enterfirst number :')) 
num_two = int(input('Enter second number'))
sum = num_one + num_two
difference = num_one - num_two
product = num_one*num_two
quotient = num_two // num_two
print(sum,difference,product,quotient)

    # iv
student_info = {
    'name': 'Alice','age':'20','grade':'A'
}
student_info.update('age',26)
print(student_info)
student_info["city"] = "Kampala"
print(student_info)



