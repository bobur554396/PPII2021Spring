-- CREATE DATABASE pp2demo;

-- CREATE USER pp2user with PASSWORD 'asdasdasd';

-- GRANT ALL PRIVILEGES ON DATABASE pp2demo TO pp2user;

-- DROP DATABASE pp2demo;

CREATE TABLE students (
  id      VARCHAR(10),
  name    VARCHAR(255),
  faculty VARCHAR(255),
  gpa     NUMERIC
);

-- Insert data
INSERT INTO students (id, name, faculty, gpa)
VALUES ('20BD001', 'Student 1', 'FIT', 3.9);

INSERT INTO students (id, name, faculty, gpa) VALUES
  ('20BD002', 'Student 2', 'FIT', 3.8),
  ('20BD003', 'Student 3', 'FIT', 3.5);


INSERT INTO students (id, name, faculty, gpa) VALUES
  ('20BD004', 'Student 4', 'FIT', 2.8),
  ('20BD005', 'Student 5', 'FIT', 3.1);

-- Select data

SELECT 2 + 5 * 10 - 7 AS result;

SELECT
  id,
  name,
  faculty,
  gpa
FROM students;

SELECT *
FROM students;

SELECT *
FROM students
WHERE gpa >= 3.1;

SELECT *
FROM students
WHERE gpa > 3.0 AND faculty = 'FIT';

SELECT *
FROM students
WHERE id = '20BD002';

SELECT *
FROM students
ORDER BY gpa ASC;

SELECT *
FROM students
ORDER BY gpa DESC;

SELECT *
FROM students
WHERE gpa > 3.0 AND faculty = 'FIT'
ORDER BY id DESC;


SELECT *
FROM students;

SELECT *
FROM students
WHERE name LIKE '%4';

SELECT *
FROM students
WHERE name LIKE 'Last%3';


SELECT *
FROM students
WHERE id = '20BD002' OR id = '20BD004' OR id = '20BD005';


SELECT *
FROM students
WHERE id IN ('20BD002', '20BD004', '20BD005');


SELECT *
FROM students
WHERE id NOT IN ('20BD002', '20BD004', '20BD005');


SELECT *
FROM students
WHERE gpa BETWEEN 3.0 AND 3.8;

-- Update data in tables

SELECT *
FROM students;

UPDATE students
SET faculty = 'FOGI'
WHERE id = '20BD002';

UPDATE students
SET faculty = 'FOGI', gpa = 3.9
WHERE id IN ('20BD004', '20BD005');

-- Delete items from tables
SELECT *
FROM students;

DELETE FROM students
WHERE id = '20BD002';

DELETE FROM students
WHERE gpa < 3.8;

-- DDL -- Data Definition Language (CREATE TABLE, ...)
-- DML -- Data Manipulation Language (INSERT, UPDATE, DELETE, ...)


SELECT *
FROM students
WHERE gpa > 3.5
LIMIT 2;

