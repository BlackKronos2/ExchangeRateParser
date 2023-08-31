from ProgramBasis import ProgramBasis

# Запуск программы
if __name__ == '__main__':
    yandexToken = 'Your Token'
    program = ProgramBasis(yandexToken)
    while True:
        print('+' * 60)
        print('1.Актуальный курс.\n2.Конвертировать.\n3.Данные за период.\n4.Прогноз курса на основе данных за 10 дней.\n5.Выход из программы.\n')
        ch = input()
        if ch == '5':
            break
        if ch == '1':
            program.GetActualRate()
        elif ch == '2':
            program.ConvertValute()
        elif ch == '3':
            program.Statistic()
        elif ch == '4':
            program.Prognosis()

