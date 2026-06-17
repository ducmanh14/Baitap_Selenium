import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) # Đợi tối đa 10 giây để load element
    driver.maximize_window()
    yield driver
    driver.quit()

# --- TEST CASE 1: ĐĂNG NHẬP THÀNH CÔNG ---
def test_login_success(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    
    # Điền đúng tài khoản mẫu của trang cung cấp
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    
    # Bấm nút Login bằng CSS Selector
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Kiểm tra thông báo thành công màu xanh lá
    success_message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_message


# --- TEST CASE 2: ĐĂNG NHẬP THẤT BẠI (SAI PASSWORD) ---
def test_login_fail(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    
    # Điền sai mật khẩu
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("WrongPassword123")
    
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Kiểm tra thông báo lỗi màu đỏ
    error_message = driver.find_element(By.ID, "flash").text
    assert "Your password is invalid!" in error_message


# --- TEST CASE 3: ĐĂNG XUẤT HỆ THỐNG (LOGOUT) ---
def test_logout(driver):
    # Đăng nhập trước khi đăng xuất
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Bấm nút Logout trên giao diện sau khi đăng nhập thành công
    driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()
    
    # Kiểm tra xem đã quay về trang login thành công chưa
    logout_message = driver.find_element(By.ID, "flash").text
    assert "You logged out of the secure area!" in logout_message