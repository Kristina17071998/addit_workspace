def Artek():
    while True:
        # Считываем фамилии студентов и их оценки
        students_input = input("Введите фамилии студентов и их оценки через запятую (например, Иванов 5, Петров 4): ")

        # Считываем количество свободных мест
        available_seats = int(input("Введите количество свободных мест: "))

        # Разбиваем строку на пары "фамилия оценка"
        students = [student.split() for student in students_input.split(', ')]

        # Проверяем формат фамилий (первая буква заглавная, остальные строчные)
        correct_format = all(student[0][0].isupper() and student[0][1:].islower() for student in students)

        if correct_format:
            break
        else:
            print("Ошибка! Фамилии должны быть в правильном формате (например, Иванов). Пожалуйста, повторите ввод.\n")

    # Создаем список тех, кто имеет оценку 5
    top_students = [student[0] for student in students if student[1] == '5']

    # Если количество отличников больше, чем свободных мест, сортируем и выводим их
    if len(top_students) > available_seats:
        top_students.sort()
        print ('')
        print('Отличники, которые поедут в Артек:')
        print(', '.join(top_students[:available_seats]))
    else:
        print("Все отличники едут в Артек:")
        print(', '.join(top_students))

# Пример использования
Artek()
