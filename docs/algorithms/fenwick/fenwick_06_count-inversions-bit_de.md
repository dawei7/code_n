# Inversionen zählen (mit BIT)

| | |
|---|---|
| **ID** | `fenwick_06` |
| **Kategorie** | fenwick |
| **Komplexität (erforderlich)** | $O(N \log N)$ |
| **Schwierigkeitsgrad** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Globale und lokale Inversionen](https://leetcode.com/problems/global-and-local-inversions/) |

## Aufgabenstellung

Gegeben ist ein Array von Ganzzahlen `arr`. Bestimme die Gesamtzahl der **Inversionen**.
Eine Inversion ist definiert als ein Paar von Indizes `(i, j)`, für das `i < j` gilt, aber `arr[i] > arr[j]`.
Während dies klassischerweise mit einem modifizierten Merge-Sort gelöst wird, musst du es elegant mithilfe eines **Fenwick-Baums (BIT)** lösen.

**Eingabe:** Ein Array von ganzen Zahlen `arr`.
**Ausgabe:** Eine ganze Zahl, die die Gesamtanzahl der Inversionen angibt.

## Wann man es verwendet

- Immer dann, wenn man messen muss, wie „unsortiert“ ein Array ist.
- Der BIT-Ansatz lässt sich in einem Vorstellungsgespräch oft leichter von Grund auf neu implementieren als die Modifikation eines komplexen rekursiven Merge-Sorts, vorausgesetzt, man versteht die Koordinatenkompression.

## Vorgehensweise

Stellen wir uns vor, wir durchlaufen das Array von rechts nach links.
Für das aktuelle Element `arr[i]` tritt bei jedem Element, das wir *bereits gesehen* haben (das heißt, das sich rechts von `i` befindet) und das streng *kleiner* als `arr[i]` ist, eine Inversion auf.
Wenn wir irgendwie eine dynamische „Häufigkeitskarte“ der Elemente führen könnten, die wir bereits gesehen haben, müssten wir nur fragen: **„Wie viele Elemente in der Karte sind kleiner als `arr[i]`?“**

Das ist eine **Prefix-Summen-Abfrage**!
1. Wir können einen Fenwick Tree als Häufigkeitsarray verwenden. `BIT[val]` speichert, wie oft wir `val` gesehen haben.
2. Wenn wir `arr[i]` sehen, fragen wir das BIT nach der Summe aller Häufigkeiten von `1` bis `arr[i] - 1`. Dadurch erfahren wir sofort, wie viele Elemente rechts davon kleiner sind!
3. Wir addieren diese Anzahl zu unserer globalen Gesamtzahl der Umkehrungen.
4. Anschließend aktualisieren wir das BIT `update`, indem wir +1 zur Häufigkeit von `arr[i]` hinzufügen.

**Koordinatenkompression:**
Was ist, wenn die Zahlen im Array negativ oder sehr groß sind (z. B. 10^9)? Ein BIT-Array der Größe 10^9 würde den Speicher zum Absturz bringen!
Da uns nur die *relative* Reihenfolge (`<` oder `>`) interessiert, können wir die Werte auf dichte Ränge von 1 bis N abbilden.
`[100, -5, 4000, 100]` wird zu `[2, 1, 3, 2]`.
Nun beträgt der Maximalwert N, und unser BIT-Array passt perfekt in den Speicher!

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

## Schritt-für-Schritt-Anleitung

`arr = [8, 4, 2, 1]`

1. **Koordinatenkomprimierung:**
   - Sortiert und eindeutig: `[1, 2, 4, 8]`.
   - Ränge: `{1:1, 2:2, 4:3, 8:4}`.
   - Das Array sieht nun so aus: `[4, 3, 2, 1]`.
2. **BIT auf Größe 5 initialisiert:** `[0, 0, 0, 0, 0]`.
3. **Iteration von rechts nach links:**
   - **i = 3 (`val=1, rank=1`):**
 - Abfrage `Prefix(1 - 1) = Prefix(0) = 0`. `inversions = 0`.
     - +1 zum Rang 1 hinzufügen. `BIT` hat `1` auf Rang 1.
   - **i = 2 (`val=2, rank=2`):**
     - Abfrage von `Prefix(2 - 1) = Prefix(1) = 1`. `inversions = 0 + 1 = 1`.
 - +1 zum Rang 2 hinzufügen. `BIT` hat `1` auf Rang 2.
   - **i = 1 (`val=4, rank=3`):**
 - Abfrage von `Prefix(3 - 1) = Prefix(2) = 2`. `inversions = 1 + 2 = 3`.
 - +1 zum Rang 3 hinzufügen.
   - **i = 0 (`val=8, rank=4`):**
 - Abfrage `Prefix(4 - 1) = Prefix(3) = 3`. `inversions = 3 + 3 = 6`.
 - +1 zu Rang 4 hinzufügen.

Gesamtzahl der Umkehrungen = 6. ✓ (Das Array ist vollständig umgekehrt, daher gilt (N × (N-1))/2 = 6).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechteste** | $O(N \log N)$ | $O(N)$ |

Die Koordinatenkomprimierung erfordert das Sortieren der eindeutigen Elemente, was $O(N \log N)$ Zeit in Anspruch nimmt.
Die Rückwärtsiteration wird N-mal durchlaufen. Innerhalb der Schleife werden eine BIT-Abfrage und eine BIT-Aktualisierung durchgeführt, die jeweils $O(\log N)$ Zeit in Anspruch nehmen. Die Gesamtzeit beträgt $O(N \log N)$.
Die Platzkomplexität beträgt $O(N)$ für das Koordinatenkomprimierungs-Wörterbuch und das BIT-Array.

## Varianten und Optimierungen

- **Inversionen beim Mergesort:** Der klassische Ansatz. Wenn während des Zusammenführungsschritts beim Mergesort ein Element aus dem rechten Array vor einem Element im linken Array herangezogen wird, bedeutet dies, dass das rechte Element kleiner ist als *alle verbleibenden Elemente* im linken Array! Man addiert einfach `len(left) - left_ptr` zur Inversionsanzahl hinzu. Dies benötigt ebenfalls $O(N \log N)$ und vermeidet die Koordinatenkomprimierung vollständig.

## Praktische Anwendungen

- **Kollaboratives Filtern:** Messung des „Kendall-Tau-Abstands“ (der mathematisch aus der Inversionsanzahl abgeleitet wird) zwischen den Ranglisten zweier Nutzer, um Filme/Produkte zu empfehlen.

## Verwandte Algorithmen in cOde(n)

- **[sort_03 – Merge-Sort](../sorting/sort_03_merge-sort.md)** — Die Grundlage für die alternative, nicht-BIT-basierte Methode zur Zählung von Inversionen.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
