# Palindromische Partitionierung (Min-Schnitte)

| | |
|---|---|
| **ID** | `dp_24` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeitsgrad** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Palindrom](https://en.wikipedia.org/wiki/Palindrome) (Problemvariante) |

## Aufgabenstellung

Gegeben sei eine Zeichenkette `s`. Teile sie in Teilzeichenketten so auf, dass
**jede Teilzeichenkette ein Palindrom ist**. Minimiere die Anzahl der
Schnitte.

**Eingabe:** eine Zeichenkette `s`.
**Ausgabe:** die minimale Anzahl an Schnitten, um `s` in
Palindrome zu unterteilen.

**Beispiel:**

| s | Min. Schnitte | Unterteilung |
|---|---:|---|
| `"aab"` | 1 | `"aa" | "b"` |
| `"a"` | 0 | `"a"` |
| `"ab"` | 1 | `"a" | "b"` |
| `"abcba"` | 0 | `"abcba"` (bereits ein Palindrom) |
| `"ababbbabbababa"` | 3 | (eines von vielen) |

## Wann man es verwendet

- Die klassische 2D-String-DP zur **Partitionierung einer Zeichenkette in
  Palindrome**. Prüft, ob man das
  Teilproblem „Ist es ein Palindrom?“ und die Optimierung „Minimale Schnitte“ miteinander verketten kann.
- Grundlage für die **Batch-Textverarbeitung** (Suche nach palindromischen
  Sequenzen), **DNA-Palindrome** und **kombinatorische Generierung**
  (Zählung aller palindromischen Partitionen einer Zeichenkette).

## Vorgehensweise

Zweistufige dynamische Programmierung:

**Stufe 1: Palindrom-Teilstrings vorab berechnen.** Erstelle eine 2D-
Boolesche Tabelle `is_pal[i][j]` = Ist `s[i..j]` ein Palindrom?
- `is_pal[i][i] = True` (einzelnes Zeichen).
- `is_pal[i][j] = (s[i] == s[j]) and (j - i < 2 or is_pal[i+1][j-1])`.
- Iteriere `j - i` in aufsteigender Reihenfolge.

**Stufe 2: Minimale Schnitte.** `dp[i]` = minimale Schnitte für `s[0..i-1]`
(Länge `i`).
- `dp[0] = 0`.
- Für jedes `i` von `1` bis `n`:
  - Wenn `s[0..i-1]` selbst ein Palindrom ist: `dp[i] = 0`.
  - Andernfalls probiere jedes `j < i` aus, sodass `s[j..i-1]` ein
    Palindrom ist. `dp[i] = min(dp[j] + 1)` über alle derartigen `j`.

**Antwort:** `dp[n]`.

**Speicherplatzoptimierung (Stufe 1):** `is_pal[i][j]` hängt nur
von `is_pal[i+1][j-1]` ab, also durchlaufe `j - i` in aufsteigender Reihenfolge, und du
erhältst das „Inner-Cell-First“-Verhalten als Nebeneffekt.

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

## Schritt-für-Schritt-Anleitung

`s = "aab"`. Erwartet: 1.

**Stufe 1:**
- `is_pal[0][0] = T`, `is_pal[1][1] = T`, `is_pal[2][2] = T`.
- Länge 2: (0,1) „aa“: gleich, Länge 2, `is_pal[0][1] = T`. (1,2) „ab“: unterschiedlich, F.
- Länge 3: (0,2) „aab“: `a != b`, F.

`is_pal`:
```
       0  1  2
  0  [ T  T  F ]
  1  [ .  T  F ]
  2  [ .  .  T ]
```

**Stufe 2:**
- `dp[0] = 0`.
- `i=1`: `s[0..0] = "a"` ist ein Palindrom (is_pal[0][0]=T). `dp[1] = 0`.
- `i=2`: `s[0..1] = "aa"` ist ein Palindrom (is_pal[0][1]=T). `dp[2] = 0`.
- `i=3`: `s[0..2] = "aab"` ist kein Palindrom (is_pal[0][2]=F). Versuche j=0,1,2:
  - j=0: is_pal[0][2] = F. Überspringen.
  - j=1: is_pal[1][2] = F. Überspringen.
  - j=2: is_pal[2][2] = T. `dp[2] + 1 = 0 + 1 = 1`. `dp[3] = 1`.

Antwort: `dp[3] = 1`. ✓ (Partition: „aa“ | „b“.)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(n²)$ | $O(n²)$ |
| **Durchschnittlicher Fall** | $O(n²)$ | $O(n²)$ |
| **Schlechteste** | $O(n²)$ | $O(n²)$ |

Beide Phasen sind $O(n²)$. Der Speicherbedarf für die Palindromtabelle beträgt
$O(n²)$. Kann auf $O(n)$ reduziert werden, indem `is_pal[i][j]`
innerhalb von Phase 2 im laufenden Betrieb berechnet wird.

## Varianten & Optimierungen

- **Alle palindromischen Partitionen zählen** — Backtracking ausgehend von
  den Schnitten; im schlimmsten Fall exponentiell.
- **Minimale Schnitte für K verschiedene Palindrome** — Verallgemeinerung
  auf ein anderes Schnittziel.
- **Die tatsächliche Partition ausgeben** — Speichern der `j`, die
  das Minimum erreicht hat, und Rückverfolgung zur Rekonstruktion.
- **$O(n)$-Raumvariante** — Berechne Palindrome on the fly
  mit „Expand-around-Center“; verzichte auf die 2D-Tabelle.
- **Manachers Algorithmus** — Palindrome in
  $O(n)$ vorverarbeiten (anstelle von $O(n²)$); nützlich, wenn viele Abfragen
  Palindrom-Informationen benötigen.

## Anwendungen in der Praxis

- **Textverarbeitung** — Finde natürliche Trennstellen in einem
  palindromischen Dokument.
- **Bioinformatik** — Lokalisieren von palindromischen Teilsequenzen in der
  DNA für Restriktionsenzym-Schnittstellen.
- **Musik / palindromische Liedtexte** — Finde die beste
  palindromische Segmentierung einer Phrase.
- **Code-Formatierung** — Aufteilung einer langen Zeichenkette in palindromische
  visuelle Blöcke.
- **Komprimierung** — Palindrome eignen sich gut als
  Rückverweise bei der LZ-Komprimierung.

## Verwandte Algorithmen in cOde(n)

- **[dp_14 — Palindromische Partitionierung](dp_14_palindromic-partitioning.md)** —
  zählt alle Partitionen, minimiert nicht. (d=5/10, r=9/10)
- **[dp_19 – Längste palindromische Teilfolge](dp_19_longest-palindromic-subsequence.md)** —
  längstes einzelnes Palindrom, keine Partition. (d=5/10, r=9/10)
- **[string_02 — Längste palindromische Teilzeichenfolge](string_02_longest-palindromic-substring.md)** —
  die zusammenhängende Variante (ohne Lücken). (d=5/10, r=7/10)

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag
finden Sie über den Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
