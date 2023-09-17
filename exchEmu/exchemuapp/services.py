import requests




def servReq(requestParamList):
    """Для обращения к стороннему серверу использую библиотеку requests"""
    respond = requests.get('https://httpbin.org/get', params=requestParamList)
    r = respond.json()

    #Формирую якобы результат работы стороннего сервера
    val = r['args']['value'] #сохраняю количество
    r['args'].clear()
    r['args']['result'] = 62.16 * int(val)

    return r