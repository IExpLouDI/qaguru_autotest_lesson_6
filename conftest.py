import pytest
from test_cases.test_case_dark_by_time import dark_theme_tests_by_time, dark_theme_tests_by_time_and_user


def gen_ids(fixture_value):

	if len(fixture_value) == 2:
		return f"Test hour - {fixture_value[0]}. Expected result = {fixture_value[1]}."
	elif len(fixture_value) == 3:
		return (f"Test hour - {fixture_value[0]}. Enabled_by_user - {fixture_value[1]}. "
				f"Expected result = {fixture_value[2]}.")

	return "Заглушка"

@pytest.fixture(scope="function", params=dark_theme_tests_by_time, ids=gen_ids)
def dark_theme_by_time_data(request):
	"""Генерация тестовых данных"""
	yield request.param


@pytest.fixture(scope="function", params=dark_theme_tests_by_time_and_user, ids=gen_ids)
def dark_theme_by_time__and_user_data(request):
	"""Генерация тестовых данных"""
	yield request.param
