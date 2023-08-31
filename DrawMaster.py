import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates
import matplotlib as matplotlib
import pandas

# анализ данных и рисование графиков
class DrawMaster:
    # формирование данных для графика
    def DrawGrahs(self, grahName, linesNames, *values_list):
        counter = 0

        for values in values_list:
            list_date = []
            list_value = []
            for i in values:
                list_date.append(i.Date)
                list_value.append(i.Value)

            # Формирование данных для графика
            data = {'Курс': list_value}
            df = pandas.DataFrame(data)
            x = matplotlib.dates.date2num(pandas.to_datetime(list_date, format='%d/%m/%Y'))

            # Инициализация графика
            pyplot.plot(x, df, label=linesNames[counter])

            # Формат для дат
            pyplot.gcf().autofmt_xdate()
            Format = mdates.DateFormatter('%Y-%m-%d')
            pyplot.gca().xaxis.set_major_formatter(Format)

            counter += 1

        pyplot.xlabel("Дата")
        pyplot.ylabel("Курс EUR")
        pyplot.title(grahName)
        pyplot.legend()

        pyplot.savefig("graph.png")
        pyplot.show()