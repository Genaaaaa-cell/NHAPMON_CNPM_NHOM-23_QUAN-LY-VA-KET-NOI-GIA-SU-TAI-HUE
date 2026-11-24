from datetime import datetime

# Giả lập cơ sở dữ liệu lưu trong bộ nhớ (In-memory database)
lessons_db = [
    {"lesson_id": 1, "tutor_name": "Nguyen Van A", "student_name": "Tran Thi B", "date": "2026-06-05", "status": "Scheduled", "rating": None, "feedback": None},
    {"lesson_id": 2, "tutor_name": "Nguyen Van A", "student_name": "Le Van C", "date": "2026-06-06", "status": "Scheduled", "rating": None, "feedback": None}
]

def check_in_lesson(lesson_id):
    """
    Chức năng Điểm danh/Xác nhận hoàn thành buổi học (Schedule Management)
    """
    for lesson in lessons_db:
        if lesson["lesson_id"] == lesson_id:
            if lesson["status"] == "Completed":
                return f"Buổi học #{lesson_id} đã được xác nhận trước đó rồi."
            
            lesson["status"] = "Completed"
            return f"Thành công: Buổi học #{lesson_id} giữa gia sư {lesson['tutor_name']} và học viên {lesson['student_name']} đã được đánh dấu hoàn thành."
            
    return f"Lỗi: Không tìm thấy buổi học với ID #{lesson_id}"


def submit_tutor_review(lesson_id, rating, feedback):
    """
    Chức năng Đánh giá gia sư sau buổi học (Reviews & Rating)
    """
    if not (1 <= rating <= 5):
        return "Lỗi: Điểm đánh giá (rating) phải từ 1 đến 5 sao."

    for lesson in lessons_db:
        if lesson["lesson_id"] == lesson_id:
            if lesson["status"] != "Completed":
                return f"Lỗi: Không thể đánh giá buổi học #{lesson_id} vì chưa hoàn thành."
            
            lesson["rating"] = rating
            lesson["feedback"] = feedback
            return f"Thành công: Đã ghi nhận {rating} sao cho gia sư {lesson['tutor_name']} với nhận xét: '{feedback}'."
            
    return f"Lỗi: Không tìm thấy buổi học với ID #{lesson_id}"

# ==================== TEST CHẠY THỬ ====================
if __name__ == "__main__":
    print("--- TRƯỚC KHI CẬP NHẬT ---")
    print(lessons_db[0])
    
    print("\n--- 1. THỰC HIỆN ĐIỂM DANH BUỔI HỌC 1 ---")
    print(check_in_lesson(1))
    
    print("\n--- 2. THỰC HIỆN ĐÁNH GIÁ SAU BUỔI HỌC 1 ---")
    print(submit_tutor_review(1, 5, "Gia sư giảng bài dễ hiểu, nhiệt tình và đúng giờ tại Huế."))
    
    print("\n--- TRẠNG THÁI SAU KHI CẬP NHẬT ---")
    print(lessons_db[0])
#hoàn thành công việc
