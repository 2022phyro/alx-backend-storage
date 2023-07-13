-- Creating procedures. This procedure adds a score for a user to the project
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE avgScore FLOAT;
    DECLARE t_score FLOAT;
    DECLARE t_weight FLOAT;
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
END $$
DELIMITER ; $$
