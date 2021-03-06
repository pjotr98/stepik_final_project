import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang: en, es, fr, uk")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_language = request.config.getoption("language")
    if browser_name == "chrome":
        # Chrome option
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        # options.add_argument("window-size=1400,2100")
        # options.add_argument('--disable-gpu')
        print("\nstart Chrome browser for test..")
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        # Firefox option
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", browser_language)
        print("\nstart Firefox browser for test..")
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
