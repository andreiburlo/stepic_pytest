import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--lang', action='store', default=None,
                     help="Choose language: ec or fr")

@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption("lang")
    print("\nstart browser for test ... ")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser =webdriver.Chrome( options=options) #'.\\chromedriver.exe',
    yield browser
    print("\nquit browser..")
    browser.quit()