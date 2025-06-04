from datetime import time


# тест-кейсы для функции test_dark_theme_by_time
"""Время, Ожидаемый результат"""
dark_theme_tests_by_time = [
		[time(hour=6).hour, False],
		[time(hour=22).hour, True],
		[time(hour=17).hour, False],
		[time(hour=5).hour, True],
		[time(hour=0).hour, True]
]

# тест-кейсы для функции test_dark_theme_by_time
"""
с 22 до 6 часов утра - ночная тема
Протестируйте правильность переключения темной темы на сайте в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
[Время, Выбор пользователя, Ожидаемый результат]
"""
dark_theme_tests_by_time_and_user = [
	[time(hour=3).hour, True, True],
	[time(hour=12).hour, True, True],
	[time(hour=6).hour, True, True],
	[time(hour=23).hour, False, False],
	[time(hour=8).hour, False, False],
	[time(hour=22).hour, None, True],
	[time(hour=5).hour, None, True],
	[time(hour=6).hour, None, False],
	[time(hour=21).hour, None, False],
	[time(hour=7).hour, None, False]
]
