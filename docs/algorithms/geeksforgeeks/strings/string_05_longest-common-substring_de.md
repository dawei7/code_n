# Longest Common Substring

| | |
|---|---|
| **ID** | `string_05` |
| **Kategorie** | strings |
| **Komplexität (erforderlich)** | $O(N * M)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) |

## Problemstellung

Gegeben sind zwei Strings `S1` und `S2`. Finde die Länge des **längsten gemeinsamen Teilstrings** (Longest Common Substring).
Ein Teilstring ist eine strikt *zusammenhängende* Zeichenfolge innerhalb eines Strings.

*(Hinweis: Nicht mit der Longest Common Subsequence zu verwechseln, bei der die Zeichen nicht zusammenhängend sein müssen).*

**Eingabe:** Zwei Strings `S1` und `S2`.
**Ausgabe:** Eine Ganzzahl, die die Länge des längsten gemeinsamen Teilstrings repräsentiert.

**Beispiel:**
`S1 = "ABCDGH"`, `S2 = "ACDGHR"`
Ausgabe: `4`. (Der längste gemeinsame Teilstring ist `"CDGH"`).

## Anwendung

- Ein klassisches Problem der dynamischen Programmierung in der Textverarbeitung.
- Wird bei der Plagiatserkennung verwendet, um identische Textblöcke zu finden.

## Ansatz

Wir können dieses Problem mit einer 2D-Tabelle für dynamische Programmierung lösen.
Sei `dp[i][j]` die Länge des längsten gemeinsamen Teilstrings, der **strikt an** `S1[i-1]` und `S2[j-1]` endet.

Wenn `S1[i-1] == S2[j-1]`, bedeutet dies, dass die Zeichen übereinstimmen! Der längste gemeinsame Teilstring, der an diesen beiden Zeichen endet, ist genau um `1` größer als der längste gemeinsame Teilstring, der an den unmittelbar vorangehenden Zeichen endet:
`dp[i][j] = dp[i-1][j-1] + 1`

Wenn `S1[i-1] != S2[j-1]`, stimmen die Zeichen nicht überein. Da ein Teilstring zusammenhängend sein muss, ist die Kette unterbrochen! Die Länge eines gemeinsamen Teilstrings, der exakt an dieser Stelle endet, ist null:
`dp[i][j] = 0`

Um den global längsten gemeinsamen Teilstring zu finden, führen wir einfach eine `max_len`-Variable und aktualisieren diese jedes Mal, wenn `dp[i][j]` berechnet wird.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_05: Longest Common Substring.

DP with a single rolling row. dp[i][j] = length of the longest
common suffix of s[:i] and t[:j].
"""


def solve(s, t):
    m, n = len(s), len(t)
    if m == 0 or n == 0:
        return 0
    prev = [0] * (n + 1)
    best = 0
    for i in range(1, m + 1):
        cur = [0] * (n + 1)
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prev = cur
    return best
```

</details>

## Durchlauf

`S1 = "ABCA"`, `S2 = "BC"`
`n = 4, m = 2`. `dp` ist 5x3.

**i = 1 ('A'):**
- `j = 1 ('B')`: 'A' != 'B' -> `dp[1][1] = 0`
- `j = 2 ('C')`: 'A' != 'C' -> `dp[1][2] = 0`

**i = 2 ('B'):**
- `j = 1 ('B')`: 'B' == 'B' -> `dp[2][1] = dp[1][0] + 1 = 1`. `max = 1`.
- `j = 2 ('C')`: 'B' != 'C' -> `dp[2][2] = 0`

**i = 3 ('C'):**
- `j = 1 ('B')`: 'C' != 'B' -> `dp[3][1] = 0`
- `j = 2 ('C')`: 'C' == 'C' -> `dp[3][2] = dp[2][1] + 1 = 1 + 1 = 2`. `max = 2`.

**i = 4 ('A'):**
- Überall keine Übereinstimmung.

Ausgabe: `2`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N * M)$ | $O(N * M)$ |
| **Durchschnittlicher Fall** | $O(N * M)$ | $O(N * M)$ |
| **Schlechtester Fall** | $O(N * M)$ | $O(N * M)$ |

Die verschachtelten Schleifen werden strikt N x M mal ausgeführt, wobei N und M die Längen der beiden Strings sind. Die Zeitkomplexität beträgt exakt $O(N \cdot M)$.
Die Platzkomplexität beträgt $O(N \cdot M)$, um das 2D-DP-Array zu speichern.

## Varianten & Optimierungen

- **Platzoptimierung $O(M)$:** Beachte, dass wir zur Berechnung der Zeile `i` nur die Zeile `i-1` betrachten müssen. Wir benötigen nicht die gesamte 2D-Matrix im Speicher! Wir können einfach zwei 1D-Arrays (`prev_row` und `curr_row`) der Größe M verwenden und zwischen ihnen abwechseln, was die Platzkomplexität auf $O(M)$ reduziert.
- **Suffix-Automat / Suffix-Baum $O(N + M)$:** Durch den Aufbau eines Suffix-Baums von `S1` und das Durchlaufen von `S2` durch diesen Baum kann das Problem in strikt linearer Zeit gelöst werden. Dies ist astronomisch schneller, aber die Datenstrukturen sind in einem Vorstellungsgespräch extrem komplex zu implementieren.

## Anwendungen in der Praxis

- **Datendeduplizierung:** Auffinden identischer Byte-Blöcke in Binärdateien, um diese durch Referenzierung auf einen einzigen gemeinsamen Speicherort zu komprimieren.

## Verwandte Algorithmen in cOde(n)

- **[dp_12 - Longest Common Subsequence](../dynamic/dp_12_lcs.md)** — Das verwandte DP-Problem, bei dem Lücken erlaubt sind. (Der einzige Unterschied besteht darin, dass bei einer Nicht-Übereinstimmung `max(dp[i-1][j], dp[i][j-1])` übernommen wird, anstatt auf `0` zurückzusetzen!)
- **[suffix_array_01 - Suffix Array](../suffix_array/suffix_array_01_construction.md)** — Die $O(N \log N)$ Datenstruktur, die dieses Problem ebenfalls in nahezu linearer Zeit unter Verwendung des Longest Common Prefix (LCP) Arrays lösen kann.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*