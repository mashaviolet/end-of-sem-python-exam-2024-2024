def user_age():
    age = int(input('Enter your age :'))
    if age >= 18:
        print('You are Eligible')
    else:
        print('you are not eligible')
user_age()        
def grade_students():
    student_mark = int(input('Enter student mark :'))
    if  student_mark >= 90:
        print('A') 
    elif 80 <= student_mark < 89:
        print('B') 
    elif 70 <= student_mark < 79:
        print('C') 
    elif 60 <= student_mark < 69:
        print('D') 
    elif student_mark < 60:
        print('F')
    
grade_students()
# iv 
def grade_students():

    student_mark = int(input('Enter student mark :'))
    if student_mark == str:
        print ('Invalid Input')
    else:
        print(student_mark)
    if  student_mark >= 90:
        print('A') 
    elif 80 <= student_mark < 89:
        print('B') 
    elif 70 <= student_mark < 79:
        print('C') 
    elif 60 <= student_mark < 69:
        print('D') 
    elif student_mark < 60:
        print('F')
    
    # v)
grade_students()
def grade_students():

    student_mark = int(input('Enter student mark :'))
    if  student_mark >= 90:
        print('A, Excellent grades') 
    elif 80 <= student_mark < 89:
        print('B, Excellent') 
    elif 70 <= student_mark < 79:
        print('C , Good') 
    elif 60 <= student_mark < 69:
        print('D Satisfactorry') 
    elif student_mark < 60:
        print('F, Needs Improvement')
    
    
grade_students()
