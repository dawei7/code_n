WITH RECURSIVE AllSubtasks AS (
    SELECT task_id, subtasks_count, 1 AS subtask_id
    FROM Tasks

    UNION ALL

    SELECT task_id, subtasks_count, subtask_id + 1
    FROM AllSubtasks
    WHERE subtask_id < subtasks_count
)
SELECT a.task_id, a.subtask_id
FROM AllSubtasks AS a
WHERE NOT EXISTS (
    SELECT 1
    FROM Executed AS e
    WHERE e.task_id = a.task_id
      AND e.subtask_id = a.subtask_id
)
ORDER BY a.task_id, a.subtask_id;
