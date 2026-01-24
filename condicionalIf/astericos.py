for x in range(7):
    for y in range(6):
        if (y < 1 or y > 6):
            print("* ", end="")
        elif x == 0 or x == 6:
            print("* ", end="")
        elif x == 3 and y == 3:
            print("* ", end="")
        else:
            print("  ", end="")
    print("*")
