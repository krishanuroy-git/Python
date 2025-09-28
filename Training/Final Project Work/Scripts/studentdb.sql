CREATE DATABASE student_db;

USE student_db;
CREATE TABLE students (
    studentid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    faculty_name VARCHAR(100) NOT NULL
);

CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    studentid INT NOT NULL,
    courseid INT NOT NULL,
    rating INT NOT NULL,
    comments TEXT,
    FOREIGN KEY (courseid) REFERENCES courses(id)
);

INSERT INTO courses (name, faculty_name) VALUES ('Python' , 'Vinay'), ('AIML', 'John'), ('BootStrap', 'Merlin');

CREATE TABLE admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL
);
