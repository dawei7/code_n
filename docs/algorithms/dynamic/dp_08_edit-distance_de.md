# Edit Distance (Levenshtein)

| | |
|---|---|
| **ID** | `dp_08` |
| **Kategorie** | dynamic |
| **Komplexität (erfordert)** | $O(n²)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Edit distance](https://en.wikipedia.org/wiki/Edit_distance) |

## Problemstellung

Gegeben sind zwei Strings `s` und `t`. Finde die minimale Anzahl an **Einzelzeichen-Edits** (Einfügungen, Löschungen oder Ersetzungen), die erforderlich sind, um `s` in `t` umzuwandeln. Dies ist die **Levenshtein-Distanz**.

**Eingabe:** zwei Strings `s`, `t`.
**Ausgabe:** die minimale Anzahl an Edits.

**Beispiel:**

| s | t | Distanz | Eine Transformation |
|---|---|---:|---|
| "" | "abc" | 3 | 3× Einfügen |
| "abc" | "abc" | 0 | (identisch) |
| "kitten" | "sitting" | 3 | k→s, e→i, +g |
| "sunday" | "saturday" | 3 | +a, +t, n→r |
| "intention" | "execution" | 5 | i→e, n→x, e→c, +u, n→n (moment, 5) |

## Wann man es verwendet

- Das kanonische **2D-String-DP**-Problem und eines der am häufigsten gestellten Probleme bei FAANG-Interviews. Die Rekurrenz ist klein (drei Operationen), aber der Zustandsraum (s-Präfix × t-Präfix) ist 2D und man kann sich leicht vertun.
- Grundlage für **Rechtschreibprüfungen**, **Fuzzy-Suche**, **DNA-Sequenz-Alignment** (mit einer gewichteten Version derselben Rekurrenz) und **Autokorrektur** in Texteditoren.

## Ansatz

Sei `dp[i][j]` = die Edit-Distanz zwischen den ersten `i` Zeichen von `s` und den ersten `j` Zeichen von `t`.

**Rekurrenz:** Betrachte die letzten Zeichen `s[i-1]` und `t[j-1]`:
- Wenn sie übereinstimmen, gilt `dp[i][j] = dp[i-1][j-1]`. Es ist kein Edit erforderlich.
- Andernfalls nimm das **Minimum** aus drei Operationen:
  - **Ersetzen** von `s[i-1]` durch `t[j-1]`: `1 + dp[i-1][j-1]`
  - **Löschen** von `s[i-1]`: `1 + dp[i-1][j]`
  - **Einfügen** von `t[j-1]`: `1 + dp[i][j-1]`

**Basisfall:** `dp[0][j] = j` (füge j Zeichen ein) und `dp[i][0] = i` (lösche i Zeichen). Der leere String ist `j` Einfügungen von jedem String der Länge `j` entfernt.

**Antwort:** `dp[len(s)][len(t)]`.

**Platzoptimierung:** Die Rekurrenz verwendet nur die vorherige Zeile und die aktuelle Zeile, daher 2D → 2×(n+1) → mit einem kleinen Trick sogar 1×(n+1) (verwende eine `prev_row`-Variable). Die Engine von cOde(n) erwartet $O(n²)$ Zeit und akzeptiert entweder 2D- oder optimierten Speicher.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_08: Edit Distance.

Levenshtein distance via standard 2D DP.
"""


def solve(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]
```

</details>

## Durchlauf

`s = "cat"`, `t = "cars"`. Antwort: 1 (füge `s` ein).

```
        ""   c   a   r   s
  ""  [  0,  1,  2,  3,  4 ]
   c  [  1,  0,  1,  2,  3 ]
   a  [  2,  1,  0,  1,  2 ]
   t  [  3,  2,  1,  1,  1 ]
```

Durchlauf zum Füllen von `dp[1][1]` = edit("c", "c"):
`s[0] = t[0] = "c"`, also `dp[1][1] = dp[0][0] = 0`.

`dp[1][2]` = edit("c", "ca"): `c ≠ a`. Kandidaten:
- Ersetzen: `1 + dp[0][1] = 1 + 1 = 2`
- Löschen `c`: `1 + dp[0][2] = 1 + 2 = 3`
- Einfügen `a`: `1 + dp[1][1] = 1 + 0 = 1`
- `dp[1][2] = 1`.

`dp[3][4]` = edit("cat", "cars") = 1. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(m·n)$ | $O(min(m, n)$) mit Rolling-Array |
| **Durchschnittlicher Fall** | $O(m·n)$ | $O(min(m, n)$) mit Rolling-Array |
| **Schlechtester Fall** | $O(m·n)$ | $O(min(m, n)$) mit Rolling-Array |

Für die 2D-Tabelle beträgt der Platzbedarf $O(m·n)$. Die Rolling-Row-Version reduziert dies auf $O(n)$ (oder $O(min(m, n)$), je nachdem, was kleiner ist).

## Varianten & Optimierungen

- **Damerau-Levenshtein** — zählt auch Transpositionen benachbarter Zeichen als 1 Edit. Nützlich für die Rechtschreibprüfung (wobei "teh" ↔ "the" 1 Transposition ist, nicht 2 Ersetzungen).
- **Gewichtete Edit-Distanz** — unterschiedliche Kosten für jede Operation. DNA-Alignment verwendet dies (Substitutionsmatrix BLOSUM / PAM).
- **Hirschberg-Algorithmus** — $O(m·n)$ Zeit, $O(min(m, n)$) Platz, UND rekonstruiert die tatsächliche Sequenz der Edits. Verwendet Divide-and-Conquer + den Rolling-Row-Trick.
- **Myers' Bit-Parallel-Algorithmus** — $O((m·n)/w)$, wobei w die Wortgröße ist; mit w=64 effektiv $O(m·n/64)$. Der Standard für produktive Diff-Tools.

## Anwendungen in der Praxis

- **Rechtschreibprüfungen und Autokorrektur** — Vorschläge sind die Wörter im Wörterbuch mit der geringsten Edit-Distanz zur Eingabe des Benutzers.
- **Plagiatsprüfung** — eine hohe Edit-Distanz zwischen zwei Dokumenten deutet darauf hin, dass sie unabhängig voneinander erstellt wurden.
- **DNA-Sequenz-Alignment** — die gewichtete Version, mit Substitutionsmatrizen, die auf die Evolution abgestimmt sind.
- **fzf, ripgrep, ag** — Fuzzy-Finder verwenden die Edit-Distanz (oder verwandte Maße), um Treffer zu bewerten.
- **git diff** — im Kern das Edit-Distanz-Problem.

## Verwandte Algorithmen in cOde(n)

- **[dp_04 — Longest Common Subsequence](dp_04_longest-common-subsequence.md)** — verwandtes 2D-String-DP, aber Maximierung statt Minimierung. (d=5/10, r=9/10)
- **[dp_20 — Shortest Common Supersequence (Length)](dp_20_shortest-common-supersequence.md)** — baut direkt auf der LCS-Tabelle auf. (d=5/10, r=9/10)
- **[dp_14 — Palindromic Partitioning](dp_14_palindromic-partitioning.md)** — ein weiteres 2D-String-DP. (d=5/10, r=9/10)

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link oben auf der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*