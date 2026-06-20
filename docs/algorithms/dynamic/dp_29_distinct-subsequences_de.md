# Eindeutige Teilfolgen

| | |
|---|---|
| **ID** | `dp_29` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(M * N)$ Zeit, $O(N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Eindeutige Teilsequenzen](https://leetcode.com/problems/distinct-subsequences/) |

## Aufgabenstellung

Gegeben sind zwei Zeichenketten `s` und `t`. Gib die Anzahl der unterschiedlichen Teilfolgen von `s` zurück, die `t` entsprechen.
Eine Teilfolge einer Zeichenkette ist eine neue Zeichenkette, die aus der ursprünglichen Zeichenkette gebildet wird, indem einige (möglicherweise auch keine) Zeichen entfernt werden, ohne die relative Position der verbleibenden Zeichen zu verändern.

**Eingabe:** Eine Zeichenkette `s` (die Quelle) und eine Zeichenkette `t` (das Ziel).
**Ausgabe:** Eine ganze Zahl, die die Anzahl der verschiedenen Teilfolgen angibt.

## Wann man es verwendet

- Das klassische DP-Problem zum Zählen von Zeichenketten.
- Anstatt die *längste* Übereinstimmung (`LCS`) oder den *kürzesten* Bearbeitungspfad (`Edit Distance`) zu ermitteln, wird die *Gesamtzahl der exakten Übereinstimmungen* ermittelt.

## Vorgehensweise

**1. Definieren des Zustands:**
Sei `dp[i][j]` die Anzahl der verschiedenen Teilsequenzen des Präfixes `s[0...i-1]`, die perfekt mit dem Präfix `t[0...j-1]` übereinstimmen.
*(Hinweis: Eine 1-basierte Indizierung für Präfixe macht die Basisfälle wesentlich übersichtlicher).*

**2. Die Basisfälle ermitteln:**
- `dp[i][0] = 1`: Ist das Ziel `t` leer, gibt es genau eine Möglichkeit, es aus BELIEBIGER Zeichenkette `s` zu bilden: alles löschen!
- `dp[0][j] = 0` (für j > 0): Ist die Quelle `s` leer, das Ziel `t` jedoch nicht, gibt es 0 Möglichkeiten, sie zu bilden.

**3. Finde den Übergang (die Rekursionsbeziehung):**
Wir vergleichen `s[i-1]` mit `t[j-1]`.
- **Fall A (Die Zeichen stimmen NICHT überein):**
  Wenn `s[i-1] != t[j-1]`, dann ist `s[i-1]` für die Bildung unseres Ziels völlig nutzlos. Wir MÜSSEN es löschen! Die Anzahl der Möglichkeiten entspricht einfach der Anzahl der Möglichkeiten, die wir hatten, ohne dieses Zeichen zu verwenden.
  `dp[i][j] = dp[i-1][j]`
- **Fall B (Die Zeichen stimmen überein):**
  Wenn `s[i-1] == t[j-1]`, haben wir tatsächlich eine WAHL!
  1. Wir können uns ENTSCHEIDEN, `s[i-1]` zu verwenden, um `t[j-1]` abzugleichen. In diesem Fall muss der Rest des Ziels `t[0...j-2]` aus dem Rest der Quelle gebildet werden `s[0...i-2]` gebildet werden. (Möglichkeiten: `dp[i-1][j-1]`).
  2. Wir können uns ENTSCHEIDEN, `s[i-1]` trotzdem zu ignorieren! Vielleicht gibt es später noch ein weiteres identisches Zeichen. Wir greifen auf die Möglichkeiten zurück, die wir ohne dieses Zeichen hatten. (Möglichkeiten: `dp[i-1][j]`).
  Daher ist die Gesamtzahl der Möglichkeiten die SUMME beider Optionen!
  `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]`

**4. Speicherplatz optimieren:**
Beachte, dass die Zeile `i` nur von der Zeile `i-1` abhängt. Genau wie bei LCS können wir dies in ein eindimensionales Array der Größe N (die Länge der Zielzeichenfolge `t`) zusammenfassen.
Da `dp[j]` jedoch von `dp[j-1]` aus der VORHERIGEN Zeile abhängt, müssen wir `j` RÜCKWÄRTS von rechts nach links durchlaufen, damit wir nicht versehentlich benötigte Daten überschreiben!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_29: Distinct Subsequences.

dp[j] = number of distinct subsequences of s[0..i-1] that
match t[0..j-1]. Iterate s left-to-right; for each char
update dp right-to-left (like 0/1 knapsack) to avoid reuse.
"""


def solve(s, t, m, n):
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty target matches every prefix of s once
    for i in range(1, m + 1):
        for j in range(n, 0, -1):
            if s[i - 1] == t[j - 1]:
                dp[j] += dp[j - 1]
    return dp[n]
```

</details>

## Schritt-für-Schritt-Anleitung

`s = "rabbbit"`, `t = "rabbit"`. M=7, N=6.
`dp` Größe 7, initialisiert auf `[1, 0, 0, 0, 0, 0, 0]`.

1. **i = 1 („r“):** passt zu `t[0]`. `j=1`: `dp[1] += dp[0]` -> `dp[1] = 1`.
   `dp` = `[1, 1, 0, 0, 0, 0, 0]` („r“ passt einmal zu „r“).
2. **i = 2 („a“):** passt zu `t[1]`. `j=2`: `dp[2] += dp[1]` -> `dp[2] = 1`.
   `dp` = `[1, 1, 1, 0, 0, 0, 0]` („ra“ passt einmal zu „ra“).
3. **i = 3 („b“):** passt zu `t[2], t[3]`.
   - `j=4` („b“): `dp[4] += dp[3] = 0`.
   - `j=3` („b“): `dp[3] += dp[2] = 1`.
   `dp` = `[1, 1, 1, 1, 0, 0, 0]` („rab“ passt einmal zu „rab“).
4. **i = 4 ('b'):** entspricht `t[2], t[3]`.
   - `j=4` ('b'): `dp[4] += dp[3] = 1`.
   - `j=3` („b“): `dp[3] += dp[2] = 1 + 1 = 2`.
   `dp` = `[1, 1, 1, 2, 1, 0, 0]` („rabb“ passt auf zwei Arten zu „rab“ und auf eine Art zu „rabb“).
5. **i = 5 („b“):** passt zu `t[2], t[3]`.
   - `j=4` („b“): `dp[4] += dp[3] = 1 + 2 = 3`.
   - `j=3` („b“): `dp[3] += dp[2] = 2 + 1 = 3`.
   `dp` = `[1, 1, 1, 3, 3, 0, 0]`.
6. **i = 6 ('i'):** passt zu `t[4]`. `j=5`: `dp[5] += dp[4]` -> `dp[5] = 3`.
7. **i = 7 („t“):** entspricht `t[5]`. `j=6`: `dp[6] += dp[5]` -> `dp[6] = 3`.

Das Ergebnis `dp[6]` ist 3. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M * N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(M * N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(M * N)$ | $O(N)$ |

Die verschachtelten Schleifen laufen genau M × N Mal und führen $O(1)$ Additionen durch. Die Laufzeit beträgt $O(M \times N)$.
Der Speicherbedarf beträgt $O(N)$ (wobei N die Länge der kürzeren Zielzeichenfolge `t` ist).

## Varianten & Optimierungen

- **Rollendes 1D-Array vs. 2D-Array:** Im Gegensatz zu LCS, wo man eine `temp`-Variable benötigt, um eine echte 1D-Aktualisierung zu simulieren, bewahrt hier das *natürliche* Rückwärtsdurchlaufen von `j` rückwärts *von Natur aus* den Wert `dp[j-1]` erhalten bleibt! Dies ist wohl die sauberste 1D-Optimierung aller 2D-Zeichenfolgenprobleme.

## Anwendungen in der Praxis

- **Sequenzalignment in der Bioinformatik:** Berechnung der Multiplizität oder Wahrscheinlichkeit, mit der sich ein bestimmter Genmarker (das Ziel) innerhalb einer stark mutierenden elterlichen DNA-Sequenz (die Quelle) bildet.

## Verwandte Algorithmen in cOde(n)

- **[dp_04 – Längste gemeinsame Teilsequenz](dp_04_longest-common-subsequence.md)** — Die grundlegende Matrix für die dynamische Programmierung von Zeichenketten, die auf `max()` statt auf Summierung `+` basiert.
- **[dp_03 – 0/1-Rucksackproblem](dp_03_knapsack.md)** — Vermittelt den hier verwendeten Trick der exakten Rückwärtsschleife, um ein Überschreiben des 1D-Zustands zu vermeiden.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
