lang = input("What is your frov language")

match lang:
    case "JavaScript":
        print("You become JS Developer")
    case "Python":
        print("You become Python Django Developer")
    case "PHP":
        print("yOU BECOME  Web Developer")
    case _:
        print("Please learn one language")