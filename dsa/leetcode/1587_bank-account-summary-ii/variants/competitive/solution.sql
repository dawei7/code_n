SELECT
    users.name,
    SUM(transactions.amount) AS balance
FROM Users AS users
INNER JOIN Transactions AS transactions
  ON transactions.account = users.account
GROUP BY users.account, users.name
HAVING SUM(transactions.amount) > 10000;
