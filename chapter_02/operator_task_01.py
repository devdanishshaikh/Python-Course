std_name = input("Enter Your name                          :")
std_roll = input("Enter Your Roll No                       :")
sub_1 = int(input("Enter marks of English                  :"))
sub_2 = int(input("Enter marks of Programing               :"))
sub_3 = int(input("Enter marks of Compter Network          :"))
sub_4 = int(input("Enter marks of Artificial Intellefgince :"))
sub_5 = int(input("Enter marks of Applied calculus         :"))

Total_marks = 500
obt_marks   = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
percentage  = round((obt_marks/Total_marks)*100,2)

if percentage >= 80 and percentage <= 100:
  grade = "A"
elif percentage >= 70 and percentage < 80:
  grade = "B"
elif percentage >= 60 and percentage < 70:
  grade = "C"
else :
  grade ="Fail"

print("======================Student Result============================")
print("Name            :",std_name)
print("Student Roll    :",std_roll)
print("Total Marks     :",Total_marks)
print("Obtained Marks  :",obt_marks)
print("Percentage      :",percentage," % ")
print("Grade :",grade)
print("================================================================")
