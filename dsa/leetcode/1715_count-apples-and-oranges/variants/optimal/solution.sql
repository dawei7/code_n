SELECT
    SUM(boxes.apple_count + COALESCE(chests.apple_count, 0)) AS apple_count,
    SUM(boxes.orange_count + COALESCE(chests.orange_count, 0)) AS orange_count
FROM Boxes AS boxes
LEFT JOIN Chests AS chests
    ON boxes.chest_id = chests.chest_id;
