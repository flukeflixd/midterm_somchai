Done = True

while Done:
    select_choice = int(input("Select choice : "))
    if select_choice == 0:
        print("Exit Program")
        Done = False
    if select_choice == 1:
        car_price = float(input("Enter car price : "))
    if select_choice == 2:
        down_payment = float(input("Enter down payment (%)"))
    if select_choice == 3:
        interest_per = float(input("Enter interest (%) per  year : "))
    if select_choice == 4:
        enter_month = float(input("Enter month : "))
    if select_choice == 5:
        #เงินดาวน์
        down = car_price  * (down_payment/100) 
        #ไฟแนนซ์
        finance = car_price - down
        #อัตตราดอกเบี้ย
        interest_rate = interest_per / 12
        #ดอกเบี้ยจัดไฟแนนซ์
        interest_amouth = finance * (interest_rate/100) * enter_month
        #จำนวนเงินต้องจ่าย
        net = finance + interest_amouth
        #จำนวนเงินต่อเดือน
        installment = car_price / enter_month

        print(f"Price car : {car_price:.2f}")
        print(f"Amount down payment(15.00%) : {down:.2f} ")
        print(f"Amount finance : {finance:.2f}")
        print(f"Amount interest(2.40%) : {interest_amouth:.2f}")
        print(f"Amount net finance : {net:.2f} ")
        print(f"Amount installment(per month) : {installment:.2f}")
    if select_choice == 6:
        car_price,down_payment,interest_per,enter_month = 0
    
        


    

