# Longest Common Subsequence (LCS)

| | |
|---|---|
| **ID** | `dp_04` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Longest common subsequence problem](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem) |

## Problemstellung

Gegeben sind zwei Sequenzen `s` und `t`. Gesucht ist die Länge der **längsten gemeinsamen Teilsequenz** (Longest Common Subsequence, LCS). Eine Teilsequenz behält die relative Reihenfolge der Elemente bei, muss aber nicht zusammenhängend sein.

**Eingabe:** zwei Sequenzen (typischerweise Strings, funktioniert aber auch mit Arrays beliebiger vergleichbarer Typen).
**Ausgabe:** die Länge der LCS.

**Beispiel:**

| s | t | LCS | Länge |
|---|---|---|---:|
| `"abcde"` | `"ace"` | `"ace"` | 3 |
| `"AGGTAB"` | `"GXTXAYB"` | `"GTAB"` | 4 |
| `"abc"` | `"def"` | `""` | 0 |
| `"abc"` | `"abc"` | `"abc"` | 3 |
| `""` | `"anything"` | `""` | 0 |

## Anwendung

- Das am häufigsten abgefragte **2D-String-DP** (neben der Edit-Distanz).
  Die Rekursionsgleichung ist einfacher als bei der Edit-Distanz: Es handelt sich um ein "Max-und-Überspringen" anstelle eines "Min-und-drei-Optionen"-Problems.
- Grundlage für **Diff-Tools** (die LCS zweier Zeilen ist der gemeinsame Block), **Versionsverwaltung** (`git diff`), **Plagiatserkennung** und **Bioinformatik** (DNA-Alignment — wobei die gewichtete LCS die produktive Version darstellt).

## Ansatz

Sei `dp[i][j]` = die Länge der LCS der ersten `i` Zeichen von `s` und der ersten `j` Zeichen von `t`.

**Rekursionsgleichung:** Betrachte die letzten Zeichen `s[i-1]` und `t[j-1]`:
- Wenn sie übereinstimmen (`s[i-1] == t[j-1]`), verlängere die LCS um 1:
  `dp[i][j] = 1 + dp[i-1][j-1]`.
- Andernfalls wähle das Maximum aus dem Überspringen eines der beiden Zeichen:
  `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

**Induktionsanfang:** `dp[0][j] = dp[i][0] = 0` (eine der Sequenzen ist leer, daher ist die LCS leer).

**Antwort:** `dp[len(s)][len(t)]`.

**Rekonstruktion:** Um die tatsächliche LCS zu erhalten, gehe von `dp[m][n]` rückwärts: Wenn `s[i-1] == t[j-1]`, ist dies Teil der LCS, gehe diagonal zurück; andernfalls gehe zum größeren der beiden Nachbarn.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_04: Longest Common Subsequence.

DP table: dp[i][j] = LCS length of seq_a[:i] and seq_b[:j]. O(n*m)
time, O(n*m) space.
"""


def solve(seq_a, seq_b):
    m, n = len(seq_a), len(seq_b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq_a[i - 1] == seq_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

</details>

## Durchlauf

`s = "AGGTAB"`, `t = "GXTXAYB"`. Antwort: 4 (`"GTAB"`).

```
         ""  G  X  T  X  A  Y  B
   ""  [  0, 0, 0, 0, 0, 0, 0, 0 ]
    A  [  0, 0, 0, 0, 0, 1, 1, 1 ]
    G  [  0, 1, 1, 1, 1, 1, 1, 1 ]
    G  [  0, 1, 1, 1, 1, 1, 1, 1 ]
    T  [  0, 1, 1, 2, 2, 2, 2, 2 ]
    A  [  0, 1, 1, 2, 2, 3, 3, 3 ]
    B  [  0, 1, 1, 2, 2, 3, 3, 4 ]
```

`dp[6][7] = 4`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(m·n)$ | $O(m·n)$ — 2D-Tabelle; $O(min(m,n)$) mit Rolling-Array |
| **Durchschnittlicher Fall** | $O(m·n)$ | $O(m·n)$ |
| **Schlechtester Fall** | $O(m·n)$ | $O(m·n)$ |

Standard-DP. Die Rolling-Row-Version (nur die vorherige Zeile speichern) reduziert den Platzbedarf auf $O(n)$, verliert jedoch die Möglichkeit, die LCS ohne erneute Ausführung zu rekonstruieren.

## Varianten & Optimierungen

- **Hunt-Szymanski-Algorithmus** — $O((r + n)$ log n), wobei `r` die Anzahl der übereinstimmenden Paare ist. Schneller, wenn die Sequenzen sehr ähnlich sind (die meisten Zeichen stimmen überein).
- **Bit-parallele LCS** — $O(n · ⌈m/w⌉)$, wobei w die Wortgröße ist. Exzellent für kurzes s und langes t.
- **Diff mit zeilenweiser Granularität** — git, diff und ähnliche Tools arbeiten auf Zeilen- statt auf Zeichenebene und verwenden ein ähnliches DP (die "Patience Diff"-Variante ist in der Praxis sogar noch schneller).
- **Mehrfache LCS** — es kann viele LCSs derselben Länge geben. Um diese zu zählen: `count[i][j] = 0` wenn `s[i-1] != t[j-1]`, ansonsten `count[i][j] = count[i-1][j-1] + count[i-1][j] + count[i][j-1] - count[i-1][j-1]` (wobei darauf zu achten ist, Doppelzählungen zu vermeiden).

## Praxisanwendungen

- **Versionsverwaltung** — `git diff` und `git merge` finden die LCS, um unveränderte Bereiche zu identifizieren.
- **Bioinformatik** — DNA- und Protein-Sequenz-Alignment (die gewichtete Version).
- **Plagiatserkennung** — eine hohe LCS zwischen zwei Aufsätzen ist verdächtig.
- **Screen-Diff-Tools** — der Vim `diff`-Befehl verwendet einen LCS-basierten Algorithmus.
- **Fuzzy String Matching** — ein hohes LCS-Verhältnis ist ein Indikator für Ähnlichkeit.

## Verwandte Algorithmen in cOde(n)

- **[dp_08 — Edit Distance](dp_08_edit-distance.md)** — die Minimierungsversion derselben 2D-Tabellenstruktur. (d=5/10, r=9/10)
- **[dp_20 — Shortest Common Supersequence (Length)](dp_20_shortest-common-supersequence.md)** — Konstruktion der SCS unter Verwendung der LCS-Tabelle. (d=5/10, r=9/10)
- **[dp_19 — Longest Palindromic Subsequence](dp_19_longest-palindromic-subsequence.md)** — LCS eines Strings mit seiner Umkehrung. (d=5/10, r=9/10)

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*