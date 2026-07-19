DELETE duplicate
FROM Person AS duplicate
INNER JOIN Person AS keeper
    ON duplicate.email = keeper.email
   AND duplicate.id > keeper.id;
