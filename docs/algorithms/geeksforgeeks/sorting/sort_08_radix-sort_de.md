# Radix Sort

| | |
|---|---|
| **ID** | `sort_08` |
| **Kategorie** | sorting |
| **Komplexität (erforderlich)** | $O(D \times (N + K)$) Zeit, $O(N + K)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Radix sort](https://en.wikipedia.org/wiki/Radix_sort) |

## Problemstellung

Gegeben ist ein Array von Integern `arr`. Sortieren Sie das Array in aufsteigender Reihenfolge.
Sie müssen das Array in linearer $O(N)$-Zeit sortieren und damit die mathematische $O(N \log N)$-Barriere für vergleichsbasierte Sortieralgorithmen durchbrechen.

**Eingabe:** Ein unsortiertes Array von Integern `arr`.
**Ausgabe:** Ein sortiertes Array.

## Wann man es verwendet

- Beim Sortieren von Integern, Strings oder Sequenzen fester Länge, bei denen die maximale Anzahl an Ziffern/Zeichen (D) relativ klein ist.
- Um das $O(N \log N)$-Limit von Algorithmen wie Merge Sort und Quick Sort vollständig zu umgehen.

## Ansatz

**1. Der Schwachpunkt von Counting Sort (`sort_07`):**
Counting Sort erreicht $O(N)$-Zeit, erfordert jedoch die Allokation eines Arrays, dessen Größe dem MAXIMALEN Wert im Array entspricht. Wenn Sie nur zwei Elemente `[1, 999999999]` haben, bringt Counting Sort den Speicher zum Absturz, indem es versucht, ein Array der Größe 1 Milliarde zu allokieren!

**2. Die Ziffer-für-Ziffer-Strategie (Radix):**
Anstatt die gesamte Zahl auf einmal zu sortieren, was wäre, wenn wir die Zahlen *Ziffer für Ziffer* sortieren würden?
Zuerst sortieren wir alle Zahlen rein basierend auf ihrer Einerstelle (Least Significant Digit).
Dann sortieren wir sie basierend auf ihrer Zehnerstelle.
Dann die Hunderterstelle... bis zur maximalen Anzahl an Ziffern!
Nach dem letzten Durchgang ist das Array auf magische Weise vollständig sortiert!

**3. Die Anforderung an ein stabiles Sortierverfahren:**
Damit dieser Zaubertrick funktioniert, MUSS der zugrunde liegende Ziffern-Sortieralgorithmus ein "stabiles Sortierverfahren" (Stable Sort) sein.
(Wenn zwei Zahlen dieselbe Zehnerstelle haben, z. B. 52 und 58, MUSS der Sortieralgorithmus ihre relative Reihenfolge aus dem vorherigen Durchgang der Einerstellen beibehalten. Wenn er sie vertauscht, schlägt der Algorithmus fehl).
Wir verwenden **Counting Sort** als zugrunde liegende Subroutine! Da wir jedoch immer nur eine einzige Basis-10-Ziffer auf einmal sortieren, muss das Counting-Sort-Array nur die Größe `10` haben! Speicherabsturz vermieden!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_08: Radix Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n) time.
"""


def solve(data, n):
    if n == 0:
        return data
    max_val = max(data)
    exp = 1
    while max_val // exp > 0:
        # Counting sort on the current digit.
        counts = [0] * 10
        for value in data:
            counts[(value // exp) % 10] += 1
        # Turn counts into a stable-position table.
        for i in range(1, 10):
            counts[i] += counts[i - 1]
        # Walk the input right-to-left so the sort stays stable.
        output = [0] * n
        for i in range(n - 1, -1, -1):
            digit = (data[i] // exp) % 10
            counts[digit] -= 1
            output[counts[digit]] = data[i]
        # Copy the per-digit sorted output back into data.
        for i in range(n):
            data[i] = output[i]
        exp *= 10
    return data
```

</details>

## Ablaufbeispiel

`arr = [170, 45, 75, 90, 802, 24, 2, 66]`.
Der Maximalwert ist `802` (3 Ziffern). Wir führen 3 Durchgänge durch (`exp=1`, `exp=10`, `exp=100`).

1. **`exp = 1` (Einerstelle):**
   - Ziffern extrahieren: `0, 5, 5, 0, 2, 4, 2, 6`.
   - Counting Sort platziert sie:
   - `[170, 90, 802, 2, 24, 45, 75, 66]`.
2. **`exp = 10` (Zehnerstelle):**
   - Ziffern extrahieren: `7, 9, 0, 0, 2, 4, 7, 6`.
   - Counting Sort behält die relative Stabilität strikt bei! (z. B. bleibt `802` vor `2`, da beide eine Zehnerziffer von `0` haben).
   - `[802, 2, 24, 45, 66, 170, 75, 90]`.
3. **`exp = 100` (Hunderterstelle):**
   - Ziffern extrahieren: `8, 0, 0, 0, 0, 1, 0, 0`.
   - Counting Sort wird angewendet.
   - `[2, 24, 45, 66, 75, 90, 170, 802]`.

Das Array ist sortiert! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(D \times (N + K)$) | $O(N + K)$ |
| **Durchschnittlicher Fall** | $O(D \times (N + K)$) | $O(N + K)$ |
| **Schlechtester Fall** | $O(D \times (N + K)$) | $O(N + K)$ |

Sei N die Anzahl der Elemente. Sei K die Basis des Zahlensystems (10 für Dezimalziffern). Sei D die maximale Anzahl an Ziffern.
Counting Sort benötigt $O(N + K)$ Zeit.
Radix Sort ruft Counting Sort genau D-mal auf.
Daher ist die Zeitkomplexität strikt $O(D \times (N + K)$).
Wenn D eine kleine Konstante ist (z. B. haben 64-Bit-Integer maximal 20 Dezimalziffern), sinkt die Zeitkomplexität perfekt auf $O(N)$ lineare Zeit!
Die Platzkomplexität beträgt $O(N + K)$, um das `output`-Array und das Basis-10-`count`-Array zu speichern.

## Varianten & Optimierungen

- **Basis 256 (Bitweiser Radix):** Anstatt Basis-10-Ziffern zu verwenden, optimieren moderne Systeme Radix Sort durch die Verwendung von Basis-256 (ein einzelnes 8-Bit-Byte). Durch die Verwendung von bitweisen Verschiebungen `(arr[i] >> (pass * 8)) & 0xFF` anstelle von Modulo-Arithmetik `(arr[i] // exp) % 10` führt die CPU den Algorithmus um Größenordnungen schneller aus. Ein 32-Bit-Integer wird in genau 4 Durchgängen sortiert!
- **MSD Radix Sort (Most Significant Digit):** Die oben geschriebene Version ist LSD (Least Significant Digit). MSD Radix Sort beginnt bei der höchsten Ziffer und unterteilt das Array rekursiv in "Buckets", was für das Sortieren von alphabetischen Strings hochgradig optimal ist!

## Anwendungen in der Praxis

- **String/Suffix-Array-Sortierung:** Radix Sort ist der weltweit schnellste Algorithmus zum Sortieren von Arrays aus Strings fester Länge (wie IP-Adressen, UUIDs oder DNA-Sequenzen), wobei jedes Zeichen als "Ziffer" behandelt wird.

## Verwandte Algorithmen in cOde(n)

- **[sort_07 - Counting Sort](sort_07_counting-sort.md)** — Die Engine, die die Ziffer-für-Ziffer-Sortierdurchgänge antreibt.
- **[sort_09 - Bucket Sort](sort_09_bucket-sort.md)** — Ein weiterer nicht-vergleichsbasierter Integer-Sortieralgorithmus, der Elemente in gleichmäßige Bereiche verteilt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*