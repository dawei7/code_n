SELECT
    metal.symbol AS metal,
    nonmetal.symbol AS nonmetal
FROM Elements AS metal
CROSS JOIN Elements AS nonmetal
WHERE metal.type = 'Metal'
  AND nonmetal.type = 'Nonmetal';
