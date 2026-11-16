import hashlib

class User:
    def __init__(self, user_id: int, username: str, password_hash: str, role: str = "MEMBER"):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash  # Mật khẩu đã băm
        self.role = role                    # "LIBRARIAN" (Thủ thư) hoặc "MEMBER" (Thành viên)


class AuthService:
    def __init__(self):
        # Giả lập cơ sở dữ liệu lưu trữ người dùng trong bộ nhớ
        self.user_db = {}

    def hash_password(self, raw_password: str) -> str:
        """Mã hóa mật khẩu bằng thuật toán SHA-256."""
        return hashlib.sha256(raw_password.encode('utf-8')).hexdigest()

    def validate_password_strength(self, password: str) -> bool:
        """Kiểm tra độ mạnh của mật khẩu (tối thiểu 6 ký tự)."""
        if not password or len(password) < 6:
            return False
        return True

    def register(self, user_id: int, username: str, raw_password: str, role: str = "MEMBER") -> bool:
        """Đăng ký tài khoản mới."""
        if username in self.user_db:
            return False  # Tên đăng nhập đã tồn tại
        if not self.validate_password_strength(raw_password):
            return False  # Mật khẩu không đạt yêu cầu

        hashed_pw = self.hash_password(raw_password)
        new_user = User(user_id, username, hashed_pw, role)
        self.user_db[username] = new_user
        return True

    def login(self, username: str, raw_password: str) -> bool:
        """Xử lý logic đăng nhập."""
        user = self.user_db.get(username)
        if not user:
            return False  # Không tìm thấy tài khoản
        return user.password_hash == self.hash_password(raw_password)