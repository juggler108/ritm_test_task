from pages.elements_page import CheckBoxPage


class TestElements:
    class TestCheckBoxPage:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/")
            check_box_page.open()
            check_box_page.go_to_elements_page()
            check_box_page.go_to_check_box_page()
            text_success = check_box_page.open_path_home_downloads_and_choose_checkbox_word_file()
            assert text_success == "wordFile", "word file checkbox was not selected"

