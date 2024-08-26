Done = True
hot = 0
ice = 0
frappe = 0



while Done:
    print("*" * 20)
    print("\tDrinks menu")
    print("*" * 20)
    print("| 0. Quit")
    print("| 1. Hot Coffee")
    print("| 2. Ice Coffee")
    print("| 3. Frappe Coffee")
    print("| 4. Caculate Cost")


    select = int(input("Select Item : "))

    if select == 1:
        hot = int(input("Hot coffee, How many glasses : "))
    
    if select == 2:
        ice = int(input("ice coffee, How many glasses : "))
    
    if select == 3:
        frappe = int(input("Frappe coffee, How many glasses : "))
    
    if select == 4:

        h = hot * 30
        i = ice * 40
        f = frappe * 50

        if hot > 0:
            print(f"Hot coffee 30 {h}")
            
        if ice > 1:
            print(f"ice coffee 30 {i}")

        if frappe > 1:
            print(f"frappe coffee 30 {f}")

            


    

        
        
        
    



