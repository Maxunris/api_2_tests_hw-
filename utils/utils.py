import requests
import allure
import curlify
import logging
from dotenv import load_dotenv
from allure_commons.types import AttachmentType

load_dotenv()
DOMAIN_URL = 'https://demowebshop.tricentis.com/'


def post_demowebshop(url, **kwargs):
    url = DOMAIN_URL + url
    with allure.step(f"POST {url}"):
        response = requests.post(url, **kwargs)
        curl = curlify.to_curl(response.request)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(curlify.to_curl(response.request))
        return response