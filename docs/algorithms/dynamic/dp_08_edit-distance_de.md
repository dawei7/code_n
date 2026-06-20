# Editierabstand (Levenshtein)

| | |
|---|---|
| **ID** | `dp_08` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Bearbeitungsabstand](https://en.wikipedia.org/wiki/Edit_distance) |

## Aufgabenstellung

Gegeben seien zwei Zeichenketten `s` und `t`. Bestimme die minimale Anzahl von
**Ein-Zeichen-Änderungen** (Einfügungen, Löschungen oder
Ersetzungen), die erforderlich sind, um `s` in `t` umzuwandeln. Dies ist die
**Levenshtein-Distanz**.

**Eingabe:** zwei Zeichenketten `s`, `t`.
**Ausgabe:** die minimale Anzahl an Bearbeitungen.

**Beispiel:**

| s | t | Abstand | Eine Umwandlung |
|---|---|---:|---|
| "" | „abc“ | 3 | Einfügen × 3 |
| „abc“ | „abc“ | 0 | (identisch) |
| „kitten“ | „sitting“ | 3 | k→s, e→i, +g |
| „sunday“ | „saturday“ | 3 | +a, +t, n→r |
| „intention“ | „execution“ | 5 | i→e, n→x, e→c, +u, n→n (Wartezeit: 5) |

## Wann man es einsetzt

- Das klassische **2D-String-DP**-Problem und eine der am häufigsten
  gestellten Fragen bei Vorstellungsgesprächen auf FAANG-Ebene. Die Rekursion ist klein
  (drei Operationen), aber der Zustandsraum (s-Präfix × t-Präfix)
  ist zweidimensional und leicht zu verwechseln.
- Grundlage für **Rechtschreibprüfungen**, **Fuzzy-Suche**,
  **DNA-Sequenz-Alignment** (mit einer gewichteten Version
  derselben Rekursion) und **Autokorrektur** in Texteditoren.

## Vorgehensweise

Sei `dp[i][j]` = der Bearbeitungsabstand zwischen den ersten `i`
Zeichen von `s` und den ersten `j` Zeichen von `t`.

**Rekursion:** Betrachte die letzten Zeichen `s[i-1]` und
`t[j-1]`:
- Wenn sie übereinstimmen, `dp[i][j] = dp[i-1][j-1]`. Keine Bearbeitung erforderlich.
- Andernfalls wähle das **Minimum** aus drei Operationen:
  - **Ersetze** `s[i-1]` durch `t[j-1]`: `1 + dp[i-1][j-1]`
  - **Lösche** `s[i-1]`: `1 + dp[i-1][j]`
  - **Einfügen** von `t[j-1]`: `1 + dp[i][j-1]`

**Basisfall:** `dp[0][j] = j` (j Zeichen einfügen) und
`dp[i][0] = i` (i Zeichen löschen). Die leere Zeichenkette ist `j`
Einfügungen von jeder Zeichenkette der Länge `j` entfernt.

**Antwort:** `dp[len(s)][len(t)]`.

**Speicheroptimierung:** Die Rekursion verwendet nur die vorherige
Zeile und die aktuelle Zeile, also 2D → 2×(n+1) → mit einer kleinen Anpassung
sogar 1×(n+1) (Verwendung einer `prev_row`-Variablen). Die Engine von cOde(n)
erwartet eine Laufzeit von $O(n²)$ und akzeptiert entweder 2D oder optimierten Speicher.

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

## Schritt-für-Schritt-Anleitung

`s = "cat"`, `t = "cars"`. Antwort: 1 (füge `s` ein).

```
        ""   c   a   r   s
  ""  [  0,  1,  2,  3,  4 ]
   c  [  1,  0,  1,  2,  3 ]
   a  [  2,  1,  0,  1,  2 ]
   t  [  3,  2,  1,  1,  1 ]
```

Schritt-für-Schritt-Anleitung zum Ausfüllen von `dp[1][1]` = edit("c", "c"):
`s[0] = t[0] = "c"`, also `dp[1][1] = dp[0][0] = 0`.

`dp[1][2]` = edit("c", "ca"): `c ≠ a`. Möglichkeiten:
- Ersetzen: `1 + dp[0][1] = 1 + 1 = 2`
- Löschen `c`: `1 + dp[0][2] = 1 + 2 = 3`
- Einfügen `a`: `1 + dp[1][1] = 1 + 0 = 1`
- `dp[1][2] = 1`.

`dp[3][4]` = edit("cat", "cars") = 1. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(m·n)$ | $O(min(m, n)$) mit rollierendem |
| **Durchschnittlicher Fall** | $O(m·n)$ | $O(min(m, n)$) mit rollender Zeile |
| **Schlechtester Fall** | $O(m·n)$ | $O(min(m, n)$) mit rollender Zeile |

Für die 2D-Tabelle beträgt der Speicherplatz $O(m·n)$. Die Version mit rollender Zeile
reduziert sich auf $O(n)$ (oder $O(min(m, n)$), je nachdem, welcher Wert kleiner ist.

## Varianten & Optimierungen

- **Damerau-Levenshtein** – zählt auch Transpositionen
  benachbarter Zeichen als 1 Änderung. Nützlich für die Rechtschreibprüfung
  (wo „teh“ ↔ „the“ 1 Transposition ist, nicht 2 Substitutionen).
- **Gewichtete Bearbeitungsdistanz** — unterschiedliche Kosten für jede
  Operation. Dies wird beim DNA-Alignment verwendet (Ersetzungsmatrix
  BLOSUM / PAM).
- **Hirschberg-Algorithmus** — $O(m·n)$ Zeit, $O(min(m, n)$)
  Speicherplatz, UND rekonstruiert die tatsächliche Abfolge der Änderungen. Verwendet
  „Teile und herrsche“ + den „Rolling-Row“-Trick.
- **Bit-paralleler Algorithmus von Myers** — $O((m·n)$/w), wobei w die
  Wortgröße ist, wobei w=64 effektiv $O(m·n/64)$ entspricht. Der
  Standard für kommerzielle Diff-Tools.

## Praktische Anwendungen

- **Rechtschreibprüfungen und Autokorrektur** — Vorschläge sind die
  Wörter im Wörterbuch mit dem geringsten Bearbeitungsabstand zur
  Benutzereingabe.
- **Plagiatserkennung** — Ein hoher Bearbeitungsabstand zwischen zwei
  Dokumenten deutet darauf hin, dass sie unabhängig voneinander erstellt wurden.
- **DNA-Sequenzabgleich** — die gewichtete Version mit
  auf die Evolution abgestimmten Substitutionsmatrizen.
- **fzf, ripgrep, ag** — Fuzzy-Finder verwenden den Edit-Abstand (oder
  verwandte Maße), um Übereinstimmungen zu ordnen.
- **git diff** — im Kern das Problem des Edit-Abstands.

## Verwandte Algorithmen in cOde(n)

- **[dp_04 – Längste gemeinsame Teilsequenz](dp_04_longest-common-subsequence.md)** —
  verwandte 2D-Strings-DP, jedoch Maximierung statt
  Minimierung. (d=5/10, r=9/10)
- **[dp_20 — Kürzeste gemeinsame Supersequenz (Länge)](dp_20_shortest-common-supersequence.md)** —
  baut direkt auf der LCS-Tabelle auf. (d=5/10, r=9/10)
- **[dp_14 — Palindromische Partitionierung](dp_14_palindromic-partitioning.md)** —
  eine weitere 2D-Strings-DP. (d=5/10, r=9/10)

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag
finden Sie unter dem Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
