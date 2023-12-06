import subprocess
import time
import pytest
from appium import webdriver
from utils.android_utils import android_get_desired_capabilities
from selenium.webdriver.common.by import By
# from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='function')
def driver(run_appium_server):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities())
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    login_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_id"))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password_id"))
    )
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_button_id"))
    )

    login_input.send_keys("username")
    password_input.send_keys("password")
    login_button.click()
    time.sleep(2)
    return driver


@pytest.fixture(scope='function')
def logout(driver):
    logout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "logout_button_id"))
    )

    logout_button.click()
    time.sleep(2)
    return driver
