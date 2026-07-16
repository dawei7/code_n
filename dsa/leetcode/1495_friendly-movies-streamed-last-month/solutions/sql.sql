SELECT DISTINCT
    c.title
FROM Content AS c
INNER JOIN TVProgram AS p
    ON p.content_id = c.content_id
WHERE c.Kids_content = 'Y'
  AND c.content_type = 'Movies'
  AND p.program_date >= '2020-06-01'
  AND p.program_date < '2020-07-01'
ORDER BY c.title;

