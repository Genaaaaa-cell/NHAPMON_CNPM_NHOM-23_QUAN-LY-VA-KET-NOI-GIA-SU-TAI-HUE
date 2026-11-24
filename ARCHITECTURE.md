# KIẾN TRÚC HỆ THỐNG DỰ ÁN HUEUNI
**Tên dự án:** HueUni - Nền tảng Quản lý và Kết nối Gia sư tại Huế  
**Công nghệ sử dụng:** Python, SQL, HTML5, CSS3, GitHub, Jira.

## 1. Mô hình kiến trúc tổng thể (Layered / MVC Architecture)
Hệ thống áp dụng kiến trúc phân tầng (3-Tier Architecture) giúp tách biệt giao diện, xử lý nghiệp vụ và dữ liệu:
- **Presentation Layer (Tầng giao diện):** Sử dụng HTML5 và CSS3 để xây dựng giao diện trực quan cho Phụ huynh, Gia sư (sinh viên tại Huế) và Quản trị viên.
- **Application Layer (Tầng nghiệp vụ):** Sử dụng Python xử lý các logic cốt lõi: xác thực tài khoản sinh viên, thuật toán tìm kiếm và ghép lớp gia sư theo bán kính 3–5 km, quản lý lịch học và sổ liên lạc điện tử.
- **Data Access Layer (Tầng dữ liệu):** Sử dụng hệ quản trị cơ sở dữ liệu SQL để lưu trữ hồ sơ người dùng, danh sách lớp học, lịch dạy và đánh giá.

## 2. Cấu trúc thư mục dự án
HueUni/
├── database/               # Chứa các file script SQL tạo bảng và dữ liệu mẫu
├── services/               # Xử lý logic nghiệp vụ (tìm kiếm, ghép lớp, xác thực)
├── templates/              # Chứa các file giao diện HTML
├── static/                 # Chứa các file CSS, hình ảnh, JavaScript
└── ARCHITECTURE.md         # Tài liệu thiết kế kiến trúc hệ thống
