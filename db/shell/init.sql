CREATE USER IF NOT EXISTS 'admin'@'%' IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';

FLUSH PRIVILEGES;

-- --------------------------------------------------------
-- init
-- --------------------------------------------------------
USE init;

CREATE TABLE IF NOT EXISTS init (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text VARCHAR(255) NOT NULL COMMENT 'text'
);

INSERT INTO init (text) VALUES
('test1');