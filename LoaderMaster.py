import requests
import xml.etree.ElementTree as etree
from datetime import datetime, timedelta


# хранение данных о валюте
class Valute:
    def __init__(self, value, date):
        self.Date = date
        self.Value = value

# загрузка данных с сайта
class LoaderMaster:
    def __dateToString(self,date):
        string_date = date.strftime("%d") + "/" + date.strftime("%m") + "/" + str(int(date.strftime("%Y")))
        return string_date

    # актуальный курс валюты
    def loadActual(self):
        now_date = datetime.now()
        datePast = now_date
        values = []

        counter = 30
        while counter != 0:
            datePast = datePast - timedelta(days=1)
            counter -= 1

        now_date = self.__dateToString(now_date)
        datePast = self.__dateToString(datePast)

        url = f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={datePast}&date_req2={now_date}&VAL_NM_RQ=R01239"
        response = requests.get(url)
        xml_data = response.text
        root = etree.fromstring(xml_data)

        for record in root.findall('Record'):
            date = record.get('Date').replace('.', '/')
            value = float(record.find('Value').text.replace(',', '.'))
            nominal = int(record.find('Nominal').text)
            if nominal > 1:
                value = value / nominal

            cr_data = Valute(value, date)
            values.append(cr_data)

        return values[len(values) - 1]

    # данные о курсе на выбранный период
    def loadPeriod(self, startDate, endDate):
        values = []

        url = f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={startDate}&date_req2={endDate}&VAL_NM_RQ=R01239"
        response = requests.get(url)
        xml_data = response.text
        root = etree.fromstring(xml_data)

        for record in root.findall('Record'):
            date = record.get('Date').replace('.', '/')
            value = float(record.find('Value').text.replace(',', '.'))
            nominal = int(record.find('Nominal').text)
            if nominal > 1:
                value = value / nominal

            cr_data = Valute(value,date)
            values.append(cr_data)
        return values