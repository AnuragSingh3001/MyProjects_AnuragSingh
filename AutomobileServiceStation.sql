CREATE TABLE IF NOT EXISTS user1_info (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    pass VARCHAR(255) NOT NULL,
    phone VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS create_receipt (
    receipt_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    vno VARCHAR(20) NOT NULL,
    maker_name VARCHAR(255) NOT NULL,
    model_type VARCHAR(255) NOT NULL,
    phone VARCHAR(10) NOT NULL,
    user_id INT,
    book_date DATETIME,
    price DECIMAL(10, 2),
    mechanic VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES user1_info(user_id)
);

CREATE TABLE IF NOT EXISTS report (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    phone VARCHAR(10) NOT NULL,
    issue TEXT NOT NULL
);
