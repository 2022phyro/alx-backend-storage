-- Creating procedures. This procedure adds a score for a user to the project
DELIMITER $$ ;

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE avgScore FLOAT;
    SELECT AVG(score) INTO avgScore
    FROM corrections AS c WHERE c.user_id = user_id;
    UPDATE users
    SET average_score = avgScore WHERE id = user_id;
END $$
DELIMITER ; $$
