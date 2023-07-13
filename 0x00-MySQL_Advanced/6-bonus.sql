-- Creating procedures. This procedure adds a score for a user to the project
DELIMITER $$ ;

CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE existId INT;
    DECLARE curr INT;
    SELECT id INTO existId FROM projects WHERE name = project_name;
    IF existId IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET curr = LAST_INSERT_ID();
    ELSE
        SET curr = existId;
    END IF;
    INSERT INTO corrections (user_id, project_id, score) 
    VALUES(user_id, curr, score);
END $$
DELIMITER ; $$
