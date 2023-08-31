from LoaderMaster import LoaderMaster
from DrawMaster import DrawMaster
from YandexDiskMaster import YandexDiskMaster
from Prognosis import Prognosis

# Запуск элементов программы
class ProgramBasis:
    def __init__(self, yandexToken):
        self.YaToken = yandexToken

    #Ввод даты пользователем
    def __dateInput(self):
        print('+' * 60)
        year = input('Введите год: ')
        month = input('Введите месяц: ')
        day = input('Введите день: ')

        if int(day) < 10:
            day = '0' + day
        if int(month) < 10:
            month = '0' + month

        date = f'{day}/{month}/{year}'
        print(f'Введена дата: {date}')
        return date

    # Актуальный курс валюты
    def GetActualRate(self):
        print('+' * 60)
        value = LoaderMaster().loadActual()
        rateValue = float('{:.2f}'.format(value.Value))
        print(f'Актуальный курс {rateValue} на {value.Date}')
        i = input('Введите любую строку чтобы продолжить...\n')

    # Конвертировать в рубли и обратно
    def ConvertValute(self):
        print('+' * 60)
        i = input('1.Конвертировать EUR/RUB\n2.Конвертировать RUB/EUR\n')
        if i != '1' and i != '2':
            return
        value = LoaderMaster().loadActual()
        rateValue = float('{:.2f}'.format(value.Value))

        valuteCount = input('Введите единицы: ')

        if i == '1':
            valuteCount = float(valuteCount) * rateValue
        else:
            valuteCount = float(valuteCount) / rateValue

        valuteCount = float('{:.2f}'.format(valuteCount))

        print(f'Вывод {valuteCount}')
        i = input('Введите любую строку чтобы продолжить...\n')

    def Statistic(self):
        print('+' * 60)

        # Ввод дат
        try:
            print('Введите 1 дату')
            date1 = self.__dateInput()
            print('+' * 60)
            print('Введите 2 дату')
            date2 = self.__dateInput()
        except:
            print('Ошибка ввода - некорректные данные')
            return

        # Получение информации
        values = LoaderMaster().loadPeriod(date1,date2)

        if len(values) == 0:
            print('На сайте нет данных на этот период')
            return

        for i in values:
            print(f'{i.Date} - {i.Value}')

        # Вывод графика
        DrawMaster().DrawGrahs('Изменения курса EUR',['Курс EUR'], values)

        choise = input('Сохранить график на диске? [Y]\n')
        if choise == 'y' or choise == 'Y':
            try:
                loader = YandexDiskMaster(self.YaToken)
                loader.SendFile("graph.png", ".png")
                print("Данные успешно отправлены")
            except:
                print("Ошибка отправки")

        choise = input('Введите любую строку чтобы продолжить...\n')

    # Прогноз о курсе, на основе 10 последних дней
    def Prognosis(self):
        print('+' * 30)
        print('Идёт прогноз...')

        analys = Prognosis()
        result = analys.DoAnalysis()
        print(f'Результат анализа: {result}')

        choise = input('Сохранить график на диске? [Y]\n')
        if choise == 'y' or choise == 'Y':
            try:
                loader = YandexDiskMaster(self.YaToken)
                loader.SendFile("graph.png", ".png")
                print("Данные успешно отправлены")
            except:
                print("Ошибка отправки")

        choise = input('Введите любую строку чтобы продолжить...\n')