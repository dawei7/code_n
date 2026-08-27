CREATE OR REPLACE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT)
RETURNS TABLE (user_id INT) AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT p.user_id
    FROM Purchases p
    WHERE p.amount >= minAmount 
      AND p.time_stamp >= startDate 
      AND p.time_stamp <= endDate
    ORDER BY p.user_id;
END;
$$ LANGUAGE plpgsql;
