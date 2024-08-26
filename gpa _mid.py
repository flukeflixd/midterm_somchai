total = 0
display = ''
total_credit  = 0
print("Input Data:")
for i in range(1,6+1):
    enter_score = int(input(f"Enter  score of subject #{i} : "))
    enter_credit = int(input(f"Enter credit of subject #{i} : "))

    if 80 <= enter_score <= 100: 
        grade = "A"
        point = enter_credit * 4
    elif 70 <= enter_score <= 79:
        grade = "B"
        point = enter_credit * 3
    elif 60 <= enter_score <= 69:
        grade = "C"
        point = enter_credit * 2
    elif 50 <= enter_score <= 59:
        grade = "D"
        point = enter_credit * 1
    else: 
        0 <= enter_score <= 49
        grade = "F"
        point = enter_credit * 0

    total += point
    total_credit += enter_credit

    display += f"|  {i} | \t{enter_score:.2f} \t| {grade} \t| {enter_credit} \t| {point:.2f} |\n"

print("\tReport Grade")
print("="*40)
print("| No. |   Mark | Grade | Credit | Points |")
print("="*40)
print(display)
print("="*40)
print(f"|\t Total |{total_credit:.1f}\t |{total:.1f}\|")
print("="*40)
    
           
    
        
    
