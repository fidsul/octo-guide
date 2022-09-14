while True:
    ms = input("skriv in hvor mange meter per sekund:")
    try:
        km = (eval(ms) *3.6)

        print(f"{ms}m/s ={km}km/t")
    except NameError:
        print(f"{ms} er ikke et tall")