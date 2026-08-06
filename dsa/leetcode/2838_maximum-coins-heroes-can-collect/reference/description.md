## Description

A battle contains $n$ heroes and $m$ monsters. The positive integer `heroes[i]` is hero $i$'s power, while `monsters[j]` is monster $j$'s power. A hero can defeat a monster exactly when the monster's power is at most the hero's power.

Defeating monster $j$ awards `coins[j]` coins. A hero's health is not reduced by fighting, so that hero may defeat every monster they are powerful enough to beat. Different heroes may each defeat the same monster, but an individual hero receives that monster's reward only once. Return one total for every hero, preserving the heroes' original order, where each total is the maximum number of coins that hero can collect.
