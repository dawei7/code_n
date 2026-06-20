# Längste aufsteigende Teilfolge ($O(n log n)$ Patience-Sort)

| | |
|---|---|
| **ID** | `dp_29` |
| **Kategorie** | dynamische_Programmierung |
| **Komplexität (erforderlich)** | $O(n log n)$ |
| **Schwierigkeitsgrad** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Längste monoton steigende Teilfolge (optimal)](https://leetcode.com/problems/longest-increasing-subsequence/) |

## Aufgabenstellung

*(Dies ist eine fortgeschrittene Optimierung von `dp_07_longest-increasing-subsequence` mittels binärer Suche.)*

Gegeben sei ein Array aus ganzen Zahlen `nums`. Gib die Länge der längsten streng monoton wachsenden Teilfolge zurück.

Der Standard-DP-Algorithmus (`dp_07`) löst dies in $O(n^2)$ Zeit, indem er jedes Elementpaar vergleicht. Können wir dies auf $O(n log n)$ optimieren?

## Wann sollte man es verwenden?

- Zur Lösung von LIS, wenn die Array-Größe N bis zu 10^5 beträgt, wobei ein $O(n^2)$-Algorithmus zu einem „Time Limit Exceeded“ (TLE)-Fehler führen würde.

## Vorgehensweise

Wir können ein aktives „Tails“-Array aufbauen.
`tails[i]` speichert das **kleinste** Endelement aller aufsteigenden Teilfolgen der Länge `i+1`.

Warum das *kleinste* Endelement behalten? 
Weil wir, wenn wir eine Teilfolge später verlängern wollen, mit einem kleineren Endelement die bestmögliche Chance haben, eine Zahl zu finden, die größer ist als dieses!

Während wir das gegebene Array `nums` durchlaufen, betrachten wir jedes `num`:
1. Ist `num` größer als jedes Element, das sich derzeit in `tails` befindet, verlängert es natürlich unsere längste aufsteigende Teilfolge um 1. Wir fügen es an das Ende von `tails` an.
2. Wenn `num` *nicht* das größte Element ist, kann es die längste Teilfolge nicht verlängern. Es kann jedoch einen bestehenden Schluss *ersetzen*, um einen günstigeren (kleineren) Schluss für eine Teilfolge dieser spezifischen Länge zu schaffen! Wir suchen das erste Element in `tails`, das \ge `num` ist, und überschreiben es mit `num`.

**Der Clou:**
Da `tails` aufsteigende Teilsequenzen mit streng aufsteigenden Längen speichert, ist mathematisch garantiert, dass das Array `tails` zu jedem Zeitpunkt **streng in aufsteigender Reihenfolge sortiert** ist!
Da es sortiert ist, können wir das zu überschreibende Element mithilfe der **binären Suche** in $O(log n)$-Zeit finden!

*(Hinweis: Das Array `tails` selbst ist NICHT die eigentliche LIS-Sequenz! Es speichert lediglich die optimalen Endsequenzen. Allerdings entspricht `length(tails)` genau der Länge der LIS).*

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

## Schritt-für-Schritt-Anleitung

`nums = [4, 5, 6, 3]`. `tails = []`.

**num = 4:**
- Die binäre Suche in `[]` ergibt `left = 0`.
- `4` anhängen. `tails = [4]`.

**num = 5:**
- Die binäre Suche in `[4]` ergibt `left = 1` (da 5 > 4).
- Anfügen von `5`. `tails = [4, 5]`.

**num = 6:**
- Die binäre Suche in `[4, 5]` ergibt `left = 2` (da 6 > 5).
- `6` anhängen. `tails = [4, 5, 6]`.

**num = 3:**
- BS in `[4, 5, 6]`. `3` ist kleiner als `4`. `left = 0`.
- Index 0 überschreiben. `tails = [3, 5, 6]`.
*(Beachte, dass `[3, 5, 6]` keine gültige Teilfolge im ursprünglichen Array ist! Das spielt jedoch keine Rolle. Die Länge beträgt weiterhin 3. Und sollten wir später auf `[4, 5]` stoßen, erleichtert es die Bildung neuer Teilfolgen, wenn `3` am Index 0 steht).*

Ausgabe: `length(tails) = 3`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n log n)$ | $O(n)$ |
| **Durchschnittlicher Fall** | $O(n log n)$ | $O(n)$ |
| **Schlechtester Fall** | $O(n log n)$ | $O(n)$ |

Wir durchlaufen n Elemente. Für jedes Element führen wir eine binäre Suche im Array `tails` durch, was $O(log n)$ Zeit in Anspruch nimmt. Die gesamte Zeitkomplexität beträgt streng $O(n log n)$.
Die Platzkomplexität beträgt $O(n)$ für das `tails`-Array.

## Varianten & Optimierungen

- **Patience-Sortierung:** Dieser Algorithmus entspricht mathematisch dem Kartenspiel „Patience“. Man legt Karten auf Stack, wobei eine Karte nur dann auf einen Stack gelegt werden darf, wenn ihr Wert kleiner ist. Die Anzahl der gebildeten Stack entspricht genau der Länge der LIS!

## Anwendungen in der Praxis

- **Versionskontrollsysteme (Git):** Wird im `diff`-Algorithmus verwendet, um die längste gemeinsame Teilfolge von Zeilen zwischen zwei Dateien zu finden, indem das LCS-Problem in ein LIS-Problem umgewandelt wird!

## Verwandte Algorithmen in cOde(n)

- **[dp_07 – Längste aufsteigende Teilfolge](dp_07_longest-increasing-subsequence.md)** — Der klassische $O(n^2)$ DP-Ansatz.
- **[search_03 – Binäre Suche](../searching/search_03_binary-search.md)** – Die hier verwendete $O(log n)$-Engine.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
