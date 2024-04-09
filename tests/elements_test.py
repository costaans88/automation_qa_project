import time

from pages.elements_page import TextBotPage


class TestElements:

    def test_test_box(self, driver):
        text_box_page = TextBotPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        text_box_page.fill_all_fields()
        output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
        print(output_name)
        print(output_email)
        print(output_cur_address)
        print(output_per_address)
