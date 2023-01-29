import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup(request):
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
    yield
    request.cls.driver.quit()
