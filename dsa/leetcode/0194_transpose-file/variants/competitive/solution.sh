#!/usr/bin/env bash
awk '
{
    if (NR == 1) columns = NF
    for (column = 1; column <= NF; column++) {
        if (NR == 1) output[column] = $column
        else output[column] = output[column] " " $column
    }
}
END {
    for (column = 1; column <= columns; column++) print output[column]
}
' file.txt
