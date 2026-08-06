## Description

The array `items` contains score records for different students. Each entry has the form `[ID_i, score_i]` and represents one score earned by the student identified by `ID_i`.

For every represented student, select that student's five highest recorded scores. Add those five values and divide their sum by `5` using integer division; this quotient is the student's top five average. Scores below the selected five do not contribute.

Return one pair `[ID_j, topFiveAverage_j]` for each student. Sort the result pairs by `ID_j` in increasing order.
