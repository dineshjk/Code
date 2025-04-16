    """Explaining input()"""

    print("\033c", end="")  # Clears the screen
    city = input("Enter the destination a city: ")
    dist = int(input("Enter the distance in kilometers: ")) #Must enter int.
    rate = float(input("Enter the fare per kilometer: "))
    price = dist * rate
    print(
        f"The fare @ \u20b9 {rate}/km for dist {dist} from here to"
        f" {city} is \u20b9 {price:.2f}."
    )
