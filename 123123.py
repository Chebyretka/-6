def count_digits(n):
    if n < 1:
        return 0
    digits = 0
    if n >= 1:
        digits += min(n, 9)
    if n >= 10:
        digits += 2 * min(n - 9, 90)
    if n >= 100:
        digits += 3 * min(n - 99, 900)
    if n >= 1000:
        digits += 4 * (n - 999)
    return digits

def find_pages_by_digits(total_digits):
    if total_digits < 1:
        return 0
    if total_digits <= 9:
        return total_digits
    if total_digits <= 9 + 2*90:
        return 9 + (total_digits - 9) // 2
    if total_digits <= 9 + 2*90 + 3*900:
        remaining = total_digits - 9 - 2*90
        return 99 + remaining // 3
    remaining = total_digits - 9 - 2*90 - 3*900
    return 999 + remaining // 4

def main():
    print("Программа для расчета нумерации страниц книги")
    while True:
        print("\nВыберите действие:")
        print("1. Рассчитать количество цифр для заданного количества страниц")
        print("2. Определить количество страниц по количеству цифр")
        print("3. Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == '1':
            try:
                pages = int(input("Введите количество страниц: "))
                if pages < 1:
                    print("Количество страниц должно быть положительным числом")
                    continue
                digits = count_digits(pages)
                print(f"Для {pages} страниц потребуется {digits} цифр")
            except ValueError:
                print("Ошибка: введите целое число")
                
        elif choice == '2':
            try:
                digits = int(input("Введите количество цифр: "))
                if digits < 1:
                    print("Количество цифр должно быть положительным числом")
                    continue
                pages = find_pages_by_digits(digits)
                print(f"При {digits} цифрах в книге {pages} страниц")
            except ValueError:
                print("Ошибка: введите целое число")
                
        elif choice == '3':
            print("До свидания!")
            break
            
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
