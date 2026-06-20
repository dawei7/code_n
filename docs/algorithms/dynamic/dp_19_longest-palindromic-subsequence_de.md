# Längste palindromische Teilfolge

| | |
|---|---|
| **ID** | `dp_19` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Längste palindromische Teilfolge](https://en.wikipedia.org/wiki/Longest_palindromic_subsequence) |

## Aufgabenstellung

Gegeben sei eine Zeichenkette `s`. Bestimme die Länge der längsten
**palindromischen Teilsequenz**. Eine Teilsequenz behält die Reihenfolge
der Elemente bei, muss jedoch nicht zusammenhängend sein.

**Eingabe:** eine Zeichenkette `s`.
**Ausgabe:** die Länge der längsten palindromischen Teilsequenz.

**Beispiel:**

| s | LPS | Länge |
|---|---|---:|
| `"bbbab"` | `"bbbb"` | 4 |
| `"cbbd"` | `"bb"` | 2 |
| `"a"` | `"a"` | 1 |
| `""` | `""` | 0 |
| `"racecar"` | `"racecar"` | 7 |
| `"abcda"` | `"a"` oder `"d"` | 1 |

## Wann man es verwendet

- Die Standard-DP für 2D-Zeichenketten. Die Reduktion auf **LCS** ist die
  elegante Erkenntnis: `LPS(s) = LCS(s, reverse(s))`.
- Grundlage für das schwierigere Problem des **längsten palindromischen
  Teilstrings** (`string_02`), das Kontiguität erfordert.

## Vorgehensweise

Zwei gleichwertige Ansätze.

### Ansatz A: 2D-DP auf `s`

Sei `dp[i][j]` = die Länge der längsten palindromischen
Teilfolge in der Teilzeichenfolge `s[i..j]` (einschließlich).

**Rekursionsbeziehung:**
- Wenn `s[i] == s[j]`: `dp[i][j] = dp[i+1][j-1] + 2`
  (das innere Palindrom um 2 verlängern).
  - Grenzfall: Wenn `i == j`, ist das einzelne Zeichen ein
    Palindrom der Länge 1, also `dp[i][i] = 1`.
  - Wenn `i+1 > j-1` (benachbart oder identisch), ist das „innere“
    leer, daher beträgt der Beitrag 2.
- Andernfalls: `dp[i][j] = max(dp[i+1][j], dp[i][j-1])` (
  eines der beiden Enden überspringen).

**Basisfall:** `dp[i][i] = 1` (einzelnes Zeichen).

**Antwort:** `dp[0][n-1]`.

**Iterationsreihenfolge:** `j - i` aufsteigend (längste Teilzeichenfolgen
zuletzt), sodass die inneren Teilprobleme zuerst berechnet werden.

### Ansatz B: Reduktion auf LCS

Die längste palindromische Teilfolge von `s` ist die **längste
gemeinsame Teilfolge** von `s` und `reverse(s)`. Gleiche $O(n²)$
Komplexität; die bestehende `dp_04`-Implementierung wird wiederverwendet.

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

## Schritt-für-Schritt-Anleitung

`s = "bbbab"`. Erwartet: 4.

`dp` ist 5×5.

Diagonale initialisieren: `dp[i][i] = 1`.

**Länge 2:** benachbarte Paare vergleichen.
- (0,1) „bb“: `s[0]=s[1]=b`, innerer Wert ist 0, also `dp[0][1] = 2`.
- (1,2) „bb“: ebenso, `dp[1][2] = 2`.
- (2,3) „ba“: `s[2]=b, s[3]=a`, keine Übereinstimmung, `dp[2][3] = max(dp[3][3], dp[2][2]) = max(1, 1) = 1`.
- (3,4) „ab“: keine Übereinstimmung, `dp[3][4] = max(dp[4][4], dp[3][3]) = 1`.

**Länge 3:**
- (0,2) „bbb“: `s[0]=s[2]=b`, innerer Wert `dp[1][1] = 1`, also `dp[0][2] = 1 + 2 = 3`.
- (1,3) „bba“: `s[1]=b, s[3]=a`, Fehlpaarung, `dp[1][3] = max(dp[2][3], dp[1][2]) = max(1, 2) = 2`.
- (2,4) „bab“: `s[2]=s[4]=b`, innerer `dp[3][3] = 1`, also `dp[2][4] = 1 + 2 = 3`.

**Länge 4:**
- (0,3) „bbba“: `s[0]=b, s[3]=a`, Fehlpaarung, `dp[0][3] = max(dp[1][3], dp[0][2]) = max(2, 3) = 3`.
- (1,4) „bbab“: `s[1]=b, s[4]=b`, inner `dp[2][3] = 1`, also `dp[1][4] = 1 + 2 = 3`.

**Länge 5:**
- (0,4) „bbbab“: `s[0]=b, s[4]=b`, inner `dp[1][3] = 2`, also `dp[0][4] = 2 + 2 = 4`.

`dp[0][4] = 4`. ✓ (LPS ist „bbbb“.)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestwert** | $O(n²)$ | $O(n²)$ |
| **Durchschnittlicher Fall** | $O(n²)$ | $O(n²)$ |
| **Schlechtester Fall** | $O(n²)$ | $O(n²)$ |

Standardmäßige 2D-DP. Der Ansatz der LCS-Reduktion hat dieselbe
Komplexität, nutzt jedoch eine bereits vorhandene Implementierung.

## Varianten & Optimierungen

- **Palindrom rekonstruieren** — von
  `dp[0][n-1]` zurück und wähle Übereinstimmungen gierig aus. $O(n)$ zusätzlicher Speicherplatz.
- **Längste palindromische Teilzeichenfolge** (`string_02`) — muss
  zusammenhängend sein. Verwende den Manacher-Algorithmus für $O(n)$ Zeit oder
  „Expand-around-center“ für $O(n²)$ Zeit und $O(1)$ Speicherplatz.
- **Anzahl der verschiedenen palindromischen Teilsequenzen** — passe die
  DP so an, dass gezählt statt maximiert wird.
- **Minimale Anzahl von Einfügungen, um ein Palindrom zu bilden** — gleiche DP,
  die Antwort lautet `n - dp[0][n-1]`.
- **Minimale Löschungen zur Bildung eines Palindroms** — ebenso.

## Anwendungen in der Praxis

- **DNA-Palindrome** — Viele Restriktionsenzyme erkennen
  palindromische DNA-Sequenzen. Das Auffinden der längsten palindromischen
  Teilsequenz hilft dabei, diese zu lokalisieren.
- **Musik / Palindromgedichte** — das Finden des längsten
  palindromischen Musters in einem Text.
- **Datenkompression** — palindromische Muster können
  mit Offset + Länge referenziert werden, was die Größe reduziert.
- **Codeanalyse** — das Auffinden von Palindromen im Quellcode
  zur Identifizierung von Refactoring-Möglichkeiten.
- **Kryptografie** — palindromische Chiffren und die
  Scytale-Chiffre basieren auf palindromischen Mustern.

## Verwandte Algorithmen in cOde(n)

- **[dp_04 — Längste gemeinsame Teilfolge](dp_04_lcs.md)** —
  die Äquivalenz zu `LPS(s) = LCS(s, reverse(s))`. (d=5/10, r=9/10)
- **[string_02 – Längste palindromische Teilzeichenfolge](string_02_longest-palindromic-substring.md)** —
  die zusammenhängende Variante. (d=5/10, r=7/10)
- **[dp_14 — Palindromische Partitionierung](dp_14_palindromic-partitioning.md)** —
  Partitionierung der Zeichenkette in Palindrome. (d=5/10, r=9/10)
- **[dp_24 — Palindromische Partitionierung (Minimale Schnitte)](dp_24_palindromic-partitioning-min-cuts.md)** —
  wie oben, jedoch unter Minimierung der Anzahl der Schnitte. (d=6/10, r=9/10)

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag
finden Sie über den Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
