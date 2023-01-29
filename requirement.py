from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select


class Requirement:
    def __init__(self, driver):
        self.driver = driver
        self.Input_name_Xpath = "//input[@name='username']"
        self.pass_xpath = "//input[@name='password']"
        self.textarea_xpath = "//textarea[@name='comments']"
        self.file_xpath = "//input[@name='filename']"
        self.checkbox_xpath = "//input[@value='cb2']"
        self.radio_button_xpath = "//input[@value='rd1']"
        self.select_xpath = "//option[@value='ms2']"
        self.drop_clck = "//select[@name='dropdown']"
        self.sub_button = "//input[@value='submit']"

    def input_name(self):
        self.driver.find_element(By.XPATH, self.Input_name_Xpath).send_keys("hariom kumar")

    def pass_input(self):
        self.driver.find_element(By.XPATH, self.pass_xpath).send_keys("hariomkumarary")

    def text_input(self):
        self.driver.find_element(By.XPATH, self.textarea_xpath).send_keys("vill+post-badheri")

    def file_upload(self):
        self.driver.find_element(By.XPATH, self.file_xpath).send_keys(
            "/Users/hariomarya/Downloads/floral-background-design_1262-2549.webp")

    def check_box(self):
        self.driver.find_element(By.XPATH, self.checkbox_xpath).click()

    def radio_btn(self):
        self.driver.find_element(By.XPATH, self.radio_button_xpath).click()

    def selector(self):
        self.driver.find_element(By.XPATH, self.select_xpath).click()

    def drop_down(self):
        Select(self.driver.find_element(By.XPATH, self.drop_clck)).select_by_visible_text("Drop Down Item 4")

    def submit(self):
        self.driver.find_element(By.XPATH, self.sub_button).click()
