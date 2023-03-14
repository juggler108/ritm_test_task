from selenium.webdriver.common.by import By


class CheckBoxPageLocators:
    CARD_LIST = (By.CSS_SELECTOR, "#app .card")
    CHECK_BOX_PAGE = (By.CSS_SELECTOR, ".show #item-1")
    HOME_ICON_EXPAND_OPEN = (By.CSS_SELECTOR, "#tree-node > ol > li > span > button > svg")
    DOWNLOADS_ICON_EXPAND_OPEN = (By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[3]/span/button")
    WORD_FILE_LABEL = (By.CSS_SELECTOR, "label[for='tree-node-wordFile']")
    TEXT_SUCCESS = (By.CSS_SELECTOR, ".text-success")
