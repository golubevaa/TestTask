from faker import Faker

from src.pages.main_page import MainPage
from src.pages.login_page import LoginPage
from src.pages.account_information_page import AccountInformationPage
from src.pages.account_created_page import AccountCreatedPage


class TestLogin:

    def test_full_login_process(self, page):

        expected_sign_up_text = "New User Signup!"
        expected_account_info_text = "Enter Account Information"
        expected_created_account_text = "ACCOUNT CREATED!"
        faker = Faker()
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        password = faker.password()
        company = faker.company()
        address = faker.address()
        city = faker.city()
        sec_address = faker.secondary_address()
        state = faker.state()
        zipcode = faker.zipcode()
        phone = faker.phone_number()

        main_page = MainPage(page)
        main_page.open_page()
        main_page.click_on_sign_up_button()
        assert page.get_by_text(expected_sign_up_text).is_visible()

        login_page = LoginPage(page)
        login_page.fill_input_name(first_name)
        login_page.fill_input_email(email)
        login_page.signup()
        assert page.get_by_text(expected_account_info_text).is_visible()

        account_info_page = AccountInformationPage(page)
        account_info_page.select_gender()
        account_info_page.fill_password(password)
        account_info_page.select_date_of_birth()
        account_info_page.select_newsletter_checkbox()
        account_info_page.select_offers_checkbox()
        account_info_page.fill_first_name(first_name)
        account_info_page.fill_last_name(last_name)
        account_info_page.fill_company(company)
        account_info_page.fill_address(address)
        account_info_page.fill_sec_address(sec_address)
        account_info_page.select_country()
        account_info_page.fill_state(state)
        account_info_page.fill_city(city)
        account_info_page.fill_zipcode(zipcode)
        account_info_page.fill_phone(phone)
        account_info_page.create_account()

        assert page.get_by_text(expected_created_account_text).is_visible()

        AccountCreatedPage(page).continue_usage()
        pass










