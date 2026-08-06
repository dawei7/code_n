#!/usr/bin/env bash
awk '
{
    if (NR == 1) columns = NF
    for (column = 1; column <= NF; column++) cells[NR, column] = $column
}
END {
    for (column = 1; column <= columns; column++) {
        for (row = 1; row <= NR; row++) {
            if (row > 1) printf " "
            printf "%s", cells[row, column]
        }
        print ""
    }
}
' file.txt
