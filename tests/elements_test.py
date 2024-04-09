import time

from pages.elements_page import TextBotPage


class TestElements:

    def test_test_box(self, driver):
        text_box_page = TextBotPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
        output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
        assert full_name == output_name, "the full name does not match"
        assert email == output_email, "the email does not match"
        assert current_address == output_cur_address, "the current address does not match"
        assert permanent_address == output_per_address, "the permanent address does not match"
