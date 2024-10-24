from src.android.pages.market_page import MarketPage
from src.android.pages.login_page import LoginPage
from src.android.pages.create_account_page import CreateAccountPage


class TestCreateAccount:

    def setup_method(self):
        """
        페이지 오브젝트 셋업 메소드
        """
        self.market_page = MarketPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.create_account_page = CreateAccountPage(self.driver)

    def test_001(self):
        """
        앱 시작 후 asset > 계정 만들기 > 계정 생성 페이지 이동

        계정 생성 페이지 헤더가 제대로 노출되는지를 확인.
        """
        self.market_page.click_asset_tab()
        self.login_page.click_label_get_started()

        assert self.create_account_page.is_label_header_create_account_page_visible()

    def test_002(self, move_to_create_account_page):
        """
        계정 생성 페이지 > 패스워드 문자 validation 확인

        Test step
        1. 문자 입력 전 letter validation label 캡쳐
        2. 문자 "a" 입력
        3. 2번 스텝 후 letter validation label 캡쳐

        Expected result
        두 캡쳐를 비교해서 달라진 것을 확인하여 색상이 변한 것을 확인
        """
        before_input_password = self.create_account_page.get_screenshot_condition_box_letter()
        self.create_account_page.input_password("a")

        assert self.create_account_page.get_screenshot_condition_box_letter() != before_input_password

    def test_003(self, move_to_create_account_page):
        """
        계정 생성 페이지 > 패스워드 문자 validation 확인

        Test step
        1. 문자 입력 전 number validation label 캡쳐
        2. 문자 "1" 입력
        3. 2번 스텝 후 number validation label 캡쳐

        Expected result
        두 캡쳐를 비교해서 달라진 것을 확인하여 색상이 변한 것을 확인
        """
        before_input_password = self.create_account_page.get_screenshot_condition_box_number()
        self.create_account_page.input_password("1")

        assert self.create_account_page.get_screenshot_condition_box_number() != before_input_password

    def test_004(self, move_to_create_account_page):
        """
        계정 생성 페이지 > 패스워드 문자 validation 확인

        Test step
        1. 문자 입력 전 number, letter validation label 캡쳐
        2. 문자 "1a" 입력
        3. 2번 스텝 후 number, letter validation label 캡쳐

        Expected result
        두 캡쳐를 비교해서 달라진 것을 확인하여 색상이 변한 것을 확인
        """
        letter_box_before_input_password = self.create_account_page.get_screenshot_condition_box_letter()
        number_box_before_input_password = self.create_account_page.get_screenshot_condition_box_number()
        self.create_account_page.input_password("1a")

        assert self.create_account_page.get_screenshot_condition_box_letter() != letter_box_before_input_password
        assert self.create_account_page.get_screenshot_condition_box_number() != number_box_before_input_password