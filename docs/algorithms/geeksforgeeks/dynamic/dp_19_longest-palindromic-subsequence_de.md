# Longest Palindromic Subsequence

| | |
|---|---|
| **ID** | `dp_19` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Longest palindromic subsequence](https://en.wikipedia.org/wiki/Longest_palindromic_subsequence) |

## Problemstellung

Gegeben sei ein String `s`. Finde die Länge der längsten **palindromischen Teilfolge** (Longest Palindromic Subsequence). Eine Teilfolge behält die Reihenfolge der Elemente bei, muss aber nicht zusammenhängend sein.

**Eingabe:** ein String `s`.
**Ausgabe:** die Länge der längsten palindromischen Teilfolge.

**Beispiel:**

| s | LPS | Länge |
|---|---|---:|
| `"bbbab"` | `"bbbb"` | 4 |
| `"cbbd"` | `"bb"` | 2 |
| `"a"` | `"a"` | 1 |
| `""` | `""` | 0 |
| `"racecar"` | `"racecar"` | 7 |
| `"abcda"` | `"a"` oder `"d"` | 1 |

## Anwendung

- Der Standard-2D-String-DP-Ansatz. Die Reduktion auf **LCS** ist die elegante Erkenntnis: `LPS(s) = LCS(s, reverse(s))`.
- Grundlage für das schwierigere Problem **Longest Palindromic Substring** (`string_02`), welches Zusammenhängigkeit erfordert.

## Ansatz

Zwei äquivalente Ansätze.

### Ansatz A: 2D DP auf `s`

Sei `dp[i][j]` = die Länge der längsten palindromischen Teilfolge im Teilstring `s[i..j]` (einschließlich).

**Rekurrenz:**
- Wenn `s[i] == s[j]`: `dp[i][j] = dp[i+1][j-1] + 2`
  (erweitere das innere Palindrom um 2).
  - Randfall: wenn `i == j`, ist das einzelne Zeichen ein Palindrom der Länge 1, also `dp[i][i] = 1`.
  - Wenn `i+1 > j-1` (benachbart oder identisch), ist das "Innere" leer, daher ist der Beitrag 2.
- Andernfalls: `dp[i][j] = max(dp[i+1][j], dp[i][j-1])` (überspringe eines der beiden Enden).

**Basis:** `dp[i][i] = 1` (einzelnes Zeichen).

**Antwort:** `dp[0][n-1]`.

**Iterationsreihenfolge:** `j - i` aufsteigend (längste Teilstrings zuletzt), sodass die inneren Teilprobleme zuerst berechnet werden.

### Ansatz B: Reduktion auf LCS

Die längste palindromische Teilfolge von `s` ist die **längste gemeinsame Teilfolge** (Longest Common Subsequence) von `s` und `reverse(s)`. Gleiche $O(n²)$ Komplexität; verwende die existierende `dp_04`-Implementierung wieder.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_19: Longest Palindromic Subsequence.

Classic DP: dp[i][j] = LPS length in s[i..j].
Base: dp[i][i] = 1. Recurrence: if s[i] == s[j],
dp[i][j] = dp[i+1][j-1] + 2; else dp[i][j] = max(dp[i+1][j], dp[i][j-1]).
"""


def solve(s, n):
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]
```

</details>

## Durchlauf

`s = "bbbab"`. Erwartet: 4.

`dp` ist 5x5.

Initialisiere Diagonale: `dp[i][i] = 1`.

**Länge 2:** Vergleiche benachbarte Paare.
- (0,1) "bb": `s[0]=s[1]=b`, Inneres ist 0, also `dp[0][1] = 2`.
- (1,2) "bb": gleich, `dp[1][2] = 2`.
- (2,3) "ba": `s[2]=b, s[3]=a`, kein Treffer, `dp[2][3] = max(dp[3][3], dp[2][2]) = max(1, 1) = 1`.
- (3,4) "ab": kein Treffer, `dp[3][4] = max(dp[4][4], dp[3][3]) = 1`.

**Länge 3:**
- (0,2) "bbb": `s[0]=s[2]=b`, Inneres `dp[1][1] = 1`, also `dp[0][2] = 1 + 2 = 3`.
- (1,3) "bba": `s[1]=b, s[3]=a`, kein Treffer, `dp[1][3] = max(dp[2][3], dp[1][2]) = max(1, 2) = 2`.
- (2,4) "bab": `s[2]=s[4]=b`, Inneres `dp[3][3] = 1`, also `dp[2][4] = 1 + 2 = 3`.

**Länge 4:**
- (0,3) "bbba": `s[0]=b, s[3]=a`, kein Treffer, `dp[0][3] = max(dp[1][3], dp[0][2]) = max(2, 3) = 3`.
- (1,4) "bbab": `s[1]=b, s[4]=b`, Inneres `dp[2][3] = 1`, also `dp[1][4] = 1 + 2 = 3`.

**Länge 5:**
- (0,4) "bbbab": `s[0]=b, s[4]=b`, Inneres `dp[1][3] = 2`, also `dp[0][4] = 2 + 2 = 4`.

`dp[0][4] = 4`. ✓ (LPS ist "bbbb".)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n²)$ | $O(n²)$ |
| **Durchschnittlicher Fall** | $O(n²)$ | $O(n²)$ |
| **Schlechtester Fall** | $O(n²)$ | $O(n²)$ |

Standard 2D DP. Der LCS-Reduktionsansatz hat die gleiche Komplexität, verwendet aber eine bestehende Implementierung wieder.

## Varianten & Optimierungen

- **Rekonstruktion des Palindroms** — gehe von `dp[0][n-1]` rückwärts und wähle Treffer gierig aus. $O(n)$ zusätzlicher Platz.
- **Longest Palindromic Substring** (`string_02`) — muss zusammenhängend sein. Verwende den Manacher-Algorithmus für $O(n)$ Zeit oder "Expand-around-center" für $O(n²)$ Zeit und $O(1)$ Platz.
- **Anzahl der verschiedenen palindromischen Teilfolgen zählen** — modifiziere die DP, um zu zählen statt zu maximieren.
- **Minimale Einfügungen für ein Palindrom** — gleiche DP, die Antwort ist `n - dp[0][n-1]`.
- **Minimale Löschungen für ein Palindrom** — identisch.

## Anwendungen in der Praxis

- **DNA-Palindrome** — viele Restriktionsenzyme erkennen palindromische DNA-Sequenzen. Das Finden der längsten palindromischen Teilfolge hilft bei deren Lokalisierung.
- **Musik / Palindrom-Gedichte** — Finden des längsten palindromischen Musters in einem Text.
- **Datenkompression** — palindromische Muster können mit Offset + Länge referenziert werden, was die Größe reduziert.
- **Code-Analyse** — Finden von Palindromen im Quellcode für Refactoring-Möglichkeiten.
- **Kryptographie** — palindromische Chiffren und die Skytale-Chiffre basieren auf palindromischen Mustern.

## Verwandte Algorithmen in cOde(n)

- **[dp_04 — Longest Common Subsequence](dp_04_lcs.md)** — die Äquivalenz `LPS(s) = LCS(s, reverse(s))`. (d=5/10, r=9/10)
- **[string_02 — Longest Palindromic Substring](string_02_longest-palindromic-substring.md)** — die zusammenhängende Variante. (d=5/10, r=7/10)
- **[dp_14 — Palindromic Partitioning](dp_14_palindromic-partitioning.md)** — Partitionierung des Strings in Palindrome. (d=5/10, r=9/10)
- **[dp_24 — Palindromic Partitioning (Min Cuts)](dp_24_palindromic-partitioning-min-cuts.md)** — dasselbe, aber minimiere die Anzahl der Schnitte. (d=6/10, r=9/10)

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*