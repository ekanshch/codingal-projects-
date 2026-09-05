while True:
    try:
        name = input("Enter Customer Name: ")
        tickets = int(input("Enter Number of Tickets: "))
        price = float(input("Enter Price of Ticket: "))

        if tickets <= 0:
            raise Exception("Tickets must be greater than zero.")
        if tickets > 10:
            raise Exception("You cannot book more than 10 tickets.")
        if price <= 0:
            raise Exception("Ticket price must be greater than zero.")

    except ValueError:
        print("Please enter numbers only!")

    except Exception as e:
        print("Error:", e)

    else:
        total = tickets * price
        print("=======BOOKING CONFIRMED=======")
        print(f"Customer Name: {name}")
        print(f"Number of Tickets: {tickets}")
        print(f"Ticket Price: ${price}")
        print(f"Total Amount: ${total}")
        break

    finally:
        print("Thank you for visiting our cinema!!")

        