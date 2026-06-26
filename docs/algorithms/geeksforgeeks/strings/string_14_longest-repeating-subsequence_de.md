# Longest Repeating Subsequence

| | |
|---|---|
| **ID** | `string_14` |
| **Kategorie** | strings |
| **Komplexität (erforderlich)** | $O(N^2)$ Zeit, $O(N^2)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **GeeksForGeeks Äquivalent** | [Longest Repeating Subsequence](https://www.geeksforgeeks.org/longest-repeating-subsequence/) |

## Problemstellung

Gegeben ist ein String `s`. Finde die Länge der längsten sich wiederholenden **Subsequence** (Teilfolge), sodass die beiden Subsequences nicht dasselbe Zeichen an derselben Position enthalten.
(D. h.: Die identischen Zeichen in den beiden Subsequences müssen von unterschiedlichen Indizes im ursprünglichen String stammen.)

**Eingabe:** Ein String `s`.
**Ausgabe:** Eine Ganzzahl, die die Länge repräsentiert.

## Wann man es verwendet

- Ein klassisches 2D Dynamic Programming Problem für Strings.
- Es ist eine direkte, geniale Modifikation des grundlegenden **Longest Common Subsequence (LCS)** Algorithmus. Wenn man LCS kennt, kennt man auch dies!

## Ansatz

**1. Die "Selbstvergleichs"-Erkenntnis:**
Beim Standardproblem der Longest Common Subsequence (LCS) erhält man `str1` und `str2`. Man findet die längste Sequenz von Zeichen, die in beiden Strings in der gleichen Reihenfolge existieren.
Was passiert, wenn wir LCS auf dem EXAKT GLEICHEN STRING ausführen? `LCS(s, s)`?
Die Antwort wäre einfach der gesamte String! Jedes Zeichen stimmt perfekt mit sich selbst überein! `s[i] == s[i]`.

**2. Die Modifikation für "unterschiedliche Indizes":**
Das Problem verlangt eine sich wiederholende Subsequence, bei der die Zeichen von *unterschiedlichen Indizes* stammen.
Also führen wir weiterhin `LCS(s, s)` aus. ABER wir fügen eine kleine, entscheidende Bedingung hinzu:
Wenn wir `s[i]` mit `s[j]` vergleichen, dürfen sie nur dann "übereinstimmen" und die Sequenzlänge erhöhen, WENN `s[i] == s[j]` **UND** `i != j`!
Wenn `i == j` gilt, betrachten wir exakt dasselbe physische Zeichen im ursprünglichen String. Wir behandeln dies als Nichtübereinstimmung!

**3. Die DP-Tabelle:**
Wir erstellen eine N+1 x N+1 DP-Matrix.
- `dp[i][j]` repräsentiert die Länge der Longest Repeating Subsequence zwischen dem Präfix `s[0...i-1]` und `s[0...j-1]`.
- Wenn `s[i-1] == s[j-1]` UND `i != j`: Wir haben ein gültiges sich wiederholendes Zeichen gefunden! `dp[i][j] = 1 + dp[i-1][j-1]`.
- Andernfalls: Wir nehmen das Maximum aus dem Überspringen eines Zeichens von einem der beiden Präfixe! `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_14: Longest Repeating Subsequence.

dp[i][j] = LRS length of s[i..] and s[j..] (with i != j).
"""


def solve(s, n):
    if n == 0:
        return 0
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == s[j] and i != j:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]
```

</details>

## Durchlauf

`s = "AABEBCDD"`
`N = 8`.

1. **`i=1` ('A'), `j=1` ('A'):** Übereinstimmung, aber `i == j`. Als Nichtübereinstimmung behandeln. `dp[1][1] = 0`.
2. **`i=1` ('A'), `j=2` ('A'):** Übereinstimmung! UND `i != j` (1 != 2).
   - `dp[1][2] = 1 + dp[0][1] = 1 + 0 = 1`.
...
Nachdem die gesamte Tabelle gefüllt ist, waren die Übereinstimmungen, die `1 + dp[i-1][j-1]` ausgelöst haben:
- 'A' an Index 0 und 'A' an Index 1.
- 'B' an Index 2 und 'B' an Index 4.
- 'D' an Index 6 und 'D' an Index 7.
Die längste Sequenz dieser Übereinstimmungen ohne sich zu überschneiden ist `"ABD"`.
`dp[8][8] = 3`. ✓

*(Die sich wiederholende Subsequence ist "ABD". Die erste verwendet die Indizes `0, 2, 6`. Die zweite verwendet die Indizes `1, 4, 7`.)*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^2)$ | $O(N^2)$ |
| **Durchschnittlicher Fall** | $O(N^2)$ | $O(N^2)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(N^2)$ |

Wir iterieren durch eine N x N Matrix. Jede Zelle benötigt $O(1)$ konstante Zeit zur Auswertung.
Die Zeitkomplexität ist strikt $O(N^2)$.
Die Platzkomplexität beträgt $O(N^2)$, um die DP-Tabelle zu speichern.

## Varianten & Optimierungen

- **Platzoptimierung $O(N)$:** Beachte in der Übergangsformel `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`, dass wir immer nur die AKTUELLE Zeile `i` und die VORHERIGE Zeile `i-1` betrachten. Wir benötigen nicht die gesamte Matrix im Speicher! Wir können einfach zwei Arrays beibehalten: `prev_row` und `curr_row`. Dies reduziert die Platzkomplexität sofort auf $O(N)$!
- **Ausgabe der Subsequence:** Wenn das Problem verlangt, tatsächlich den String `"ABD"` anstelle von nur `3` zurückzugeben, beginnt man bei `dp[n][n]` und verfolgt den Weg rückwärts. Wenn `dp[i][j] == dp[i-1][j-1] + 1`, fügt man `s[i-1]` zum String hinzu und bewegt sich diagonal nach oben links. Andernfalls bewegt man sich zum Maximum von `(i-1, j)` oder `(i, j-1)`. Den finalen String umkehren!

## Anwendungen in der Praxis

- **Datenkompressionsanalyse:** Auffinden intrinsischer Muster und weitreichender Redundanzen innerhalb eines einzelnen Datenstroms (wie einer Audiodatei), um maßgeschneiderte wörterbuchbasierte Kompressionsalgorithmen (wie LZ77/LZ78) zu entwerfen.

## Verwandte Algorithmen in cOde(n)

- **[dynamic_01 - Longest Common Subsequence](../dynamic/dp_01_longest-common-subsequence.md)** — Der grundlegende Algorithmus, auf dem dieses gesamte Problem aufbaut.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*