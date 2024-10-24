# Flipster test

_Flipster_ 의 안드로이드앱을 이용해서 간단한 테스트케이스 4개를 작성하였습니다.

실행 방법은 아래와 같습니다.

1. `appium server --allow-insecure=chromedriver_download`
2. `python3 -m venv venv`
3. `source venv/bin/activate`
4. `pip3 install -r requirements.txt`
5. `pytest tests/android/test_create_account.py --platform=android --alluredir=allure-results`

## Driver generate
드라이버 생성로직은 `conftest.py`를 확인해주세요.

## Test case
`tests/android/test_create_account.py` 를 확인해주세요. 계정 생성 페이지에서 패스워드를 넣었을 때 활성화되는 validation label의 색상변화를 base64의 스크린샷으로 찍어 비교 하고 있습니다.

## PageObject
페이지 클래스에 대해서는 `src/android/pages` 를 확인해주세요.
