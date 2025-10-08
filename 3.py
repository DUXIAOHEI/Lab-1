def draw_function_graph():
    blue = "\u001b[44m"
    reset = "\u001b[0m"
    
    height = 9  
    width = 20
    
    graph = [[' ' for _ in range(width)] for _ in range(height)]
    
    for i in range(height):
        graph[i][width//2] = '|' 
    for j in range(width):
        graph[height-1][j] = '-' 
    graph[height-1][width//2] = '+' 
    
    for j in range(1, width):
        if j == width//2:
            continue  
            
        x = (j - width//2) / 2.0  
        if x <= 0:
            continue  
            
        y = 1 / x  
        
        i = height - 1 - int(y * 2) 
        
        if 0 <= i < height-1:  
            graph[i][j] = '*'
    
    for i in range(height):
        line = ""
        for j in range(width):
            if graph[i][j] == '*':
                line += blue + graph[i][j] + reset
            else:
                line += graph[i][j]
        print(line)
    
    print("\n")


draw_function_graph()