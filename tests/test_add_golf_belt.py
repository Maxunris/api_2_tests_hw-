import requests
from selene import browser, have
import allure
from tests.conftest import DOMAIN_URL, LOGIN, PASSWORD
from utils.utils import post_demowebshop


def test_add_to_cart_golf_belt():

    with allure.step("Получаем куки для платья"):
        response = post_demowebshop("login", data={"Email": LOGIN, "Password": PASSWORD},
                                    allow_redirects=False)
        cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})

    with allure.step("Добавляем платье в корзину"):
        add_to_cart_url = "https://demowebshop.tricentis.com/addproducttocart/details/40/1"
        requests.post(add_to_cart_url, cookies={"NOPCOMMERCE.AUTH": cookie})

    with allure.step("Открываем корзину"):
        browser.open('https://demowebshop.tricentis.com/')
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open("https://demowebshop.tricentis.com/cart")

    with allure.step("Проверяем корзину"):
        browser.element('.product-name').should(have.text("Casual Golf Belt"))

    with allure.step('Удаляем товары'):
        browser.element('[name=removefromcart]').click()
        browser.element('[name=updatecart]').click()

    with allure.step('Проверяем, что в корзине ничего нет'):
        browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))