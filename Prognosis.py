from datetime import datetime, timedelta
from LoaderMaster import LoaderMaster
from LoaderMaster import Valute
from DrawMaster import DrawMaster

# Прогноз курса на основе информации за последние 30 дней
class Prognosis:
    period = 2
    length = 10

    # Построение SMA
    def __init__(self):
        index = 0
        sum = 0
        SMAindex = 0

        date1 = datetime.now()
        date2 = date1

        # Инфомация за последние 10 дней
        counter = 9
        while counter > 0:
            date2 = date2 - timedelta(days=1)

            date2Test = date2.strftime("%d") + "/" + date2.strftime("%m") + "/" + str(int(date2.strftime("%Y")))
            values = LoaderMaster().loadPeriod(date2Test, date2Test)
            if len(values) != 0:
                counter -= 1

        date1 = date1.strftime("%d") + "/" + date1.strftime("%m") + "/" + str(int(date1.strftime("%Y")))
        date2 = date2.strftime("%d") + "/" + date2.strftime("%m") + "/" + str(int(date2.strftime("%Y")))

        values = LoaderMaster().loadPeriod(date2, date1)

        SMAvalues = [0] * (int(len(values) / int(self.period)))
        # Суммируем цены за периоды и делим их на сам период
        while index < len(values):
            # Когда определен целый период - делим сумму и записываем в массив
            if (index + 1) % self.period == 0:
                sum += values[index].Value
                value = float(sum) / self.period
                dateIndex = (SMAindex * self.period) + (self.period - 1)
                SMAvalues[SMAindex] = Valute(value,values[dateIndex].Date)
                sum = 0
                SMAindex += 1
            else:
                # Если период еще не прошел
                sum += values[index].Value
            index += 1

        self.SMA = SMAvalues
        self.Values = values

    # Если линия SMA лежит выше курс, то это тренд на понижение
    def __GetTrend(self, valueSMA, value):
        if valueSMA > value:
            return True
        else:
            return False

    def DoAnalysis(self):
        EndTrend = self.__GetTrend(self.Values[len(self.Values) - 1].Value, self.SMA[len(self.SMA) - 1].Value)
        self.TrendDegree = 0

        # Просмотр тренда SMA и курса валюты с конца
        index = len(self.Values) - 1
        while index > 0:
            trend = self.__GetTrend(self.Values[index].Value, self.SMA[int(index / self.period)].Value)

            if trend != EndTrend:
                break

            self.TrendDegree += 1
            index -= 1

        trend = ''

        if EndTrend == True:
            trend += 'Положительный тренд'
        else:
            trend += 'Отрицательный тренд'

        DrawMaster().DrawGrahs('Прогноз валюты на основе SMA',['Курс EUR','Линия SMA'], self.Values, self.SMA)

        return trend