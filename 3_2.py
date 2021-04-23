def person_data(name, surname, birth_year, residence_place, e_mail, phone_number):
    """Функция запрашивает персональные данные и выводит их одной строкой
    """
    print(' '.join(['Имя:', name, ', фамилия:', surname, ', год рождения:', birth_year, ', место жительства:', residence_place, ', e-mail:', e_mail, ', тел.:', phone_number]))
person_data(name=input('Введите Ваши данные.\nИмя: '), surname=input('Фамилия: '), birth_year = input('Год рождения: '), residence_place = input('Место проживания: '), e_mail = input('Электронный адрес: '), phone_number = input('Номер телефона: '))