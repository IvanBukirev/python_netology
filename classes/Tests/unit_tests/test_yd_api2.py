import os
import time

import pytest
import requests
from dotenv import load_dotenv

load_dotenv("../../../.env")
API_URL = "https://cloud-api.yandex.net/v1/disk/resources"
TOKEN = os.getenv("YANDEX_DISK_TOKEN")

if not TOKEN:
    pytest.skip("YANDEX_DISK_TOKEN не установлен", allow_module_level=True)

HEADERS = {"Authorization": f"OAuth {TOKEN}"}
TEST_FOLDER = "test_folder_pytest_12345"


def create_folder(folder_name):
    """Создает папку на Яндекс.Диске"""
    params = {"path": f"/{folder_name}"}
    return requests.put(API_URL, headers=HEADERS, params=params)


def delete_folder(folder_name):
    """Удаляет папку с Яндекс.Диска"""
    params = {"path": f"/{folder_name}", "permanently": "true"}
    return requests.delete(API_URL, headers=HEADERS, params=params)


def folder_exists(folder_path):
    """Проверяет существование папки по полному пути"""
    params = {"path": folder_path}
    response = requests.get(API_URL, headers=HEADERS, params=params)
    return response.status_code == 200


def test_token_validity():
    """Проверка валидности токена"""
    response = requests.get("https://cloud-api.yandex.net/v1/disk", headers=HEADERS)
    assert response.status_code == 200, f"Токен невалиден: {response.status_code}"
    print(f"Токен действителен, имя диска: {response.json().get('user', {}).get('display_name')}")


@pytest.fixture(scope="module", autouse=True)
def cleanup():
    """Фикстура для удаления тестовой папки после тестов"""
    yield
    delete_folder(TEST_FOLDER)
    time.sleep(1)


def test_create_folder_success():
    """Тест успешного создания папки"""
    if folder_exists(f"/{TEST_FOLDER}"):
        delete_folder(TEST_FOLDER)
        time.sleep(1)

    response = create_folder(TEST_FOLDER)
    assert response.status_code == 201
    assert folder_exists(f"/{TEST_FOLDER}")


def test_create_folder_already_exists():
    """Тест создания существующей папки"""
    if not folder_exists(f"/{TEST_FOLDER}"):
        create_folder(TEST_FOLDER)
        time.sleep(1)

    response = create_folder(TEST_FOLDER)
    assert response.status_code == 409
    assert "уже существует" in response.json().get("message", "").lower()


def test_create_folder_unauthorized():
    """Тест с неверным токеном"""
    invalid_headers = {"Authorization": "OAuth invalid_token_12345"}
    params = {"path": f"/{TEST_FOLDER}_unauth"}
    response = requests.put(API_URL, headers=invalid_headers, params=params)
    assert response.status_code == 401


def test_create_folder_invalid_name():
    """Тест с заведомо недопустимыми символами"""
    # Используем действительно запрещенные символы: \ / : * ? " < > |
    invalid_name = 'invalid\\/*?"<>|name'
    response = create_folder(invalid_name)

    assert response.status_code in [400, 409], (
            f"Ожидался код 400 или 409, получен {response.status_code}"
    )
    error_message = response.json().get("message", "").lower()
    assert any(keyword in error_message for keyword in ["недопустим", "запрещён", "invalid", "conflict"]), (
            f"Неожиданное сообщение об ошибке: {error_message}"
    )
