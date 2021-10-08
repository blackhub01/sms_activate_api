import requests


API_KEY = YOUR-API-KEY-HERE
URL = 'https://sms-activate.ru/stubs/handler_api.php'


def responce(query):
    data = {
        'api_key': API_KEY,
    }
    total_data = data | query
    r = requests.request('POST', URL, data=total_data)
    return r.text


def getBalance():
    query = {
        'action': 'getBalance'
    }
    return responce(query)


def getNumber(service):
    """ Коды сервисов:
        full - полная аренда
        vk - вКонтакте
        ok - Одноклассники
        tg - Телеграм
        go - Google
        av - Авито
        ig - Instagram
        ym - Юла
        ma - Mail.Ru
        ya - Яндекс
        dp - ProtonMail
        hz - Drom
        wx - Apple
        ot - Любой другой
    """
    query = {
        'action': 'getNumber',
        'service': service,
        'forward': 0
    }
    # функция возвращает следующий список элементов:
    # 0 - строка
    # 1 - id операции
    # 2 - номер телефона
    return responce(query).split(':')


def setStatus(dict, status):
    """
    коды статуса:
        1 - сообщить о готовности номера (смс на номер отправлено)
        3 - запросить еще один код (бесплатно)
        6 - завершить активацию
        8 - сообщить о том, что номер использован и отменить активацию
    """
    query = {
        'action': 'setStatus',
        'id': dict[1],
        'status': status
    }
    return responce(query)


def getStatus(dict):
    query = {
        'action': 'getStatus',
        'id': dict[1],
    }
    return responce(query)
