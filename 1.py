def print_thai_flag():

    RED = '\033[41m'    
    WHITE = '\033[37m'  
    BLUE = '\033[44m'   
    RESET = '\033[0m'    
    
    width = 40
    stripe_height = 2
    blue_height = 4  
    
    for _ in range(stripe_height):
        print(RED + ' ' * width + RESET)
    
    for _ in range(stripe_height):
        print(WHITE + ' ' * width + RESET)
    
    for _ in range(blue_height):
        print(BLUE + ' ' * width + RESET)
    
    for _ in range(stripe_height):
        print(WHITE + ' ' * width + RESET)
    
    for _ in range(stripe_height):
        print(RED + ' ' * width + RESET)

print("Таиланд:")
print_thai_flag()