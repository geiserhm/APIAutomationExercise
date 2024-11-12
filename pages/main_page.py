from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.endpoint_url = "#example > div > div > div.column.has-text-centered > div.endpoint-url.notification.is-dark.is-family-code.is-size-7"


    def get_endpoint_value(self):
        value = self.driver.find_element(By.CSS_SELECTOR, self.endpoint_url)
        return value.text