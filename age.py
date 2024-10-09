def within_range(num: int, min: int, max: int, ) -> bool:
    return (min < number and number <= max)


def give_message() -> None:
    state: str = ""

    if 0 < number and number <= 99:
        if number < 25:
            state = "Young"
        elif number < 50:
            state = "Adult"
        elif number < 75:
            state = "Elderly"
        elif number <= 99:
            state = "Ghost"

    print(state)

    match state:
        case "Young":
            print("Lucky")
        case "Adult":
            print("♥")
        case "Elderly":
            print("Legend")
        case "Ghost":
            print("Fart")
        case _:
            pass


while (True):
    age = input("How old are you?")
# Check if valid number
    try:
        number = int(age)
    except ValueError as err:
        print("How old are you?")
        continue
# Check if input is between 0 and 99
    valid: bool = within_range(number, 0, 99)
    if not valid:
        print("You gave wrong number (0-99)")
        continue

    give_message(number)
    break
