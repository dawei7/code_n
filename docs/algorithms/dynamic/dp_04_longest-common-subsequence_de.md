# Längste gemeinsame Teilfolge (LCS)

| | |
|---|---|
| **ID** | `dp_04` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Problem der längsten gemeinsamen Teilfolge](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem) |

## Aufgabenstellung

Gegeben sind zwei Sequenzen `s` und `t`. Bestimme die Länge der
**längsten Teilsequenz**, die beiden gemeinsam ist. Eine Teilsequenz behält
die relative Reihenfolge der Elemente bei, muss aber nicht
zusammenhängend sein.

**Eingabe:** zwei Sequenzen (typischerweise Zeichenketten, funktioniert aber auch mit
Arrays beliebiger vergleichbarer Typen).
**Ausgabe:** die Länge der LCS.

**Beispiel:**

| s | t | LCS | Länge |
|---|---|---|---:|
| `"abcde"` | `"ace"` | `"ace"` | 3 |
| `"AGGTAB"` | `"GXTXAYB"` | `"GTAB"` | 4 |
| `"abc"` | `"def"` | `""` | 0 |
| `"abc"` | `"abc"` | `"abc"` | 3 |
| `""` | `"anything"` | `""` | 0 |

## Wann man es verwendet

- Die am häufigsten gestellte Aufgabe zum **2D-String-DP** (zusammen mit der Editierdistanz).
  Die Rekursion ist einfacher als bei der Editierdistanz: Es handelt sich um ein
  „Max-and-Skip“-Verfahren statt um ein „Min-and-Three-Choices“-Verfahren.
- Grundlage für **Diff-Tools** (der LCS zweier Zeilen ist der
  gemeinsame Block), **Versionskontrolle** (`git diff`), **Plagiatserkennung**
  ** sowie **Bioinformatik** (DNA-Alignment – wobei
  der gewichtete LCS die Produktionsversion ist).

## Vorgehensweise

Sei `dp[i][j]` = die Länge des LCS der ersten `i`
Zeichen von `s` und der ersten `j` Zeichen von `t`.

**Rekursion:** Betrachte die letzten Zeichen `s[i-1]` und
`t[j-1]`:
- Wenn sie übereinstimmen (`s[i-1] == t[j-1]`), verlängere die LCS um 1:
  `dp[i][j] = 1 + dp[i-1][j-1]`.
- Andernfalls wähle die bessere der beiden Möglichkeiten, eines der Zeichen zu überspringen:
  `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

**Basisfall:** `dp[0][j] = dp[i][0] = 0` (eine der Sequenzen
ist leer, daher ist die LCS leer).

**Antwort:** `dp[len(s)][len(t)]`.

**Rekonstruktion:** Um die tatsächliche LCS zu erhalten, gehe von
`dp[m][n]` aus zurück: Wenn `s[i-1] == t[j-1]`, ist dies Teil der LCS,
gehe diagonal weiter; andernfalls gehe zum größeren der beiden
Nachbarn.

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
| **Bestfall** | $O(m·n)$ | $O(m·n)$ — 2D-Tabelle; $O(min(m,n)$) mit rollendem |
| **Durchschnittlicher Fall** | $O(m·n)$ | $O(m·n)$ |
| **Schlechtester Fall** | $O(m·n)$ | $O(m·n)$ |

Standard-DP. Die Version mit rollender Zeile (nur die vorherige
Zeile wird beibehalten) reduziert den Speicherbedarf auf $O(n)$, verliert jedoch die Möglichkeit,
die LCS ohne erneuten Durchlauf zu rekonstruieren.

## Varianten & Optimierungen

- **Hunt-Szymanski-Algorithmus** — $O((r + n)$ log n), wobei `r` die
  Anzahl der übereinstimmenden Paare ist. Schneller, wenn die Sequenzen
  sehr ähnlich sind (die meisten Zeichen stimmen überein).
- **Bit-parallele LCS** — $O(n · ⌈m/w⌉)$, wobei w die Wortgröße ist.
  Hervorragend geeignet für kurze s und lange t.
- **Diff mit Zeilengranularität** — git, diff und
  ähnliche Tools arbeiten auf Zeilenebene, nicht auf Zeichenebene, und verwenden eine
  ähnliche dynamische Programmierung (die „Patience-Diff“-Variante ist in der
  Praxis sogar noch schneller).
- **Mehrere LCS** — es kann viele LCS gleicher
  Länge geben. Um sie zu zählen: `count[i][j] = 0`, wenn `s[i-1] != t[j-1]`,
  sonst `count[i][j] = count[i-1][j-1] + count[i-1][j] + count[i][j-1] - count[i-1][j-1]` (wobei darauf zu achten ist, dass keine Doppelzählungen auftreten).

## Anwendungen in der Praxis

- **Versionskontrolle** — `git diff` und `git merge` finden LCS, um
  unveränderte Bereiche zu identifizieren.
- **Bioinformatik** — Alignment von DNA- und Proteinsequenzen
  (die gewichtete Variante).
- **Plagiatserkennung** — Ein hoher LCS-Wert zwischen zwei Aufsätzen ist
  verdächtig.
- **Screen-Diff-Tools** — Der Vim-Befehl `diff` verwendet einen
  LCS-basierten Algorithmus.
- **Fuzzy-String-Abgleich** — Ein hoher LCS-Wert ist ein Anzeichen für
  Ähnlichkeit.

## Verwandte Algorithmen in cOde(n)

- **[dp_08 — Edit Distance](dp_08_edit-distance.md)** —
  Minimierungsversion derselben 2D-Tabellenstruktur.
  (d=5/10, r=9/10)
- **[dp_20 — Kürzeste gemeinsame Supersequenz (Länge)](dp_20_shortest-common-supersequence.md)** —
  Erstellung der SCS mithilfe der LCS-Tabelle. (d=5/10, r=9/10)
- **[dp_19 — Längste palindromische Teilsequenz](dp_19_longest-palindromic-subsequence.md)** —
  LCS einer Zeichenkette mit ihrer Umkehrung. (d=5/10, r=9/10)

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag
finden Sie über den Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
