print("########### Wellcome To My CGPA Calculator ############")
print("\n 1.Press 1 to Calculate with Cource \n 2.Press 2 to Clculate With Semester")

print("Enter you chosse:")
chosse=int(input())
if(chosse==1):
    print("Enter The Previous Credit Earned: ")
    previous_credit_earned=float(input())
    print("Enter The Previous CGPA: ")
    previous_cgpa=float(input())

    credit_list=[]
    review_list=[]
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
             review_list.append(credit_list[i])
             
    
    sumation_of_earned_credit=sum(credit_list)-sum(review_list)
    gpa=sum_of_credit_and_grade/sumation_of_earned_credit
    print("Course Name \t Credit Hours \t Letter Grade \t Grade Point")
    for i in range(0,total):
         print("Course_{}\t\t{}\t\t{}\t\t{}".format(i+1,credit_list[i],letter_grade[i],grade_point[i]))
    
    print("\n\t\t\t\t\t\t\tGPA: {:0.2f}".format(gpa))
    print("Registered Credit Hours in this Semester: {}".format(sum(credit_list)))
    print("Credit Hours Earned in this Semester: {}".format(sumation_of_earned_credit))
    print("Total Credit Hours Earned: {}".format(previous_credit_earned+sumation_of_earned_credit))
    cgpa=(((previous_cgpa*previous_credit_earned)+(sumation_of_earned_credit*gpa))/(previous_credit_earned+sumation_of_earned_credit))
    print("CGPA: {:0.2f}".format(cgpa))



elif(chosse==2):
      credit_earned=[]
      grade_earned=[]
      sum_of_gpa=0
      print("Enter Total Semester Number")
      total=int(input())
      for i in range(0,total):
           print("Enter Your Semester_{} Credit and Grade".format(i+1))
           credit_earned.append(float(input()))
           grade_earned.append(float(input()))
           sum_of_gpa= sum_of_gpa + credit_earned[i]*grade_earned[i]
     

      print("Toral Semester: {}".format(total))
      print("Total Credit: {}".format(sum(credit_earned)))
      print("Total Grade: {:0.2f}".format(sum(grade_earned)))
      print("CGPA {:0.2f}".format(sum_of_gpa/sum(credit_earned)))









    






        





    