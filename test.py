def print_framed_text(*lines):
    # Знаходимо найширший рядок
    max_len = max(len(line) for line in lines)
    
    # Створюємо верхню рамку
    border = '"""' + '"' * (max_len + 2) + '"""'
    print(border)
    
    # Виводимо кожен рядок з боковими рамками
    for line in lines:
        padded_line = line + ' ' * (max_len - len(line))  # додаємо пробіли для вирівнювання
        print(f'""" {padded_line} """')
    
    # Нижня рамка
    print(border)
print_framed_text("teqy","jgrdj","fdsjgrejswh")
input()