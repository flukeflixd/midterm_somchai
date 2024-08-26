import random
display = ''
Done = True

while Done:
    print("="*30)
    print("\tMain Menu")
    print("="*30)
    print("1. Input number of subject (8)")
    print("2. Start Random Grade")
    print("3. Exit Program")
    print("="*30)

    select = int(input("Select your Choice : "))
    
    if select == 3:
        print("Exit Program .... ")
    
    if select == 1:
        enter_number = int(input("Enter your number of subject : "))
        print("Press any key to continue . . . ")

    if select == 2:
        print("Start Random Score&Grade . . . . ")
        print("="*30)
        for i in range(enter_number+1):
            score_random = random.randint(40,100)
           # print(score_random)
            if score_random >= 80 and score_random <= 100:
                grade = 'A'
            elif score_random >= 70 and score_random <= 79:
                grade = 'B'
            elif score_random >= 60 and score_random <= 69:
                grade = 'C'
            elif score_random >= 50 and score_random <= 59:
                grade = 'D'
            else:
                score_random >= 40 and score_random <= 49
                grade = 'F'
            
            print(f"Your #{i} subject is {grade}")

            
            

                
            

            

            
            
            
    
        
        





        
    