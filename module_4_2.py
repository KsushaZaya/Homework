def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # Ничего не возвращает


#inner_function()  # Выдает ошибку, т.к. вызов из предыдущего пространства имен невозможен.

test_function() #Работает, т.к. вызывается глобальное пространство имен, содержащее нужную нам функцию.