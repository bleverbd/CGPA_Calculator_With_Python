print("########### Wellcome To My CGPA Calculator ############")
print("\n 1.Press 1 to Calculate with Cource \n 2.Press 2 to Clculate With Semester")

print("Enter you chosse:")
chosse=int(input())
if(chosse==1):
    credit_list=[]
    number_list=[]
    letter_grade=[]
    grade_point=[]
    sum_of_credit_and_grade=0.0

    print("Enter Total Course Number")
    total=int(input())
    for i in range(0,total):
        print("Enter Your Course_{} Credit and Number".format(i+1))
        credit_list.append(float(input()))
        number_list.append(float(input()))
        if(number_list[i]>=80.0 and number_list[i]<=100.0):
             letter_grade.append("A Plus")
             grade_point.append(4.0)
             sum_of_credit_and_grade=sum_of_credit_and_grade+credit_list[i]*grade_point[i]

        elif(number_list[i]>=75.0 and number_list[i]<80.0):
             letter_grade.append("A Regular")
             grade_point.append(3.75)
             sum_of_credit_and_grade=sum_of_credit_and_grade+credit_list[i]*grade_point[i]
        elif(number_list[i]>=70.0 and number_list[i]<75.0):
             letter_grade.append("A Minus")
             grade_point.append(3.50)
             sum_of_credit_and_grade=sum_of_credit_and_grade+credit_list[i]*grade_point[i]
        elif(number_list[i]>=65.0 and number_list[i]<70.0):
             letter_grade.append("B Plus")
             grade_point.append(3.25)
             sum_of_credit_and_grade=sum_of_credit_and_grade+credit_list[i]*grade_point[i]
        elif(number_list[i]>=60.0 and number_list[i]<65.0):
             letter_grade.append("B Regular")
             grade_point.append(3.00)
             sum_of_credit_and_grade=sum_of_credit_and_grade+credit_list[i]*grade_point[i]
        elif(number_list[i]>=55.0 and number_list[i]<60.0):
             letter_grade.append("B Minus")
             grade_point.append(2.75)
             sum_of_credit_and_grade=sum_of_credit_and_grade+credit_list[i]*grade_point[i]
        elif(number_list[i]>=50.0 and number_list[i]<55.0):
             letter_grade.append("C Plus")
             grade_point.append(2.50)
             sum_of_credit_and_grade=sum_of_credit_and_grade+credit_list[i]*grade_point[i]
        elif(number_list[i]>=45.0 and number_list[i]<50.0):
             letter_grade.append("C Regular")
             grade_point.append(2.25)
             sum_of_credit_and_grade=sum_of_credit_and_grade+credit_list[i]*grade_point[i]
        elif(number_list[i]>=40.0 and number_list[i]<45.0):
             letter_grade.append("D")
             grade_point.append(2.00)
             sum_of_credit_and_grade=sum_of_credit_and_grade+credit_list[i]*grade_point[i]
        elif(number_list[i]<40.0):
             letter_grade.append("F")
             grade_point.append(0.00)
             sum_of_credit_and_grade=sum_of_credit_and_grade+credit_list[i]*grade_point[i]
    
    sumation_of_credit=sum(credit_list)
    gpa=sum_of_credit_and_grade/sumation_of_credit
    print("Course Name \t Credit Hours \t Letter Grade \t Grade Point")
    for i in range(0,total):
         print("Course_{}\t\t{}\t\t{}\t\t{}".format(i+1,credit_list[i],letter_grade[i],grade_point[i]))
    
    print("\n\t\t\t\t\t\t\tGPA:{}".format(gpa))




        





    