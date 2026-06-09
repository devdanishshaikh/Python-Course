original_salary = float(input("Enter your salary :"))

if original_salary >=50000 :
  bonus = (20/100)*original_salary
  final_salary =original_salary + bonus

elif original_salary >=30000 and original_salary < 50000 :
  bonus = (10/100)*original_salary
  final_salary =original_salary + bonus

else :
   bonus = (5/100)*original_salary
   final_salary =original_salary + bonus

final_salary =original_salary + bonus

print("Original Salary :",original_salary)

print("Bonus           :",bonus)

print("Final Salary    :",final_salary)
