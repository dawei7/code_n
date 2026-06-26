# Palindromic Partitioning (Min Cuts)

| | |
|---|---|
| **ID** | `dp_24` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Palindrome](https://en.wikipedia.org/wiki/Palindrome) (Problemvariante) |

## Problemstellung

Gegeben ist ein String `s`. Zerlegen Sie diesen in Teilstrings, sodass **jeder Teilstring ein Palindrom ist**. Minimieren Sie die Anzahl der Schnitte.

**Eingabe:** ein String `s`.
**Ausgabe:** die minimale Anzahl an Schnitten, um `s` in Palindrome zu zerlegen.

**Beispiel:**

| s | Min cuts | Partitionierung |
|---|---:|---|
| `"aab"` | 1 | `"aa" | "b"` |
| `"a"` | 0 | `"a"` |
| `"ab"` | 1 | `"a" | "b"` |
| `"abcba"` | 0 | `"abcba"` (bereits ein Palindrom) |
| `"ababbbabbababa"` | 3 | (eine von vielen) |

## Wann man es verwendet

- Die klassische 2D-String-DP für die **Zerlegung eines Strings in Palindrome**. Testet, ob man das Teilproblem "ist Palindrom" mit der Optimierung "Min Cuts" verknüpfen kann.
- Grundlage für **Batch-Textverarbeitung** (Finden von palindromischen Sequenzen), **DNA-Palindrome** und **kombinatorische Generierung** (Zählen aller palindromischen Partitionen eines Strings).

## Ansatz

Zweistufige DP:

**Stufe 1: Vorberechnung der Palindrom-Teilstrings.** Erstellen Sie eine 2D-Boolean-Tabelle `is_pal[i][j]` = ist `s[i..j]` ein Palindrom?
- `is_pal[i][i] = True` (einzelnes Zeichen).
- `is_pal[i][j] = (s[i] == s[j]) and (j - i < 2 or is_pal[i+1][j-1])`.
- Iterieren Sie mit zunehmendem `j - i`.

**Stufe 2: Min Cuts.** `dp[i]` = minimale Schnitte für `s[0..i-1]` (Länge `i`).
- `dp[0] = 0`.
- Für jedes `i` von `1` bis `n`:
  - Wenn `s[0..i-1]` selbst ein Palindrom ist: `dp[i] = 0`.
  - Andernfalls versuchen Sie jedes `j < i`, sodass `s[j..i-1]` ein Palindrom ist. `dp[i] = min(dp[j] + 1)` über alle solchen `j`.

**Antwort:** `dp[n]`.

**Platzoptimierung (Stufe 1):** `is_pal[i][j]` hängt nur von `is_pal[i+1][j-1]` ab. Wenn Sie also mit zunehmendem `j - i` iterieren, erhalten Sie das Verhalten, bei dem die inneren Zellen zuerst berechnet werden, automatisch.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_24: Palindromic Partitioning (Min Cuts).

Return the minimum number of cuts to partition s into
palindromes. Precompute is_pal[i][j] (whether s[i..j] is a
palindrome) in O(n^2), then dp[i] = min over j with
is_pal[i][j] of (0 if j == n-1 else 1 + dp[j+1]).
"""


def solve(s, n):
    if n == 0:
        return 0
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                is_pal[i][j] = True
    INF = float("inf")
    dp = [INF] * (n + 1)
    dp[n] = 0
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if is_pal[i][j]:
                cost = 0 if j == n - 1 else 1 + dp[j + 1]
                if cost < dp[i]:
                    dp[i] = cost
    return dp[0]
```

</details>

## Durchlauf

`s = "aab"`. Erwartet: 1.

**Stufe 1:**
- `is_pal[0][0] = T`, `is_pal[1][1] = T`, `is_pal[2][2] = T`.
- Länge 2: (0,1) "aa": gleich, Länge 2, `is_pal[0][1] = T`. (1,2) "ab": verschieden, F.
- Länge 3: (0,2) "aab": `a != b`, F.

`is_pal`:
```
       0  1  2
  0  [ T  T  F ]
  1  [ .  T  F ]
  2  [ .  .  T ]
```

**Stufe 2:**
- `dp[0] = 0`.
- `i=1`: `s[0..0] = "a"` ist Palindrom (is_pal[0][0]=T). `dp[1] = 0`.
- `i=2`: `s[0..1] = "aa"` ist Palindrom (is_pal[0][1]=T). `dp[2] = 0`.
- `i=3`: `s[0..2] = "aab"` kein Palindrom (is_pal[0][2]=F). Versuche j=0,1,2:
  - j=0: is_pal[0][2] = F. Überspringen.
  - j=1: is_pal[1][2] = F. Überspringen.
  - j=2: is_pal[2][2] = T. `dp[2] + 1 = 0 + 1 = 1`. `dp[3] = 1`.

Antwort: `dp[3] = 1`. ✓ (Partitionierung: "aa" | "b".)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n²)$ | $O(n²)$ |
| **Durchschnittlicher Fall** | $O(n²)$ | $O(n²)$ |
| **Schlechtester Fall** | $O(n²)$ | $O(n²)$ |

Beide Stufen sind $O(n²)$. Der Platzbedarf für die Palindrom-Tabelle beträgt $O(n²)$. Dies kann auf $O(n)$ reduziert werden, indem `is_pal[i][j]` während der Laufzeit innerhalb von Stufe 2 berechnet wird.

## Varianten & Optimierungen

- **Alle palindromischen Partitionen zählen** — Backtracking von den Schnitten aus; exponentiell im schlechtesten Fall.
- **Min Cuts für K verschiedene Palindrome** — Verallgemeinerung auf ein anderes Schnitt-Ziel.
- **Die tatsächliche Partitionierung ausgeben** — Speichern Sie das `j`, das das Minimum erreicht hat, und gehen Sie den Weg zurück, um die Partitionierung zu rekonstruieren.
- **$O(n)$ Platz-Variante** — Berechnen Sie Palindrome während der Laufzeit mittels "Expand-around-center"; verzichten Sie auf die 2D-Tabelle.
- **Manacher-Algorithmus** — Vorverarbeitung von Palindromen in $O(n)$ (statt $O(n²)$); nützlich, wenn viele Anfragen Palindrom-Informationen benötigen.

## Anwendungen in der Praxis

- **Textverarbeitung** — Finden natürlicher Trennpunkte in einem palindromischen Dokument.
- **Bioinformatik** — Lokalisierung palindromischer Subsequenzen in DNA für Restriktionsenzym-Schnittstellen.
- **Musik / palindromische Liedtexte** — Finden der besten palindromischen Segmentierung einer Phrase.
- **Code-Formatierung** — Zerlegen eines langen Strings in palindromische visuelle Blöcke.
- **Kompression** — Palindrome sind gute Kandidaten für Rückwärtsreferenzen in der LZ-Kompression.

## Verwandte Algorithmen in cOde(n)

- **[dp_14 — Palindromic Partitioning](dp_14_palindromic-partitioning.md)** — zählt alle Partitionen, minimiert nicht. (d=5/10, r=9/10)
- **[dp_19 — Longest Palindromic Subsequence](dp_19_longest-palindromic-subsequence.md)** — längstes einzelnes Palindrom, keine Partitionierung. (d=5/10, r=9/10)
- **[string_02 — Longest Palindromic Substring](string_02_longest-palindromic-substring.md)** — die zusammenhängende Variante (keine Lücken). (d=5/10, r=7/10)

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*