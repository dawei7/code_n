## Description

A spell contains `n` focus points numbered from $0$ through $n-1$. Some focus points listed in `crystals` hold an energy source. Existing directed runes are described by corresponding entries of `flowFrom` and `flowTo`: magic can travel along each rune from `flowFrom[i]` to `flowTo[i]`.

A focus point can participate in the cast if it contains a crystal or can receive magic through a directed path originating at a crystal. Alice may add new directed runes between focus points. Added runes can extend the energized region further, just like the existing ones.

Return the minimum number of directed runes that must be added so every focus point becomes energized.
