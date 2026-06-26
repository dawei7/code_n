# Z-Algorithmus

| | |
|---|---|
| **ID** | `string_07` |
| **Kategorie** | Strings |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Interview-Relevanz** | 2/10 |
| **GeeksForGeeks-Äquivalent** | [Z algorithm (Linear time pattern searching Algorithm)](https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/) |

## Problemstellung

Gegeben sei ein String `S` der Länge N.
Konstruiere das Z-Array.
Das Z-Array ist ein Array der Länge N, bei dem das i-te Element die Länge des längsten Teilstrings speichert, der bei `S[i]` beginnt und gleichzeitig ein Präfix des Strings `S` ist.
Du musst dieses Array in linearer Zeit $O(N)$ erstellen.

**Eingabe:** Ein String `S`.
**Ausgabe:** Ein Integer-Array, das das Z-Array repräsentiert.

## Wann man ihn verwendet

- Zur Durchführung von String-Matching in $O(N+M)$ Zeit.
- Als konzeptionell einfachere Alternative zum gefürchteten KMP-Algorithmus. Während KMP das "längste echte Präfix, das auch ein Suffix ist" verfolgt, misst der Z-Algorithmus direkt: "Wie viel des Präfixes stimmt ab dieser Stelle überein?".

## Ansatz

**1. Die Definition des Z-Arrays:**
Für den String `S = "aabzaa"`.
- `Z[0] = 6` (Das Präfix stimmt vollständig mit sich selbst überein).
- `Z[1] = 1` (`"abzaa"` stimmt mit `"a"` überein).
- `Z[2] = 0` (`"bzaa"` stimmt nicht mit `"a"` überein).
- `Z[3] = 0` (`"zaa"` stimmt nicht mit `"a"` überein).
- `Z[4] = 2` (`"aa"` stimmt perfekt mit dem Präfix `"aa"` überein).
- `Z[5] = 1` (`"a"` stimmt mit `"a"` überein).

**2. Die Z-Box (Das Sliding Window bekannter Übereinstimmungen):**
Wenn wir das Array naiv berechnen (durch zeichenweisen Vergleich ab jedem Index i), benötigen wir $O(N^2)$ Zeit.
Um $O(N)$ zu erreichen, müssen wir redundante Vergleiche vermeiden.
Wir verwalten eine "Z-Box", die durch eine linke Grenze `L` und eine rechte Grenze `R` definiert ist. Diese Box repräsentiert den am weitesten rechts liegenden Teilstring, den wir bisher gefunden haben, der perfekt mit dem Präfix übereinstimmt.
Innerhalb dieser Box stimmt `S[L...R]` perfekt mit `S[0...(R-L)]` überein.

**3. Die drei Fälle:**
Während wir i von 1 bis N-1 iterieren:
- **Fall 1 (Außerhalb der Box):** `i > R`. Wir befinden uns in unbekanntem Terrain! Wir haben keine zwischengespeicherten Informationen. Wir vergleichen `S[i]` manuell mit `S[0]`, `S[i+1]` mit `S[1]` usw., bis eine Abweichung auftritt. Danach aktualisieren wir unsere Box: `L = i` und `R = i + matches - 1`.
- **Fall 2 (Innerhalb der Box, sicher):** `i <= R`. Da `S[L...R]` perfekt mit dem Präfix übereinstimmt, sind die Zeichen ab `i` identisch mit den Zeichen ab dem Index `k = i - L`. Wir können einfach `Z[k]` nachschlagen!
  Wenn `Z[k]` strikt kleiner ist als der verbleibende Platz in unserer Box (`R - i + 1`), dann WISSEN wir, dass die Übereinstimmung endet, bevor sie die Box verlässt! Wir setzen sofort `Z[i] = Z[k]` in $O(1)$ Zeit! Keine Vergleiche erforderlich!
- **Fall 3 (Innerhalb der Box, berührt den Rand):** `i <= R`, aber `Z[k] >= R - i + 1`. Unser zwischengespeicherter Wert besagt, dass die Übereinstimmung genau bis zum Rand unserer bekannten Box (oder darüber hinaus) reicht. Wir können sicher `Z[i] = R - i + 1` setzen, um alle Vergleiche innerhalb der Box zu überspringen! Wir müssen jedoch die Zeichen *außerhalb* der Box manuell prüfen, um zu sehen, wie weit die Übereinstimmung tatsächlich geht. Nach der Prüfung aktualisieren wir `L` und `R`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_07: Z-Algorithm.

