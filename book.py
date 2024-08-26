
total = 0
output = ""
while True:
    book = int(input("How many book you want to buy : "))
    for n in range(book):
        price_book = float(input(f"Price Book number {n+1} : "))
        output = output + f"Your book {n+1} Price is {price_book:.2f} \n"
        total += price_book
    if book >= 3 and total >= 2500:
        print(f"\nYour Order,Congrat you get discount for 15%")
        print()
        print(output)
        print(f"Your Book total is : { (total * 0.15) : .2f}")
    else:
        print(f"Your order")
        print(output)
        print(f"Your Book total is : {total:.2f}")
    choice = input("You want to buy book again? Y / N :")
    if choice == "N" or choice == "n":
        print("Exit Program . . .")
    total = 0
    output = ""



