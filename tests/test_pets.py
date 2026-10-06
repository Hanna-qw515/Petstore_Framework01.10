# tests_pets
from builtins import id

import allure
from allure_pytest.utils import allure_title


@allure.feature('Управление питомцами')
@allure.story('Создание')
@allure.title('Проверка успешного создания питомца')
def test_create_pet(api, test_pet_data):
    with allure.step('Отправка POST запроса на создание'):
        response = api.create_pet(test_pet_data)

    with allure.step('Проверка статуса кода'):
        assert response.status_code == 200

    with allure.step('Проверка имени созданного питомца в БД'):
        assert response.json()["name"] == "QA_Step"

@allure.feature('Управление питомцами')
@allure.story('Обновление')
@allure.title('Обновление статуса питомца на sold')
def test_update_pet_status(api, test_pet_data):
    test_pet_data["status"] = "sold"

    with allure.step('Отправка PUT запроса с новым статусом'):
        response = api.update_pet(test_pet_data)

    with allure.step('Проверка статуса кода 200'):
        assert response.status_code == 200

    with allure.step('Проверка что статус обновился'):
        assert response.json()["status"] == "sold"

@allure.feature('Управление питомцами')
@allure.story('Негативный тест')
@allure.title('Поиск несуществующего питомца - ожидаем 404')
def test_get_non_existent_pet(api):
    with allure.step('GET запрос питомца с ID = 0'):
        response = api.get_pet(0)

    with allure.step('Проверка статуса кода 404'):
        assert response.status_code == 404

@allure.feature("Управление питомцами")
@allure.story("Полный жизненный цикл")
@allure.title("E2E: создать питомца, удалить и проверить 404")
def test_full_pet_lifecycle(api, test_pet_data):

    with allure.step("Создаём питомца (POST)"):
        response = api.create_pet(test_pet_data)
        assert response.status_code == 200

    with allure.step("Удаляем питомца (DELETE)"):
        response = api.delete_pet(test_pet_data["id"])
        assert response.status_code == 200

    with allure.step("Проверяем что питомец удалён — ожидаем 404"):
        response = api.get_pet(test_pet_data["id"])
        assert response.status_code == 404

