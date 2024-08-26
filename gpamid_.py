display = ''
credit = 3
total = 0
for i in range(1,5+1):
    subject_name = input(f"Enter subject name {i} ")
    subject_score = int(input(f"Enter subject score {i} "))
    


    if 80 <= subject_score <= 100 :
        grade = 'A'
        point = 4.0 * credit
    elif 70 <= subject_score <= 79:
        grade = 'B'
        point = 3.0 * credit
    elif 60 <= subject_score <= 69:
        grade = 'C'
        point = 2.0 * credit
    elif 50 <= subject_score <= 59:
        grade = 'D'
        point = 1.0 * credit
    else: 
        40 <= subject_score <= 49
        grade = 'F'
        point = 0.0 * credit

    allcredit =  credit * 5
    total += point
    
    display += f"{i} {subject_name} {subject_score} {grade} {point}\n"


avg = total / allcredit
print(f"\tGrade Point Average(GPA) Report")
print("="*30)
print("No.  Subject Name\tMark Grade Point")
print("="*30)
print(display)
print("="*30)
print(f"Total Point : {total:.1f}")
print(f"Total Credit : {credit:.1f}")
print(f"Grade Point Average(GPA) : {avg:.2f}")


