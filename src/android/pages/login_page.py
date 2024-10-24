import appium.webdriver

from src.android.android_page_factory import AndroidPageFactory
from src.android.locators import login_page_locator


class LoginPage(AndroidPageFactory):

    def __init__(self, driver: appium.webdriver.Remote):
        super().__init__(driver)

    def click_label_get_started(self):
        self.click(login_page_locator.LABEL_GET_STARTED)


