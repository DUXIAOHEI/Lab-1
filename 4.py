import os

def read_sequence(filename):
    with open(filename, 'r') as file:
        numbers = [float(line.strip()) for line in file if line.strip()]
    return numbers

def analyze_numbers(numbers):
    greater_than_5 = 0
    less_than_5 = 0
    
    for num in numbers:
        if num >= 0:  
            if num > 5:
                greater_than_5 += 1
            elif num < 5:
                less_than_5 += 1
    
    total = greater_than_5 + less_than_5
    
    if total == 0:
        return 0, 0
    
    percent_greater = (greater_than_5 / total) * 100
    percent_less = (less_than_5 / total) * 100
    
    return percent_greater, percent_less

def create_diagram(percent_greater, percent_less, width=50):
    """创建百分比图"""
    diagram = []
    diagram.append("=" * 60)
    diagram.append("        ДИАГРАММА ПРОЦЕНТНОГО СООТНОШЕНИЯ")
    diagram.append("=" * 60)
    diagram.append("")
    diagram.append("Условие: Числа больше 5 и меньше 5, отрицательные отбросить")
    diagram.append("")
    
    bar_greater = "█" * int((percent_greater / 100) * width)
    diagram.append(f"Числа > 5: [{bar_greater:<{width}}] {percent_greater:.1f}%")
    
    bar_less = "█" * int((percent_less / 100) * width)
    diagram.append(f"Числа < 5: [{bar_less:<{width}}] {percent_less:.1f}%")
    
    diagram.append("")
    diagram.append(f"Всего чисел (без отрицательных и равных 5): {int(percent_greater + percent_less)}")
    diagram.append("=" * 60)
    
    return "\n".join(diagram)

def create_animated_diagram(numbers):
    percent_greater, percent_less = analyze_numbers(numbers)
    
    frames = []
    
    frame1 = ["=" * 60]
    frame1.append("        ДИАГРАММА ПРОЦЕНТНОГО СООТНОШЕНИЯ")
    frame1.append("=" * 60)
    frame1.append("")
    frame1.append("Загрузка данных...")
    frames.append("\n".join(frame1))
    
    frame2 = ["=" * 60]
    frame2.append("        ДИАГРАММА ПРОЦЕНТНОГО СООТНОШЕНИЯ")
    frame2.append("=" * 60)
    frame2.append("")
    frame2.append("Условие: Числа больше 5 и меньше 5, отрицательные отбросить")
    frame2.append("")
    frame2.append("Анализ данных...")
    frames.append("\n".join(frame2))
    
    frames.append(create_diagram(percent_greater, percent_less))
    
    return frames

def main():
    try:
        numbers = read_sequence('sequence.txt')
        print(f"Прочитано {len(numbers)} чисел из файла sequence.txt")
        
        percent_greater, percent_less = analyze_numbers(numbers)
        
        frames = create_animated_diagram(numbers)
        
        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')  
            print(frame)
            input("\nНажмите Enter для продолжения...")
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(create_diagram(percent_greater, percent_less))
        
        print("\nДЕТАЛЬНАЯ СТАТИСТИКА:")
        print("-" * 40)
        
        greater_count = 0
        less_count = 0
        negative_count = 0
        equal_5_count = 0
        
        for num in numbers:
            if num < 0:
                negative_count += 1
            elif num > 5:
                greater_count += 1
            elif num < 5:
                less_count += 1
            else:  # num == 5
                equal_5_count += 1
        
        print(f"Всего чисел в файле: {len(numbers)}")
        print(f"Чисел > 5: {greater_count}")
        print(f"Чисел < 5: {less_count}")
        print(f"Отрицательных чисел (отброшено): {negative_count}")
        print(f"Чисел равных 5 (отброшено): {equal_5_count}")
        
    except FileNotFoundError:
        print("Ошибка: Файл sequence.txt не найден!")
        print("Создаем тестовые данные для демонстрации...")
        
        import random
        test_numbers = [random.uniform(-10, 15) for _ in range(250)]
        
        with open('sequence.txt', 'w') as f:
            for num in test_numbers:
                f.write(f"{num}\n")
        
        print("Тестовые данные созданы в файле sequence.txt")
        print("Запустите программу снова.")

if __name__ == "__main__":
    main()