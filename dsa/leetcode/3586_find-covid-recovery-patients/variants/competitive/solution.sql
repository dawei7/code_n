WITH first_positive AS (
    SELECT patient_id, MIN(test_date) AS positive_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
),
first_recovery AS (
    SELECT fp.patient_id,
           fp.positive_date,
           MIN(ct.test_date) AS negative_date
    FROM first_positive AS fp
    JOIN covid_tests AS ct
      ON ct.patient_id = fp.patient_id
     AND ct.result = 'Negative'
     AND ct.test_date > fp.positive_date
    GROUP BY fp.patient_id, fp.positive_date
)
SELECT p.patient_id,
       p.patient_name,
       p.age,
       CAST(julianday(fr.negative_date) - julianday(fr.positive_date) AS INTEGER) AS recovery_time
FROM first_recovery AS fr
JOIN patients AS p
  ON p.patient_id = fr.patient_id
ORDER BY recovery_time ASC, p.patient_name ASC;
