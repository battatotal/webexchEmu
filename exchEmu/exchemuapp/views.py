from rest_framework.response import Response
from rest_framework.views import APIView
from .services import servReq


class MainView(APIView):


    def get(self, request):
        if request.GET:                                             #<<< проверяю словарь GET у объекта-запроса(передавались ли аргументы)
            if 'from' in request.GET and 'to' in request.GET and "value" in request.GET:    #<<< проверка наличия необъодимых параметров
                lst = {}                                            #<<< словарь, в котором будут параметры для запроса на сторонний сервис
                for key,value in request.GET.items():
                    lst[key] = value

                res = servReq(lst)                                   #<<< отрабатывается запрос к стороннему сервису

                return Response(res['args'])                         #<<< возвращается JSON с данными полученными из стороннего сервиса

            return Response({"GET": "допустимый набор параметров: 'from','to','value'"})
        return Response({"GET":"запрос без параметров"})
