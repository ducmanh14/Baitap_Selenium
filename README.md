# BÁO CÁO BÀI TẬP KIỂM THỬ TỰ ĐỘNG BẰNG SELENIUM

## 1. Thông tin sinh viên
- **Họ và tên:** Mai Đức Mạnh
- **Mã sinh viên:** 23010814

## 2. Công nghệ sử dụng
- **Ngôn ngữ lập trình:** Python (Phiên bản 3.14)
- **Thư viện chính:** Selenium WebDriver v4
- **Framework chạy test:** Pytest
- **Trình duyệt thử nghiệm:** Google Chrome

## 3. Website thử nghiệm
- **Hệ thống cấu hình:** `https://the-internet.herokuapp.com/login`

## 4. Chi tiết các Test Cases đã xây dựng
Dự án đã xây dựng và chạy thành công tối thiểu 03 kịch bản kiểm thử tự động (Automation Test Cases) bao gồm:

| STT | Tên Test Case | Các bước thực hiện kịch bản | Kết quả mong đợi (Assertion) | Trạng thái thực tế |
|---|---|---|---|---|
| 1 | `test_login_success` | 1. Truy cập trang Login.<br>2. Điền chính xác tài khoản (`tomsmith`/`SuperSecretPassword!`).<br>3. Bấm nút Submit. | Hệ thống chuyển hướng thành công và hiển thị dòng chữ thông báo: "You logged into a secure area!" | **Passed** (Thành công) |
| 2 | `test_login_fail` | 1. Truy cập trang Login.<br>2. Điền đúng username nhưng mật khẩu sai.<br>3. Bấm nút Submit. | Hệ thống chặn lại và hiển thị dòng thông báo lỗi màu đỏ: "Your password is invalid!" | **Passed** (Thành công) |
| 3 | `test_logout` | 1. Đăng nhập thành công vào hệ thống.<br>2. Trên giao diện Secure Area, bấm nút "Logout". | Hệ thống đăng xuất thành công, đưa về trang Login và hiển thị thông báo: "You logged out of the secure area!" | **Passed** (Thành công) |

## 5. Hướng dẫn cài đặt và chạy thử code trên máy local
1. Cài đặt các thư viện cần thiết:
   ```bash
   pip install selenium pytest
