-- Creating procedures. This procedure adds a score for a user to the project
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users,
    (SELECT users.id, SUM(score * weight) / SUM(weight)
    AS ave FROM users
    INNER JOIN corrections
        ON users.id = corrections.user_id
    INNER JOIN projects
        ON projects.id = corrections.project_id
    GROUP BY users.id) 
    AS weighted
    SET users.average_score = weighted.ave
    WHERE users.id = weighted.id;
END $$
DELIMITER ; $$
