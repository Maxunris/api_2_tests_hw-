import requests
from selene import browser, have
import allure
from tests.conftest import DOMAIN_URL, LOGIN, PASSWORD
from utils.utils import post_demowebshop


def test_add_to_cart_diamond():
    with allure.step("Получаем куки для первого товара"):
        response = post_demowebshop("login", data={"Email": LOGIN, "Password": PASSWORD},
                                    allow_redirects=False)
        cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})

    with allure.step("Добавляем кулон  в корзину"):
        add_to_cart_url = "https://demowebshop.tricentis.com/addproducttocart/details/14/1"
        requests.post(add_to_cart_url, cookies={"NOPCOMMERCE.AUTH": cookie}, allow_redirects=False)

    with allure.step("Открываем корзину"):
        browser.open(DOMAIN_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open("https://demowebshop.tricentis.com/cart")

    with allure.step("Проверяем корзину"):
        browser.element('.product-name').should(have.text('Black & White Diamond Heart'))

    with allure.step('Удаляем товары'):
        browser.element('[name=removefromcart]').click()
        browser.element('[name=updatecart]').click()

    with allure.step('Проверяем, что в корзине ничего нет'):
        browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))