SELECT c.candidate_id
FROM Candidates AS c
JOIN Rounds AS r
  ON r.interview_id = c.interview_id
WHERE c.years_of_exp >= 2
GROUP BY c.candidate_id
HAVING SUM(r.score) > 15
ORDER BY c.candidate_id;
