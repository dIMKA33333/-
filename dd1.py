import datetime
import datetime
result=""
city_codes = {}
with (open('Roman.csv', mode='r', encoding='utf-8') as f):
    for row in f.readlines():
        city_codes[row[0]] = row[1]
        data = {}
        while True:
            print(" Добавтье данные")
            print(" Посмотреть информацию")
            print(" Выход")

            choice = input("Выбирите опцию:")
            if choice == '1':
                last_name = input("Введите фамилию(заглавные буквы):").upper()
                first_name = input("Введите имя(заглавными буквами):").upper()
                gender = input("Введите пол( 'm' для мужского, 'f' для женского):")
                date_of_birth = input("Введите дату рождения в формате YYYY-MM-DD:")
                parsed_date = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
                resident = input("Является ли ризидентом(да/нет):").strip().lower() == 'да'
                city_code_input = input("Введите код города(заглавные  буквы):").upper()
                city_code = city_codes.get(city_code_input, None)
                if city_code is None:
                    print("Код города не найден.")
                    continue
                year_of_birth = parsed_date.year
                month_of_birth = parsed_date.month
                day_of_birth = parsed_date.day
                if gender == 'm':
                    result=result+'1'
                elif gender == 'm':
                    first_digit = '2'
                else:
                    first_digit = '2' if day_of_birth[6:10] < '2000' else '6'

                cnp = first_digit + year_of_birth + month_of_birth + day_of_birth + city_code + (
                    '1' if gender == 'm' else '2')
                ascii_code = str(ord(last_name[0]))
                if len(ascii_code) < 2:
                    ascii_code = '0' + ascii_code
                    cnp += ascii_code
                    myltipliers = '279146358279'
                    total = sum(int(result[i]) * int(myltipliers[i] for i in range(12))
                    check_digit = total % 9
                    cnp += str(check_digit)
                    data[result] = {
                        "Имя": first_name,
                        "Фамилия": last_name,
                        "Пол": gender,
                        "Дата рождения": parsed_date.year,
                        "Резидент": resident,
                        "Город": city_code_input
                    }

                   print("f.CNP: {cnp_key}),Информация: {info}")
