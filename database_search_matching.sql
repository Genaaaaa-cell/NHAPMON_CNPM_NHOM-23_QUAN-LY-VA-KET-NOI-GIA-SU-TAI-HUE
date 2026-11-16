-- SCRUM-12: Thiet ke Database cho chuc nang Tim kiem & Ghep doi Gia su tai Hue
CREATE TABLE Tutor_Search_Profiles (
    tutor_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    district VARCHAR(100) NOT NULL,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    hourly_rate DECIMAL(10, 2),
    is_verified BOOLEAN DEFAULT FALSE
);

CREATE INDEX idx_subject_district ON Tutor_Search_Profiles(subject, district);
