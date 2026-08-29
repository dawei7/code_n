-- Write your PostgreSQL query statement below
SELECT DISTINCT title
FROM
    TVProgram
    JOIN Content USING (content_id)
WHERE
    TO_CHAR(program_date, 'YYYYMM') = '202006'
    AND kids_content = 'Y'
    AND content_type = 'Movies';
