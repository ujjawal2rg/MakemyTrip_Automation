import pytest
from selenium import webdriver




def pytest_addoption(parser): #for cross browser cmd line
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
    elif browser_name == "edge":
        driver=webdriver.Edge(executable_path="C:\Driver\edgedriver.exe")
    driver.get("https://www.makemytrip.com/")
    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()







