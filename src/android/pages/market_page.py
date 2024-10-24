import appium.webdriver

from src.android.android_page_factory import AndroidPageFactory


class MarketPage(AndroidPageFactory):

    def __init__(self, driver: appium.webdriver.Remote):
        super().__init__(driver)
