import appium.webdriver

from src.android.android_page_factory import AndroidPageFactory
from src.android.locators import create_account_page_locator


class CreateAccountPage(AndroidPageFactory):

    def __init__(self, driver: appium.webdriver.Remote):
        super().__init__(driver)

    def is_label_header_create_account_page_visible(self) -> bool:
        header = self.find_element_for_wait(create_account_page_locator.LABEL_HEADER_CREATE_ACCOUNT_PAGE)
        return header.is_displayed() and header.text == "Create account"

    def input_password(self, password: str):
        self.input(create_account_page_locator.INPUT_PASSWORD, password)

    def get_screenshot_condition_box_letter(self) -> str:
        return self.find_element_for_wait(create_account_page_locator.LABEL_LETTER).screenshot_as_base64

    def get_screenshot_condition_box_number(self) -> str:
        return self.find_element_for_wait(create_account_page_locator.LABEL_NUMBER).screenshot_as_base64

    def get_screenshot_condition_box_special_symbol(self) -> str:
        return self.find_element_for_wait(create_account_page_locator.LABEL_SPECIAL_SYMBOL).screenshot_as_base64

    def get_screenshot_condition_box_least_characters(self) -> str:
        return self.find_element_for_wait(create_account_page_locator.LABEL_LEAST_CHARACTERS).screenshot_as_base64
