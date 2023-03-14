from locators.elements_page_locators import CheckBoxPageLocators
from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def go_to_elements_page(self):
        elements_page = self.elements_are_visible(self.locators.CARD_LIST)
        elements_page[0].click()

    def go_to_check_box_page(self):
        self.element_is_visible(self.locators.CHECK_BOX_PAGE).click()

    def open_path_home_downloads_and_choose_checkbox_word_file(self):
        self.element_is_visible(self.locators.HOME_ICON_EXPAND_OPEN).click()
        self.element_is_visible(self.locators.DOWNLOADS_ICON_EXPAND_OPEN).click()
        self.element_is_visible(self.locators.WORD_FILE_LABEL).click()
        text_success = self.element_is_present(self.locators.TEXT_SUCCESS).text
        return text_success
