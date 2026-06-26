# K-th Smallest / Order Statistic (Binary Lifting)

| | |
|---|---|
| **ID** | `fenwick_07` |
| **Category** | fenwick |
| **Complexity (required)** | $O(log M)$ Query |
| **Difficulty** | 8/10 |
| **Interview relevance** | 3/10 |
| **LeetCode Equivalent** | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) (Advanced Variant) |

## Problem statement

Gegeben ist eine dynamische Sammlung von Zahlen, in der Elemente kontinuierlich eingefügt oder gelöscht werden können. Unterstützen Sie eine Abfrage, um das **K-th smallest element** (das k-te Ordnungselement) in der Sammlung zu finden.
Während ein balancierter Binary Search Tree (wie ein AVL- oder Rot-Schwarz-Baum, der um Teilbaumgrößen erweitert wurde) dies auf natürliche Weise löst, ist die Implementierung eines solchen Baums von Grund auf in einem Interview praktisch unmöglich.
Sie müssen dies elegant lösen, indem Sie einen **Fenwick Tree** in Kombination mit einer Technik namens **Binary Lifting** verwenden, um die Abfrage in strikter $O(log M)$ Zeit zu beantworten.

**Input:** Eine Sequenz von Einfügungen und Abfragen für das K-th smallest element.
**Output:** Die Werte, die die Abfragen beantworten.

## When to use it

- Zur Bestimmung von gleitenden Medianen oder spezifischen Perzentilen in einem hochdynamischen Datenstrom.
- Binary Lifting auf einem Fenwick Tree ist eine tiefgreifende "Geheimwaffe" in der wettbewerbsorientierten Programmierung, um das Schreiben hunderter Zeilen von AVL-Tree-Code zu vermeiden.

## Approach

Wie in `fenwick_06` verwenden wir den Fenwick Tree als **Frequency Array**. `BIT[val]` speichert, wie oft `val` in unserer Sammlung vorkommt.
Die Präfixsumme bis `val` verrät uns genau, wie viele Elemente in der Sammlung $\le val$ sind.
Um das K-th smallest element zu finden, suchen wir den **kleinsten Index `val`, für den gilt: `PrefixSum(val) >= K`**.

Ein naiver Ansatz wäre eine binäre Suche über den Indexbereich $1 \dots M$. Für jeden Schätzwert `mid` fragen wir den BIT nach der Präfixsumme ab. Dies benötigt $O(log M)$ für die binäre Suche und $O(log M)$ für die Präfixabfrage, was zu $O(log^2 M)$ führt.

**Binary Lifting ($O(log M)$):**
Wir können die binäre Suche *direkt in die Traversierungsstruktur des BIT* integrieren!
1. Wir beginnen bei `index = 0` und `current_sum = 0`.
2. Wir betrachten die größte Zweierpotenz, die in unser Maximum passt (z. B. $2^{19}$). Nennen wir diese `step`.
3. Wir prüfen den BIT an der Stelle `index + step`. Aufgrund der Konstruktion des Fenwick Trees speichert `BIT[index + step]` praktischerweise genau die Summe der Häufigkeiten des Blocks von `index` bis `index + step`!
4. Wenn `current_sum + BIT[index + step] < K`:
   - Das bedeutet, das k-te Element ist strikt *größer* als `index + step`.
   - Wir springen sicher vorwärts! `index += step`.
   - Wir akkumulieren die Summe: `current_sum += BIT[index]`.
5. Wenn die Summe $\ge K$ ist, springen wir NICHT.
6. Halbieren Sie `step` (z. B. auf $2^{18}$) und wiederholen Sie den Vorgang, bis `step` zu 0 wird.
7. Der Zielindex ist `index + 1`!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for fenwick_07: K-th Smallest (Order-Statistic BIT).

