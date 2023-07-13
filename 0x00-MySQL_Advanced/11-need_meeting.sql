-- Introduction into view and how to use them

CREATE OR REPLACE VIEW need_meeting AS
    SELECT name FROM students
    WHERE score < 80
    AND (
        last_meeting IS NULL OR last_meeting <= DATE_SUB(CURDATE(), INTERVAL 1 MONTH));

