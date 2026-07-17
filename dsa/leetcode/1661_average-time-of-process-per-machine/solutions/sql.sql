SELECT
    starts.machine_id,
    ROUND(AVG(ends.timestamp - starts.timestamp), 3) AS processing_time
FROM Activity AS starts
INNER JOIN Activity AS ends
    ON ends.machine_id = starts.machine_id
   AND ends.process_id = starts.process_id
   AND ends.activity_type = 'end'
WHERE starts.activity_type = 'start'
GROUP BY starts.machine_id;
