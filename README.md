# webexchEmu

URI для теста проекта /api/rates?from=USD&to=RUB&value=1
      В проекте отображена основная логика ТЗ - пользователь обращается к приложению, приложение в свою очередь обращается к стороннему сервису (в данном случае не нашел сервисов без регистрации, по этому использовал сервис не относящийся к теме валюты) при этом 
суть приложения не меняется - пользователь делает GET запрос c параметрами. Приложение с помощью библиотеки request обращается к стороннему сервису, передавая эти параметры, и получает результат(т.к в роли стороннего сервиса используется по сути заглушка,
то возвращаемые данные преобразую в ручную, хотя настоящий сервис бы вернул подсчитанный результат), и далее, полученный от стороннего сервиса результат, приложение возвращает в виде JSON.
