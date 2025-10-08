def draw_pattern_ren():
    blue = "\u001b[44m"
    reset = "\u001b[0m"
    width = 21
    height = 4
    
    for i in range(height):
        if i == 0:
            print(reset + " " * ((width - 3) // 2) + blue + " " * 3 + reset)
        elif i == 1:
            print(reset + " " * ((width - 5) // 2) + blue + " " * 5 + reset)
        elif i == 2:
            print(reset + " " * ((width - 7) // 2) + blue + " " * 7 + reset)
        elif i == 3:
            print(blue + " " * 9 + reset + " " * 3 + blue + " " * 9 + reset)
        elif i == 4:
            print(reset + " " * 2 + blue + " " * 5 + reset + " " * 7 + blue + " " * 5 + reset + " " * 2)
    print("\n")


draw_pattern_ren()