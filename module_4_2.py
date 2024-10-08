def test_function():
    def inner_function():
        print('Я внутри области видимости функции test_function')

    inner_function()


test_function()
inner_function()       #Приведёт к ошибке, потому что находится вне области видимости
                       # функции test_function, где была впервые объявлена.

