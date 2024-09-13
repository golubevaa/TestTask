from faker import Faker
from src.pages.main_page import MainPage
from src.pages.login_page import LoginPage
from src.pages.account_information_page import AccountInformationPage
from src.pages.account_created_page import AccountCreatedPage
from src.pages.delete_account_page import DeleteAccountPage
from src.entities.signup_data import GENDER_VALUES, DAYS, MONTHS, YEARS, COUNTRY
from random import choice
from allure import step, title, suite


@suite("Users Operations")
class TestLogin:

    @title("Register User E2E Test")
    def test_full_login_process(self, page):

        expected_sign_up_text = "New User Signup!"
        expected_account_info_text = "ENTER ACCOUNT INFORMATION"
        expected_created_account_text = "ACCOUNT CREATED!"
        expected_account_deleted_text = "ACCOUNT DELETED!"
        person = Faker()
        first_name = person.first_name()
        gender = choice(GENDER_VALUES)
        day = choice(DAYS)
        month = choice(MONTHS)
        year = choice(YEARS)
        country = choice(COUNTRY)

        main_page = MainPage(page)
        main_page.open_page()

        with step("Page is visible"):
            assert main_page.is_visible
        main_page.click_on_sign_up_button()

        login_page = LoginPage(page)
        with step("Text about new user signup is displayed"):
            assert expected_sign_up_text in login_page.signup_title.inner_text(), \
                "Title contain text about beginning of sing up"
            assert login_page.signup_title.is_visible(), \
                "Title is displayed"

        login_page.perform_sign_up_preparations(name=first_name, email=person.email())

        account_info_page = AccountInformationPage(page)
        with step("Text about filling account info is displayed"):
            assert expected_account_info_text in account_info_page.enter_account_info_title.inner_text(), \
                "Title contains text about filling profile"
            assert account_info_page.enter_account_info_title.is_visible(), \
                "Title is displayed"

        account_info_page.enter_account_information(gender=gender, person=person,
                                                    day=day, month=month, year=year)
        account_info_page.enter_address_information(name=first_name, person=person, country=country)
        account_info_page.create_account()

        account_created_page = AccountCreatedPage(page)
        with step("Text about account creation is displayed"):
            assert expected_created_account_text in account_created_page.account_created_title.inner_text(), \
                "Title contains text about account creation"
            assert account_created_page.account_created_title.is_visible(), \
                "Title is displayed"

        account_created_page.continue_usage()

        with step("Text 'Logged in as {}' is displayed".format(first_name)):
            assert main_page.login_label(first_name).is_visible()

        main_page.delete_account()

        delete_account_page = DeleteAccountPage(page)
        with step("Text about account remove is displayed"):
            assert expected_account_deleted_text in delete_account_page.account_deleted_label.inner_text(), \
                "Title contains text about user's delete"
            assert delete_account_page.account_deleted_label.is_visible(), \
                "Title is displayed"

        delete_account_page.click_to_continue_button()
