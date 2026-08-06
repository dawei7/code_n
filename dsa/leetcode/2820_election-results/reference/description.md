## Description

The `Votes` table records the candidates selected by each voter. Every voter owns one vote. A voter who selects several candidates divides that vote equally among all of those candidates, while a row whose candidate is `NULL` represents an abstention and contributes nothing.

Add the fractional contributions received by every candidate. Return every candidate whose total is the largest; a tie may therefore produce several rows. Sort the candidate names in ascending order.
