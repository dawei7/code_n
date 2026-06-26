# Distinct Subsequences

| | |
|---|---|
| **ID** | `dp_29` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(M * N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) |

## Problemstellung

Gegeben sind zwei Strings `s` und `t`. Geben Sie die Anzahl der verschiedenen Teilfolgen (Subsequences) von `s` zurück, die `t` entsprechen.
Eine Teilfolge eines Strings ist ein neuer String, der aus dem ursprünglichen String durch das Löschen einiger (oder keiner) Zeichen gebildet wird, ohne die relative Position der verbleibenden Zeichen zu verändern.

**Eingabe:** Ein String `s` (die Quelle) und ein String `t` (das Ziel).
**Ausgabe:** Eine Ganzzahl, die die Anzahl der verschiedenen Teilfolgen darstellt.

## Wann man es verwendet

- Das klassische DP-Problem zum Zählen von Strings.
- Anstatt die *längste* Übereinstimmung (`LCS`) oder den *kürzesten* Editierpfad (`Edit Distance`) zu finden, suchen Sie hier die *Gesamtzahl der exakten Übereinstimmungen*.

## Ansatz

**1. Definition des Zustands:**
Sei `dp[i][j]` die Anzahl der verschiedenen Teilfolgen des Präfixes `s[0...i-1]`, die exakt dem Präfix `t[0...j-1]` entsprechen.
*(Hinweis: Eine 1-basierte Indizierung für Präfixe macht die Basisfälle deutlich übersichtlicher).*

**2. Bestimmung der Basisfälle:**
- `dp[i][0] = 1`: Wenn das Ziel `t` leer ist, gibt es genau 1 Möglichkeit, es aus JEDEM String `s` zu bilden: alles löschen!
- `dp[0][j] = 0` (für j > 0): Wenn die Quelle `s` leer ist, das Ziel `t` jedoch nicht, gibt es 0 Möglichkeiten, es zu bilden.

**3. Bestimmung des Übergangs (Die Rekurrenz):**
Wir vergleichen `s[i-1]` mit `t[j-1]`.
- **Fall A (Die Zeichen stimmen NICHT überein):**
  Wenn `s[i-1] != t[j-1]`, dann ist `s[i-1]` für den Aufbau unseres Ziels völlig nutzlos. Wir MÜSSEN es löschen! Die Anzahl der Möglichkeiten ist einfach die Anzahl der Möglichkeiten, die wir ohne dieses Zeichen hatten.
  `dp[i][j] = dp[i-1][j]`
- **Fall B (Die Zeichen stimmen überein):**
  Wenn `s[i-1] == t[j-1]`, haben wir tatsächlich eine WAHL!
  1. Wir können WÄHLEN, `s[i-1]` zu verwenden, um `t[j-1]` zu matchen. In diesem Fall muss der Rest des Ziels `t[0...j-2]` durch den Rest der Quelle `s[0...i-2]` gebildet werden. (Möglichkeiten: `dp[i-1][j-1]`).
  2. Wir können WÄHLEN, `s[i-1]` trotzdem zu ignorieren! Vielleicht gibt es später noch ein identisches Zeichen. Wir greifen auf die Möglichkeiten zurück, die wir ohne dieses Zeichen hatten. (Möglichkeiten: `dp[i-1][j]`).
  Daher ist die Gesamtzahl der Möglichkeiten die SUMME beider Wahlen!
  `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]`

**4. Platzoptimierung:**
Beachten Sie, dass Zeile `i` nur von Zeile `i-1` abhängt. Genau wie bei LCS können wir dies auf ein 1D-Array der Größe N (die Länge des Ziel-Strings `t`) reduzieren.
Da `dp[j]` jedoch von `dp[j-1]` aus der VORHERIGEN Zeile abhängt, müssen wir `j` RÜCKWÄRTS von rechts nach links iterieren, damit wir nicht versehentlich Daten überschreiben, die wir noch benötigen!

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

## Durchlauf

`s = "rabbbit"`, `t = "rabbit"`. M=7, N=6.
`dp` der Größe 7 wird initialisiert mit `[1, 0, 0, 0, 0, 0, 0]`.

1. **i = 1 ('r'):** matcht `t[0]`. `j=1`: `dp[1] += dp[0]` -> `dp[1] = 1`.
   `dp` = `[1, 1, 0, 0, 0, 0, 0]` ("r" matcht "r" einmal).
2. **i = 2 ('a'):** matcht `t[1]`. `j=2`: `dp[2] += dp[1]` -> `dp[2] = 1`.
   `dp` = `[1, 1, 1, 0, 0, 0, 0]` ("ra" matcht "ra" einmal).
3. **i = 3 ('b'):** matcht `t[2], t[3]`.
   - `j=4` ('b'): `dp[4] += dp[3] = 0`.
   - `j=3` ('b'): `dp[3] += dp[2] = 1`.
   `dp` = `[1, 1, 1, 1, 0, 0, 0]` ("rab" matcht "rab" einmal).
4. **i = 4 ('b'):** matcht `t[2], t[3]`.
   - `j=4` ('b'): `dp[4] += dp[3] = 1`.
   - `j=3` ('b'): `dp[3] += dp[2] = 1 + 1 = 2`.
   `dp` = `[1, 1, 1, 2, 1, 0, 0]` ("rabb" hat 2 Möglichkeiten, "rab" zu matchen, 1 Möglichkeit für "rabb").
5. **i = 5 ('b'):** matcht `t[2], t[3]`.
   - `j=4` ('b'): `dp[4] += dp[3] = 1 + 2 = 3`.
   - `j=3` ('b'): `dp[3] += dp[2] = 2 + 1 = 3`.
   `dp` = `[1, 1, 1, 3, 3, 0, 0]`.
6. **i = 6 ('i'):** matcht `t[4]`. `j=5`: `dp[5] += dp[4]` -> `dp[5] = 3`.
7. **i = 7 ('t'):** matcht `t[5]`. `j=6`: `dp[6] += dp[5]` -> `dp[6] = 3`.

Das Ergebnis `dp[6]` ist 3. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M * N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(M * N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(M * N)$ | $O(N)$ |

Die verschachtelten Schleifen laufen exakt M x N Mal durch und führen $O(1)$ Additionen aus. Die Zeitkomplexität ist $O(M \times N)$.
Die Platzkomplexität ist $O(N)$ (wobei N die Länge des kürzeren Ziel-Strings `t` ist).

## Varianten & Optimierungen

- **Rolling 1D-Array vs. 2D-Array:** Im Gegensatz zu LCS, wo man eine `temp`-Variable benötigt, um ein echtes 1D-Update zu simulieren, bleibt hier durch das Rückwärts-Iterieren von `j` der Wert `dp[j-1]` *natürlicherweise* erhalten! Es ist wohl die sauberste 1D-Optimierung unter allen 2D-String-Problemen.

## Anwendungen in der Praxis

- **Bioinformatik Sequenz-Alignment:** Berechnung der Multiplizität oder Wahrscheinlichkeit eines spezifischen Gen-Markers (das Ziel), der sich innerhalb einer stark mutierenden Eltern-DNA-Sequenz (die Quelle) bildet.

## Verwandte Algorithmen in cOde(n)

- **[dp_04 - Longest Common Subsequence](dp_04_longest-common-subsequence.md)** — Die grundlegende String-DP-Matrix, die auf `max()` anstatt auf der Summation `+` basiert.
- **[dp_03 - 0/1 Knapsack](dp_03_knapsack.md)** — Vermittelt den exakten Trick der Rückwärtsschleife, der hier verwendet wird, um ein Überschreiben des 1D-Zustands zu vermeiden.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*