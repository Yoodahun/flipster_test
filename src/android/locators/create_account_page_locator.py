from appium.webdriver.common.appiumby import AppiumBy

LABEL_HEADER_CREATE_ACCOUNT_PAGE = (AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.TextView[1]')
INPUT_PASSWORD = (AppiumBy.XPATH, "//android.widget.TextView[@text='Password']/parent::android.widget.EditText")
LABEL_LETTER = (AppiumBy.XPATH, "//android.widget.TextView[@text='Letter']")
LABEL_NUMBER = (AppiumBy.XPATH, "//android.widget.TextView[@text='Number']")
LABEL_SPECIAL_SYMBOL = (AppiumBy.XPATH, "//android.widget.TextView[@text='Special symbol']")
LABEL_LEAST_CHARACTERS = (AppiumBy.XPATH, "//android.widget.TextView[@text='Least 8 characters']")