Given a frequency array freq[1..n] (how many times
"""


def solve(freq, n, k):
    """K-th smallest via order-statistic BIT (binary lifting)."""
    total = sum(freq)
    if k < 1 or k > total:
        return -1
    if n == 0:
        return -1
    # Build BIT.
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] = freq[i - 1]
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]
    # Binary lifting: find largest idx with BIT.prefix(idx) < k.
    # The k-th smallest value is then idx + 1 (since the BIT
    # is 1-indexed and BIT[i] represents the count of value i).
    # The descent uses STRICT less-than: we take a step only
    # if bit[pos + bitmask] < (k - bit.prefix(pos)), so that
    # bit.prefix(pos) stays strictly less than k. The k-th
    # value is the smallest idx with prefix >= k, which is
    # (largest pos with prefix < k) + 1.
    idx = 0
    bitmask = 1
    while bitmask << 1 <= n:
        bitmask <<= 1
    remaining = k
    while bitmask > 0:
        nxt = idx + bitmask
        if nxt <= n and bit[nxt] < remaining:
            remaining -= bit[nxt]
            idx = nxt
        bitmask >>= 1
    return idx + 1
```

</details>

## Walk-through

*(Konzeptionell)*
`max_val = 15`. `max_power = 8`.
Werte einfügen: `[2, 2, 5, 8]`.
Wir suchen das `K = 3`. kleinste Element (das 5 sein sollte).
Das BIT-Array ist mit diesen Häufigkeiten gefüllt.

1. `step = 8`. Prüfe `BIT[8]` (enthält die Summe der Häufigkeiten 1 bis 8). Nehmen wir an, `BIT[8] = 4` (da alle vier Elemente $\le 8$ sind).
   - `0 + 4 < 3` ist FALSCH. Nicht springen. `index = 0`.
2. `step = 4`. Prüfe `BIT[4]` (enthält Summe 1 bis 4). Wert ist 2 (die beiden `2`er).
   - `0 + 2 < 3` ist WAHR!
   - Springen! `index = 4`. `current_sum = 2`.
3. `step = 2`. Prüfe `BIT[4 + 2 = 6]`. (Enthält Summe von 5 bis 6). Wert ist 1 (die `5`).
   - `current_sum (2) + BIT[6] (1) < 3` ist FALSCH (3 < 3 ist falsch).
   - Nicht springen. `index = 4`.
4. `step = 1`. Prüfe `BIT[4 + 1 = 5]`. (Enthält Summe von 5). Wert ist 1.
   - `current_sum (2) + BIT[5] (1) < 3` ist FALSCH.
   - Nicht springen. `index = 4`.

Die Schleife endet. Rückgabe `index + 1` = `5`. ✓
Das 3. kleinste Element ist exakt 5!

## Complexity

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(log M)$ | $O(M)$ |
| **Durchschnittlicher Fall** | $O(log M)$ | $O(M)$ |
| **Schlechtester Fall** | $O(log M)$ | $O(M)$ |

*Wobei M der Maximalwert in der Sammlung ist.*
Die Binary-Lifting-Schleife wird exakt $\log_2 M$ mal ausgeführt. In jeder Iteration führt sie $O(1)$ Operationen aus, da sie die Summe direkt vom spezifischen BIT-Index liest, ohne nach oben zu traversieren! Die Zeitkomplexität ist strikt $O(log M)$.
Die Platzkomplexität beträgt $O(M)$ für das Speichern des BIT-Arrays (was eine Koordinatenkompression erfordert, falls M astronomisch groß ist).

## Variants & optimizations

- **Segment Tree Walking:** Sie können exakt dieselbe $O(log M)$ Abfrage für das Ordnungselement erreichen, indem Sie einen Segment Tree durchlaufen und je nachdem, ob die Summe des linken Kindes $\ge K$ ist, nach links oder rechts abbiegen. Die Fenwick-Tree-Version ist jedoch aufgrund der Speicherlokalität und des Verzichts auf Pointer deutlich schneller.

## Real-world applications

- **Datenbank-Perzentile:** Berechnung der exakten 99. Perzentil-Antwortzeit aus einem hochfrequenten Strom von Server-Telemetrie-Logs.

## Related algorithms in cOde(n)

- **[fenwick_06 - Count Inversions](fenwick_06_count-inversions-bit.md)** — Die grundlegende Anwendung des Fenwick Trees als Häufigkeitskarte.
- **[heap_04 - Median in a Stream](../heap/heap_04_median-in-a-stream.md)** — Ein anderer Ansatz unter Verwendung von zwei Priority Queues. Zwei Heaps sind besser, wenn Sie *nur* den exakten 50. Perzentil (Median) benötigen, aber der Fenwick-Ansatz ist erforderlich, wenn Sie beliebige K-te Perzentile dynamisch abfragen möchten.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für wettbewerbsorientierte Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*