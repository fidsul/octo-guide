while True:
    num_1 = input("Skriv inn et tall:")
    symbol = input("Skriv inn et symbol")
    num_2 = input("Skriv inn et ftall:")

    print(f"{num_1} + {symbol} + {num_2} = {eval(num_1 + symbol +num_2)}"  )