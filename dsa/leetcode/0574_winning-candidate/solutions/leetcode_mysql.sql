SELECT
    candidate.Name
FROM Candidate AS candidate
JOIN Vote AS vote
    ON vote.CandidateId = candidate.id
GROUP BY candidate.id, candidate.Name
ORDER BY COUNT(*) DESC
LIMIT 1;