Linear-time pattern matching.
"""


def solve(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    s = pattern + "$" + text
    z = [0] * len(s)
    l = 0
    r = 0
    for i in range(1, len(s)):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    offset = m + 1
    for i in range(offset, len(s)):
        if z[i] == m:
            return i - offset
    return -1
```

</details>

## Durchlauf

`S = "aabcaabxaaaz"`.

1. `i = 1`: `S[1] = 'a'`. Außerhalb der Box. Vergleiche `S[1]` mit `S[0]` ('a' == 'a'). `S[2] != S[1]`.
   - `Z[1] = 1`. Box ist `L=1, R=1`.
2. `i = 2`: `S[2] = 'b'`. Außerhalb der Box (`i > R`). Sofortige Abweichung.
   - `Z[2] = 0`. Box unverändert.
3. `i = 3`: `S[3] = 'c'`. Sofortige Abweichung. `Z[3] = 0`.
4. `i = 4`: `S[4] = 'a'`. Außerhalb der Box. Vergleiche `S[4]` mit `S[0]` ('a'=='a'), `S[5]` mit `S[1]` ('a'=='a'), `S[6]` mit `S[2]` ('b'=='b'), `S[7]` mit `S[3]` ('x'!='c').
   - `Z[4] = 3`. Box ist nun `L=4, R=6` (`"aab"`).
5. `i = 5`: `S[5] = 'a'`. Innerhalb der Box (`5 <= 6`)!
   - Entsprechender Index k = 5 - 4 = 1.
   - `Z[1]` ist `1`.
   - Verbleibender Platz in der Box ist R - i + 1 = 6 - 5 + 1 = 2.
   - `1 < 2`! (Fall 2: Sicher!).
   - Setze sofort `Z[5] = 1`. Keine Vergleiche! ✓
6. `i = 6`: `S[6] = 'b'`. Innerhalb der Box!
   - k = 6 - 4 = 2.
   - `Z[2]` ist `0`.
   - `0 < 1`. (Fall 2: Sicher!).
   - Setze sofort `Z[6] = 0`. ✓
7. `i = 7`: `S[7] = 'x'`. Außerhalb der Box...

Finales Array: `[0, 1, 0, 0, 3, 1, 0, 0, 2, 1, 1, 0]`.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Obwohl sich eine `while`-Schleife innerhalb der `for`-Schleife befindet, betrachte genau, was die `while`-Schleife tut: Sie erhöht `right` NUR, wenn eine erfolgreiche Zeichenübereinstimmung gefunden wird.
Sobald `right` erhöht wurde, geht es NIEMALS zurück! Es kann den String nur von `0` bis `N` durchlaufen.
Daher führt die innere `while`-Schleife über die gesamte äußere `for`-Schleife hinweg maximal insgesamt N Mal aus.
Die Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität ist $O(N)$, um das Integer-Z-Array zu speichern.

## Varianten & Optimierungen

- **String Matching (`string_13`):** Um dies für Pattern Matching zu verwenden (z. B. Suche nach `"dog"` in `"the dog ran"`), verkettet man sie einfach mit einem speziellen Trennzeichen: `"dogthe dog ran"`. Man berechnet das Z-Array. Jeder Index, an dem `Z[i] == len("dog")` gilt, ist eine perfekte Übereinstimmung des Musters im Text!

## Anwendungen in der Praxis

- **Bioinformatik:** Schnelles Mapping massiver DNA-Short-Reads auf ein Referenzgenom. Die Logik des Z-Algorithmus ist fundamental einfacher auf GPUs zu parallelisieren als KMP.

## Verwandte Algorithmen in cOde(n)

- **[string_03 - KMP Pattern Matching](string_03_kmp-string-matching.md)** — Die berühmte, aber etwas schwerer zu verstehende Alternative zum $O(N)$ String-Matching-Algorithmus.
- **[string_02 - Longest Palindromic Substring](string_02_longest-palindromic-substring.md)** — Manachers Algorithmus für Palindrome verwendet exakt dieselbe "Sliding Box"-Caching-Logik (Fälle 1, 2 und 3), um $O(N)$ Zeit zu erreichen!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*