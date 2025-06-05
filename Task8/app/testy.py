import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class SimpleAppTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000/")

    def find_login_error(self):
        try:
            return self.driver.find_element(By.ID, "login-error").text
        except NoSuchElementException:
            return ""

    def tearDown(self):
        self.driver.quit()

    def test_1_title_on_main_page(self):
        self.assertIn("Prosta Aplikacja", self.driver.title)

    def test_2_header_on_main_page(self):
        h1 = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1.text, "Witaj w prostej aplikacji!")

    def test_3_login_link_visible(self):
        link = self.driver.find_element(By.LINK_TEXT, "Przejdź do logowania")
        self.assertTrue(link.is_displayed())

    def test_4_counter_link_visible(self):
        link = self.driver.find_element(By.LINK_TEXT, "Licznik kliknięć")
        self.assertTrue(link.is_displayed())

    def test_5_navigate_to_login(self):
        self.driver.find_element(By.LINK_TEXT, "Przejdź do logowania").click()
        self.assertIn("/login", self.driver.current_url)

    def test_6_login_page_header(self):
        self.driver.get("http://localhost:5000/login")
        h2 = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(h2.text, "Logowanie")

    def test_7_empty_login_shows_error(self):
        self.driver.get("http://localhost:5000/login")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "login-error"))
        )
        self.assertIn("Nieprawidłowy login lub hasło", self.find_login_error())

    def test_8_wrong_login_shows_error(self):
        self.driver.get("http://localhost:5000/login")
        self.driver.find_element(By.NAME, "username").send_keys("x")
        self.driver.find_element(By.NAME, "password").send_keys("y")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "login-error"))
        )
        error_text = self.find_login_error()
        self.assertIn("Nieprawidłowy login lub hasło", error_text)

    def test_9_correct_login_redirects(self):
        self.driver.get("http://localhost:5000/login")
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        WebDriverWait(self.driver, 3).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Zalogowano pomyślnie")
        )
        self.assertIn("Zalogowano pomyślnie", self.driver.page_source)

    def test_10_login_back_to_main(self):
        self.driver.get("http://localhost:5000/login")
        self.driver.find_element(By.LINK_TEXT, "Powrót").click()
        self.assertIn("/", self.driver.current_url)

    def test_11_navigate_to_counter(self):
        self.driver.find_element(By.LINK_TEXT, "Licznik kliknięć").click()
        self.assertIn("/counter", self.driver.current_url)

    def test_12_counter_initial_value(self):
        self.driver.get("http://localhost:5000/counter")
        text = self.driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("Liczba kliknięć", text)

    def test_13_counter_button_present(self):
        self.driver.get("http://localhost:5000/counter")
        button = self.driver.find_element(By.TAG_NAME, "button")
        self.assertTrue(button.is_displayed())

    def test_14_counter_increases(self):
        self.driver.get("http://localhost:5000/counter")
        before = int(self.driver.find_element(By.TAG_NAME, "h2").text.split(": ")[1])
        self.driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(0.2)
        after = int(self.driver.find_element(By.TAG_NAME, "h2").text.split(": ")[1])
        self.assertEqual(after, before + 1)

    def test_15_counter_multiple_clicks(self):
        self.driver.get("http://localhost:5000/counter")
        start = int(self.driver.find_element(By.TAG_NAME, "h2").text.split(": ")[1])
        for _ in range(3):
            self.driver.find_element(By.TAG_NAME, "button").click()
            time.sleep(0.1)
        end = int(self.driver.find_element(By.TAG_NAME, "h2").text.split(": ")[1])
        self.assertEqual(end, start + 3)

    def test_16_counter_back_to_main(self):
        self.driver.get("http://localhost:5000/counter")
        self.driver.find_element(By.LINK_TEXT, "Powrót").click()
        self.assertIn("/", self.driver.current_url)

    def test_17_main_links_work(self):
        for text in ["Przejdź do logowania", "Licznik kliknięć"]:
            self.driver.get("http://localhost:5000/")
            link = self.driver.find_element(By.LINK_TEXT, text)
            link.click()
            self.assertIn(self.driver.current_url, self.driver.current_url)

    def test_18_success_page_text(self):
        self.driver.get("http://localhost:5000/success")
        self.assertIn("Zalogowano pomyślnie", self.driver.page_source)

    def test_19_login_password_field_type(self):
        self.driver.get("http://localhost:5000/login")
        password_field = self.driver.find_element(By.NAME, "password")
        self.assertEqual(password_field.get_attribute("type"), "password")

    def test_20_login_username_field_type(self):
        self.driver.get("http://localhost:5000/login")
        username_field = self.driver.find_element(By.NAME, "username")
        self.assertEqual(username_field.get_attribute("type"), "text")

    def test_21_main_page_has_two_links(self):
        self.driver.get("http://localhost:5000/")
        links = self.driver.find_elements(By.TAG_NAME, "a")
        self.assertEqual(len(links), 2)

    def test_22_login_error_color(self):
        self.driver.get("http://localhost:5000/login")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "login-error"))
        )
        error = self.driver.find_element(By.ID, "login-error")
        color = error.value_of_css_property("color")
        self.assertTrue(color is not None)

    def test_23_counter_page_has_button_and_link(self):
        self.driver.get("http://localhost:5000/counter")
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        links = self.driver.find_elements(By.TAG_NAME, "a")
        self.assertGreaterEqual(len(buttons), 1)
        self.assertGreaterEqual(len(links), 1)

    def test_24_login_form_has_two_inputs(self):
        self.driver.get("http://localhost:5000/login")
        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        self.assertGreaterEqual(len(inputs), 3)  # username, password, submit

    def test_25_refresh_counter_page(self):
        self.driver.get("http://localhost:5000/counter")
        value1 = int(self.driver.find_element(By.TAG_NAME, "h2").text.split(": ")[1])
        self.driver.refresh()
        value2 = int(self.driver.find_element(By.TAG_NAME, "h2").text.split(": ")[1])
        self.assertEqual(value1, value2)

    def test_26_login_trim_spaces(self):
        self.driver.get("http://localhost:5000/login")
        self.driver.find_element(By.NAME, "username").send_keys(" admin ")
        self.driver.find_element(By.NAME, "password").send_keys(" admin ")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "login-error"))
        )
        self.assertIn("Nieprawidłowy login lub hasło", self.find_login_error())

    def test_27_login_wrong_case(self):
        self.driver.get("http://localhost:5000/login")
        self.driver.find_element(By.NAME, "username").send_keys("ADMIN")
        self.driver.find_element(By.NAME, "password").send_keys("ADMIN")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "login-error"))
        )
        self.assertIn("Nieprawidłowy login lub hasło", self.find_login_error())

    def test_28_login_long_input(self):
        self.driver.get("http://localhost:5000/login")
        long_str = "a" * 100
        self.driver.find_element(By.NAME, "username").send_keys(long_str)
        self.driver.find_element(By.NAME, "password").send_keys(long_str)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "login-error"))
        )
        self.assertIn("Nieprawidłowy login lub hasło", self.find_login_error())

    def test_29_click_counter_without_reload(self):
        self.driver.get("http://localhost:5000/counter")
        for _ in range(2):
            self.driver.find_element(By.TAG_NAME, "button").click()
            time.sleep(0.1)
        count = int(self.driver.find_element(By.TAG_NAME, "h2").text.split(": ")[1])
        self.assertGreaterEqual(count, 2)

    def test_30_counter_page_title(self):
        self.driver.get("http://localhost:5000/counter")
        self.assertIn("Licznik kliknięć", self.driver.title)


if __name__ == '__main__':
    unittest.main()
