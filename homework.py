from datetime import time


def test_dark_theme_by_time(dark_theme_by_time_data):
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = dark_theme_by_time_data[0]
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    if 6 <= current_time < 22:
        is_dark_theme = False
    else:
        is_dark_theme = True

    assert is_dark_theme is dark_theme_by_time_data[1]


def test_dark_theme_by_time_and_user_choice(dark_theme_by_time__and_user_data):
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = dark_theme_by_time__and_user_data[0]
    dark_theme_enabled_by_user = dark_theme_by_time__and_user_data[1]
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    if dark_theme_enabled_by_user:
        is_dark_theme = True
    elif 6 <= current_time < 22:
        is_dark_theme = False
    else:
        is_dark_theme = True if dark_theme_enabled_by_user is None else False

    assert is_dark_theme is dark_theme_by_time__and_user_data[2]


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = [user for user in users if user["name"] == "Olga"][0]
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = [user for user in users if user["age"] < 20]
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = return_function_info(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = return_function_info(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = return_function_info(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"


def return_function_info(object_, *params):
    result = ' '.join(([word.capitalize() for word in object_.__name__.split("_")]
                              + [f"{list(params)}"])).replace("'", "")
    print(result)

    return result
