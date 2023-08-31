from datetime import datetime
import yadisk

# загрузка данных на яндекс диск
class YandexDiskMaster:
    # Имя папки на диске
    dirName = 'ExchangeRateAnalysis'

    def __init__(self, yaToken):
        self.token = yaToken
        self.sender = yadisk.YaDisk(token=yaToken)

    # Отправка данных на диск
    def SendFile(self, fileName, fileExtension):

        # Тест токена
        if self.sender.check_token() != True:
            print('Нет доступа к Яндекс Диску')
            return

        # В имя каждого файла записывается дата сохранения
        dateN = datetime.strftime(datetime.now(), "%d.%m.%Y-%H.%M.%S")
        # Если папки на диске нет - создаем
        if not self.sender.is_dir('/' + self.dirName):
            self.sender.mkdir('/' + self.dirName)
        # Отправка файлов
            self.sender.upload(fileName, '/' + self.dirName + '/graph' + dateN + fileExtension)