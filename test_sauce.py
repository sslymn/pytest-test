import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_Source:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        self.driver.quit()

    def login_info(self, username, password):
        userNameInput = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "user-name")))
        passwordInput = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "password")))    
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "login-button")))
        loginBtn.click()

    @pytest.mark.parametrize("username, password", [("1", "1"),("2","2"),("3","3")])
    def test_invalid_login(self,username,password):
        userNameInput = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"password")))
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage =WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

    def test_both(self):
        self.login_info("", "")
        errorMessage = self.driver.find_element(By.CSS_SELECTOR, "h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"KULLANICI ADI VE ŞİFRE ALANLARININ BOŞ GEÇİLDİĞİ TESTİ SONUCU: {testResult}")
        assert testResult, "Hatalı"

    def test_fpassword(self):
        self.login_info("standard_user", "")
        errorMessage = self.driver.find_element(By.XPATH, "//div[@id='login_button_container']//form//h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"ŞİFRE ALANININ BOŞ GEÇİLDİĞİ TESTİ SONUCU: {testResult}")
        assert testResult, "Metin hatalı"

    def test_locked_out(self):
        self.login_info("locked_out_user", "secret_sauce")
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"ŞİFRE ALANININ BOŞ GEÇİLDİĞİ TESTİ SONUCU: {testResult}")
        assert testResult, "Metin hatalı"

    def test_login_list(self):
        self.login_info("standard_user", "secret_sauce")
        WebDriverWait(self.driver, 5).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
        p_list = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        testResult = len(p_list) == 6
        assert testResult, "Ürün sayısı 6 değil"

    def test_login(self):
        self.login_info("problem_user", "secret_sauce")
        assert "https://www.saucedemo.com/inventory.html" in self.driver.current_url, "Giriş başarısız"
        print("Giriş başarılı")

    def test_logout(self):
        self.test_login()
        burger_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        burger_button.click()
        logout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_button.click()
        WebDriverWait(self.driver, 5).until(EC.url_to_be("https://www.saucedemo.com/"))
        assert "https://www.saucedemo.com/" in self.driver.current_url, "Çıkış başarısız"
        print("Çıkış başarılı")

    def test_checkout(self):
        self.login_info("standard_user", "secret_sauce")
        add_to_cart_button = self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()
        remove_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "remove-sauce-labs-backpack")))
        assert remove_button.text == "Remove"

# testClass = Test_Source()
# testClass.test_invalid_login()
# testClass.test_both()
# testClass.test_fpassword()
# testClass.test_login_list()
# testClass.test_login()
# testClass.test_logout()
# testClass.test_checkout()
