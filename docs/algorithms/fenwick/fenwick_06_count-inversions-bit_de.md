# Inversionen zählen (mit BIT)

| | |
|---|---|
| **ID** | `fenwick_06` |
| **Kategorie** | fenwick |
| **Komplexität (erforderlich)** | $O(N \log N)$ |
| **Schwierigkeit** | 6/10 |
| **Interview-Relevanz** | 7/10 |
| **LeetCode-Äquivalent** | [Global and Local Inversions](https://leetcode.com/problems/global-and-local-inversions/) |

## Problemstellung

Gegeben ist ein Array von Ganzzahlen `arr`. Finde die Gesamtzahl der **Inversionen**.
Eine Inversion ist definiert als ein Paar von Indizes `(i, j)`, sodass `i < j`, aber `arr[i] > arr[j]` gilt.
Während dies klassischerweise mit einem modifizierten Merge Sort gelöst wird, musst du es hier elegant mithilfe eines **Fenwick Tree (BIT)** lösen.

**Eingabe:** Ein Array von Ganzzahlen `arr`.
**Ausgabe:** Eine Ganzzahl, die die Gesamtzahl der Inversionen repräsentiert.

## Wann man es verwendet

- Immer dann, wenn du messen musst, wie „unsortiert“ ein Array ist.
- Der BIT-Ansatz ist in einem Interview oft einfacher von Grund auf zu implementieren als ein komplexer rekursiver Merge Sort, vorausgesetzt, man versteht die Koordinatenkompression.

## Ansatz

Stell dir vor, wir iterieren von rechts nach links durch das Array.
Für das aktuelle Element `arr[i]` tritt eine Inversion für jedes Element auf, das wir *bereits gesehen haben* (was bedeutet, dass sie rechts von `i` liegen) und das strikt *kleiner* als `arr[i]` ist.
Wenn wir irgendwie eine dynamische „Häufigkeitskarte“ der bereits gesehenen Elemente pflegen könnten, müssten wir nur fragen: **„Wie viele Elemente in der Karte sind kleiner als `arr[i]`?“**

Dies ist eine **Präfixsummen-Abfrage (Prefix Sum Query)**!
1. Wir können einen Fenwick Tree als Häufigkeits-Array verwenden. `BIT[val]` speichert, wie oft wir `val` bereits gesehen haben.
2. Wenn wir `arr[i]` sehen, fragen wir den BIT nach der Summe aller Häufigkeiten von `1` bis `arr[i] - 1`. Dies sagt uns sofort, wie viele Elemente rechts davon kleiner sind!
3. Wir addieren diese Anzahl zu unserer globalen Gesamtzahl der Inversionen.
4. Dann führen wir ein `update` auf dem BIT durch, indem wir die Häufigkeit von `arr[i]` um +1 erhöhen.

**Koordinatenkompression:**
Was ist, wenn die Zahlen im Array negativ oder extrem groß sind (z. B. 10^9)? Ein BIT-Array der Größe 10^9 würde den Speicher sprengen!
Da uns nur die *relative* Ordnung (`<` oder `>`) interessiert, können wir die Werte auf dichte Ränge von 1 bis N abbilden.
`[100, -5, 4000, 100]` wird zu `[2, 1, 3, 2]`.
Nun ist der Maximalwert N, und unser BIT-Array passt perfekt in den Speicher!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for fenwick_06: Count Inversions (BIT).

Count the number of inversions in an array: pairs
"""


def solve(arr, n):
    """Inversion count via BIT, with value compression."""
    if n <= 1:
        return 0
    # Compress arr to 1..n by rank order.
    sorted_unique = sorted(set(arr))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
    compressed = [rank[v] for v in arr]
    # BIT of size n (max compressed value is n).
    bit = [0] * (n + 2)
    inv = 0
    for i in range(n - 1, -1, -1):
        v = compressed[i]
        # prefix sum of bit up to v-1.
        j = v - 1
        s = 0
        while j > 0:
            s += bit[j]
            j -= j & -j
        inv += s
        # Add 1 at index v.
        j = v
        while j <= n:
            bit[j] += 1
            j += j & -j
    return inv
```

</details>

## Durchlauf

`arr = [8, 4, 2, 1]`

1. **Koordinatenkompression:**
   - Sortierte eindeutige Werte: `[1, 2, 4, 8]`.
   - Ränge: `{1:1, 2:2, 4:3, 8:4}`.
   - Array wird zu: `[4, 3, 2, 1]`.
2. **BIT initialisiert auf Größe 5:** `[0, 0, 0, 0, 0]`.
3. **Iteration von rechts nach links:**
   - **i = 3 (`val=1, rank=1`):**
     - Abfrage `Prefix(1 - 1) = Prefix(0) = 0`. `inversions = 0`.
     - Addiere +1 zu Rang 1. `BIT` hat `1` an Rang 1.
   - **i = 2 (`val=2, rank=2`):**
     - Abfrage `Prefix(2 - 1) = Prefix(1) = 1`. `inversions = 0 + 1 = 1`.
     - Addiere +1 zu Rang 2. `BIT` hat `1` an Rang 2.
   - **i = 1 (`val=4, rank=3`):**
     - Abfrage `Prefix(3 - 1) = Prefix(2) = 2`. `inversions = 1 + 2 = 3`.
     - Addiere +1 zu Rang 3.
   - **i = 0 (`val=8, rank=4`):**
     - Abfrage `Prefix(4 - 1) = Prefix(3) = 3`. `inversions = 3 + 3 = 6`.
     - Addiere +1 zu Rang 4.

Gesamtzahl der Inversionen = 6. ✓ (Das Array ist perfekt umgekehrt, daher gilt (N x (N-1))/2 = 6).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(N)$ |

Die Koordinatenkompression erfordert das Sortieren der eindeutigen Elemente, was $O(N \log N)$ Zeit in Anspruch nimmt.
Die Rückwärtsiteration läuft N-mal durch. Innerhalb der Schleife führt sie eine BIT-Abfrage und ein BIT-Update durch, was jeweils $O(\log N)$ Zeit benötigt. Die Gesamtzeit beträgt $O(N \log N)$.
Die Platzkomplexität beträgt $O(N)$ für das Dictionary der Koordinatenkompression und das BIT-Array.

## Varianten & Optimierungen

- **Merge Sort Inversionen:** Der klassische Ansatz. Während des Merge-Schritts von Merge Sort gilt: Wenn ein Element aus dem rechten Array vor einem Element aus dem linken Array gezogen wird, bedeutet dies, dass das rechte Element kleiner ist als *alle verbleibenden Elemente* im linken Array! Man addiert einfach `len(left) - left_ptr` zur Inversionsanzahl. Dies benötigt ebenfalls $O(N \log N)$ und vermeidet die Koordinatenkompression vollständig.

## Anwendungen in der Praxis

- **Collaborative Filtering:** Messung der „Kendall-Tau-Distanz“ (die mathematisch aus der Inversionsanzahl abgeleitet ist) zwischen den bewerteten Präferenzlisten zweier Benutzer, um Filme oder Produkte zu empfehlen.

## Verwandte Algorithmen in cOde(n)

- **[sort_03 - Merge Sort](../sorting/sort_03_merge-sort.md)** — Die Grundlage für die alternative, nicht-BIT-basierte Methode zum Zählen von Inversionen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*