-- Creating procedures. This procedure adds a score for a user to the project
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE avgScore FLOAT;
    DECLARE t_score FLOAT;
    DECLARE t_weight FLOAT;
    DECLARE user_id INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE u_cursor CURSOR FOR
    SELECT id from users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN u_cursor;
    user_loop: LOOP
        FETCH u_cursor INTO user_id;

        -- Calculate total score
        SELECT SUM((corrections.score * projects.weight)) INTO t_score
        FROM corrections INNER JOIN projects
        ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        -- Calculate total weight
        SELECT SUM(projects.weight) INTO t_weight
        FROM corrections INNER JOIN projects
        ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        SET avgScore = t_score / t_weight;
        UPDATE users
        SET average_score = avgScore WHERE id = user_id;
        FETCH NEXT FROM u_cursor INTO user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;
    END LOOP user_loop;

    CLOSE u_cursor;
END $$
DELIMITER ; $$

