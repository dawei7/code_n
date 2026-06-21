# Longest Increasing Subsequence ($O(n log n)$ Patience Sort)

| | |
|---|---|
| **ID** | `dp_29` |
| **Category** | dynamic_programming |
| **Complexity (required)** | $O(n log n)$ |
| **Difficulty** | 7/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Longest Increasing Subsequence (Optimal)](https://leetcode.com/problems/longest-increasing-subsequence/) |

## Problem statement

*(Dies ist eine fortgeschrittene Optimierung mittels binärer Suche von `dp_07_longest-increasing-subsequence`).*

Gegeben ist ein Array `nums` von Ganzzahlen. Geben Sie die Länge der längsten streng monoton steigenden Teilfolge zurück.

Der Standard-DP-Algorithmus (`dp_07`) löst dies in $O(n^2)$ Zeit, indem jedes Paar von Elementen verglichen wird. Können wir dies auf $O(n log n)$ optimieren?

## Wann ist dieser Ansatz zu verwenden?

- Zur Lösung des LIS-Problems, wenn die Array-Größe N bis zu 10^5 beträgt, da ein $O(n^2)$-Algorithmus hier zu einem Time Limit Exceeded (TLE)-Fehler führen würde.

## Ansatz

Wir können ein aktives `tails`-Array konstruieren.
`tails[i]` speichert das **kleinste** Endelement aller steigenden Teilfolgen der Länge `i+1`.

Warum das *kleinste* Endelement speichern?
Weil wir bei einer späteren Erweiterung der Teilfolge die bestmögliche Chance haben, eine Zahl zu finden, die größer als das Endelement ist, wenn dieses möglichst klein ist!

Während wir über das gegebene `nums`-Array iterieren, betrachten wir jedes `num`:
1. Wenn `num` größer ist als jedes Element, das sich aktuell in `tails` befindet, erweitert es unsere längste steigende Teilfolge natürlich um 1. Wir hängen es an das Ende von `tails` an.
2. Wenn `num` *nicht* das größte Element ist, kann es die längste Folge nicht erweitern. Es kann jedoch ein existierendes Endelement *ersetzen*, um ein günstigeres (kleineres) Endelement für eine Folge dieser spezifischen Länge zu erzeugen! Wir finden das erste Element in `tails`, das \ge `num` ist, und überschreiben es mit `num`.

**Die Magie:**
Da `tails` steigende Teilfolgen von streng zunehmenden Längen speichert, ist das `tails`-Array mathematisch garantiert zu jedem Zeitpunkt **streng aufsteigend sortiert**!
Da es sortiert ist, können wir das zu überschreibende Element mittels **binärer Suche** in $O(log n)$ Zeit finden!

*(Hinweis: Das `tails`-Array selbst ist NICHT die tatsächliche LIS-Folge! Es speichert lediglich die optimalen Endelemente. Die `length(tails)` entspricht jedoch exakt der Länge der LIS).*

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_29: LIS (Patience Sort).

Maintain a sorted tails array; binary-search to place each
value. O(n log n).
"""


def solve(arr, n):
    if n == 0:
        return 0
    import bisect
    tails = []
    for v in arr:
        idx = bisect.bisect_left(tails, v)
        if idx == len(tails):
            tails.append(v)
        else:
            tails[idx] = v
    return len(tails)
```

</details>

## Durchlauf

`nums = [4, 5, 6, 3]`. `tails = []`.

**num = 4:**
- Binäre Suche in `[]` ergibt `left = 0`.
- `4` anhängen. `tails = [4]`.

**num = 5:**
- BS in `[4]` ergibt `left = 1` (da 5 > 4).
- `5` anhängen. `tails = [4, 5]`.

**num = 6:**
- BS in `[4, 5]` ergibt `left = 2` (da 6 > 5).
- `6` anhängen. `tails = [4, 5, 6]`.

**num = 3:**
- BS in `[4, 5, 6]`. `3` ist kleiner als `4`. `left = 0`.
- Index 0 überschreiben. `tails = [3, 5, 6]`.
*(Beachten Sie, dass `[3, 5, 6]` keine gültige Teilfolge im ursprünglichen Array ist! Aber das spielt keine Rolle. Die Länge ist immer noch 3. Und falls wir später auf `[4, 5]` stoßen würden, erleichtert die `3` an Index 0 den Aufbau neuer Folgen).*

Ausgabe: `length(tails) = 3`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n log n)$ | $O(n)$ |
| **Durchschnittlicher Fall** | $O(n log n)$ | $O(n)$ |
| **Schlechtester Fall** | $O(n log n)$ | $O(n)$ |

Wir iterieren über n Elemente. Für jedes Element führen wir eine binäre Suche auf dem `tails`-Array durch, was $O(log n)$ Zeit in Anspruch nimmt. Die gesamte Zeitkomplexität beträgt somit streng $O(n log n)$.
Die Platzkomplexität beträgt $O(n)$ für das `tails`-Array.

## Varianten & Optimierungen

- **Patience Sorting:** Dieser Algorithmus ist mathematisch äquivalent zum Kartenspiel Patience. Man legt Karten auf Stapel, wobei eine Karte nur dann auf einen Stapel gelegt werden darf, wenn ihr Wert kleiner ist. Die Anzahl der gebildeten Stapel entspricht exakt der Länge der LIS!

## Anwendungen in der Praxis

- **Versionsverwaltungssysteme (Git):** Wird im `diff`-Algorithmus verwendet, um die längste gemeinsame Teilfolge (Longest Common Subsequence) von Zeilen zwischen zwei Dateien zu finden, indem das LCS-Problem in ein LIS-Problem transformiert wird!

## Verwandte Algorithmen in cOde(n)

- **[dp_07 - Longest Increasing Subsequence](dp_07_longest-increasing-subsequence.md)** — Der klassische $O(n^2)$ DP-Ansatz.
- **[search_03 - Binary Search](../searching/search_03_binary-search.md)** — Die $O(log n)$-Engine, die hier verwendet wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den enzyklopädischen Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*