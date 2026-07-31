SELECT e.left_operand,
       e.operator,
       e.right_operand,
       CASE
           WHEN e.operator = '<'
                AND left_variable.value < right_variable.value
               THEN 'true'
           WHEN e.operator = '>'
                AND left_variable.value > right_variable.value
               THEN 'true'
           WHEN e.operator = '='
                AND left_variable.value = right_variable.value
               THEN 'true'
           ELSE 'false'
       END AS value
FROM Expressions AS e
JOIN Variables AS left_variable
  ON left_variable.name = e.left_operand
JOIN Variables AS right_variable
  ON right_variable.name = e.right_operand
ORDER BY e.left_operand,
         e.operator,
         e.right_operand;
