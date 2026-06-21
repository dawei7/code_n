# Sqrt(x) (Floor Square Root)

| | |
|---|---|
| **ID** | `dc_10` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(\log N)$ Time, $O(1)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) |

## Problem statement

Gegeben ist eine nicht-negative Ganzzahl `x`. Berechnen und zurückgeben Sie die Quadratwurzel von `x`.
Da der Rückgabetyp eine Ganzzahl ist, werden die Dezimalstellen abgeschnitten und nur der ganzzahlige Teil des Ergebnisses zurückgegeben.
Es ist nicht gestattet, eingebaute Exponentenfunktionen oder Operatoren wie `pow(x, 0.5)` oder `x ** 0.5` zu verwenden.

**Input:** Eine nicht-negative Ganzzahl `x`.
**Output:** Eine Ganzzahl, die den abgerundeten Wert (Floor) der Quadratwurzel darstellt.

## Wann man es verwendet

- Um zu beweisen, dass man Binary Search auf einen kontinuierlichen mathematischen Bereich anwenden kann, anstatt nur auf ein Array diskreter Objekte.
- Es führt das Konzept der Suche in einem "Antwortraum" (Decrease and Conquer) ein.

## Ansatz

**1. Der "Antwortraum":**
Wir haben kein Array, das wir durchsuchen können. Wir wissen jedoch, dass die Quadratwurzel von X zwingend zwischen 0 und X liegen muss.
Daher ist unser "Array" buchstäblich die kontinuierliche Folge von Ganzzahlen [0, 1, 2 \dots X].
Da diese Folge inhärent sortiert ist, können wir Binary Search anwenden!

**2. Die Logik der Binary Search:**
- `low = 0`, `high = x`.
- Bestimme `mid`.
- Berechne `square = mid * mid`.
- Wenn `square == x`: Wir haben die exakte Quadratwurzel gefunden! Gib `mid` zurück.
- Wenn `square < x`: `mid` ist zu klein. Aber Achtung: Da wir den *Floor* der Quadratwurzel suchen, könnte `mid` tatsächlich die korrekte Antwort sein, falls das Quadrat der nächsten Ganzzahl zu groß ist! Wir speichern `mid` in einer Variable `ans` und suchen dann im oberen Bereich weiter (`low = mid + 1`).
- Wenn `square > x`: `mid` ist zu groß. Die Antwort muss kleiner sein. Suche im unteren Bereich (`high = mid - 1`).

**3. Randfälle:**
Wenn X = 0 oder X = 1 ist, ist die Quadratwurzel einfach X. Dies kann direkt am Anfang der Funktion behandelt werden, um mathematische Anomalien zu vermeiden.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_10: Floor Square Root.

Given a non-negative integer n, return floor(sqrt(n)).
"""


def solve(n):
    """Return floor(sqrt(n)) via binary search (D&C style)."""
    if n < 2:
        return n
    lo, hi, res = 1, n, 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        sq = mid * mid
        if sq <= n:
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res
```

</details>

## Durchlauf

`x = 8`. `low = 1`, `high = 4` (da 8/2=4).

1. **Schleife 1:**
   - `mid = (1 + 4) // 2 = 2`.
   - `square = 2 * 2 = 4`.
   - `4 < 8`. Es ist ein Kandidat! `ans = 2`.
   - Suche höher: `low = 2 + 1 = 3`.
2. **Schleife 2:**
   - `mid = (3 + 4) // 2 = 3`.
   - `square = 3 * 3 = 9`.
   - `9 > 8`. Definitiv zu groß.
   - Suche niedriger: `high = 3 - 1 = 2`.
3. **Schleife 3:**
   - `low (3) <= high (2)` ist FALSCH. Die Schleife endet.

Das Ergebnis `ans` ist `2`. ✓ (Da 2^2 = 4 und 3^2 = 9, ist der Floor von \sqrt{8} gleich 2).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(log x)$ | $O(1)$ |
| **Schlechtester Fall** | $O(log x)$ | $O(1)$ |

Der Suchraum beginnt bei x/2 und wird wiederholt halbiert. Die Zeitkomplexität beträgt exakt $O(log X)$.
Es werden keine zusätzlichen Arrays alloziert. Die Platzkomplexität ist $O(1)$.

## Varianten & Optimierungen

- **Newton-Raphson-Verfahren:** Eine auf Analysis basierende Optimierung, die quadratisch statt logarithmisch konvergiert. Bei einer anfänglichen Schätzung r = x aktualisiert man die Schätzung wiederholt mittels r = \frac{1}{2} (r + \frac{x}{r}), bis r x r \le x gilt. Es erfordert Fließkommadivision, ist aber extrem schnell und mathematisch elegant.
- **Berechnung der exakten Fließkomma-Quadratwurzel:** Wenn die Frage nach der Quadratwurzel auf 5 Dezimalstellen statt nach dem Floor verlangt, kann keine Ganzzahldivision verwendet werden. Man initialisiert `low = 0.0`, `high = max(1.0, x)`. Man durchläuft eine Schleife `while (high - low) > 0.00001` (der Präzisionsschwellenwert) und berechnet `mid = (low + high) / 2.0`.

## Anwendungen in der Praxis

- **Computergrafik (Beleuchtungsmodelle):** Die Berechnung des euklidischen Abstandsvektors zwischen einer Lichtquelle und einer Pixelnormalen erfordert eine enorme Anzahl an Quadratwurzelberechnungen. Hardware-Grafikpipelines nutzen oft extrem clevere Bit-Hacks (wie die berühmte Fast Inverse Square Root `0x5f3759df` aus Quake III), um das Newton-Verfahren sofort zu approximieren.

## Verwandte Algorithmen in cOde(n)

- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — Die exakt gleiche Kernlogik, nur angewendet auf einen virtuellen Ganzzahlraum anstatt auf ein Array.
- **[math_01 - Fast Exponentiation](../math/math_01_fast-exponentiation.md)** — Ein weiterer mathematischer Divide-and-Conquer-Algorithmus.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*