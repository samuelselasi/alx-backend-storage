-- An SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
	BEGIN
		UPDATE users AS U,
			(SELECT U.id, SUM(score * weight) / SUM(weight) AS wei_avg
				FROM users AS U
				JOIN corrections AS C ON U.id = C.user_id
				JOIN projects AS P ON C.project_id = P.id	
				GROUP BY U.id)
			AS weighted_avg
		SET U.average_score = weighted_avg.wei_avg
		WHERE U.id = weighted_avg.id;
	END $$
