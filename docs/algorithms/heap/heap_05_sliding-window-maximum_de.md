# Sliding Window Maximum

| | |
|---|---|
| **ID** | `heap_05` |
| **Kategorie** | heap |
| **Komplexität (erforderlich)** | $O(N log K)$ mit Heap, $O(N)$ mit Deque |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) |

## Problemstellung

Gegeben ist ein Array von Integern `nums` und ein Integer `k`. Es gibt ein gleitendes Fenster (Sliding Window) der Größe `k`, das sich vom linken Ende des Arrays bis zum rechten Ende bewegt. Man kann nur die `k` Zahlen innerhalb des Fensters sehen. Bei jedem Schritt bewegt sich das Fenster um eine Position nach rechts.
Geben Sie ein Array zurück, das das Maximum innerhalb des Fensters bei jedem Schritt enthält.

**Eingabe:** Ein Array von Integern `nums` und ein Integer `k`.
**Ausgabe:** Ein Array von Integern, das das Maximum in jedem Fenster repräsentiert.

## Wann man es verwendet

- Ein häufig abgefragtes Problem in Vorstellungsgesprächen, um zu testen, ob man weiß, wie man eine **Monotonic Queue** aufbaut, welche den naiven Priority-Queue-Ansatz bei weitem übertrifft.
- Hinweis: Obwohl dies unter "Heap" kategorisiert ist, vermeidet die optimale Lösung explizit die Verwendung eines Heaps!

## Ansatz

**Ansatz 1: Der Lazy Max-Heap ($O(N \log N)$)**
Wir können einen Max-Heap von Tupeln `(value, index)` verwalten.
Wenn das Fenster zum Index `i` gleitet:
1. `push` von `(nums[i], i)` in den Max-Heap.
2. Das maximale Element befindet sich an `heap[0]`. Aber Vorsicht! Was, wenn das maximale Element vom Index `i - k - 1` stammt (es ist aus dem hinteren Teil des Fensters herausgefallen)?
3. **Lazy Deletion:** Wir verwenden einfach eine `while`-Schleife: Wenn `heap[0].index <= i - k`, führen wir `pop` aus! Wir kümmern uns nicht um veraltete Elemente tief im Heap, sondern nur darum, ob der *aktuelle Champion* veraltet ist.
4. Speichere `heap[0].value`.

**Ansatz 2: Die Monotonic Deque ($O(N)$ - Optimal!)**
Anstelle eines Heaps verwenden wir eine Double-Ended Queue (Deque), um Array-`indices` zu speichern.
Wir halten eine strikte Regel ein: **Die Werte, die den Indizes in der Deque entsprechen, müssen streng monoton fallend sein.**
Warum? Wenn eine neue, riesige Zahl `100` in das Fenster eintritt, sind alle kleineren Zahlen `5, 10, 50`, die *vor* ihr in das Fenster eingetreten sind, völlig nutzlos! Sie können niemals wieder das Maximum sein, da `100` größer als sie ist UND sie länger im Fenster überleben wird als sie!

1. Iteriere durch `nums` am Index `i`.
2. **Veraltete Elemente entfernen:** Wenn der Index an der `front` der Deque \le i - k ist, ist er aus dem Fenster gefallen. Führe `popleft()` aus.
3. **Verlierer entfernen:** Solange der `back` der Deque einen Wert \le nums[i] hat, führe `pop()` aus. Diese sind totes Gewicht.
4. **Neues Element hinzufügen:** `append(i)` an den `back` der Deque.
5. Das Maximum des aktuellen Fensters ist immer sofort an der `front` der Deque verfügbar!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for heap_05: Sliding Window Maximum.

For each window of size k, return the max. Use a max-heap keyed
on (-value, index); pop from the top while the index is outside
the current window.
"""


def solve(arr, k, n):
    if k <= 0 or k > n:
        return []
    import heapq
    heap = []
    for i in range(k):
        heapq.heappush(heap, (-arr[i], i))
    out = [-heap[0][0]]
    for i in range(k, n):
        heapq.heappush(heap, (-arr[i], i))
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        out.append(-heap[0][0])
    return out
```

</details>

## Durchlauf

`nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`.
`q` speichert Indizes. Betrachten wir `q_vals` zur konzeptionellen Verdeutlichung.

1. **i=0 (num=1):** `q=[0]`. `q_vals=[1]`.
2. **i=1 (num=3):** Pop `0` (1 <= 3). Push `1`. `q=[1]`. `q_vals=[3]`.
3. **i=2 (num=-1):** Push `2`. `q=[1, 2]`. `q_vals=[3, -1]`.
   - Fenstergröße 3 erreicht! Maximum ist `nums[q[0]] = 3`. `res = [3]`.
4. **i=3 (num=-3):** Push `3`. `q=[1, 2, 3]`. `q_vals=[3, -1, -3]`.
   - Maximum ist `3`. `res = [3, 3]`.
5. **i=4 (num=5):** Veraltungsprüfung: `q[0]=1 <= 4-3` (1 <= 1). Pop `1`! (Die `3` ist abgelaufen).
   - Verliererprüfung: Pop `-3`. Pop `-1`. Push `4`. `q=[4]`. `q_vals=[5]`.
   - Maximum ist `5`. `res = [3, 3, 5]`.
6. **i=5 (num=3):** Push `5`. `q=[4, 5]`. `q_vals=[5, 3]`.
   - Maximum ist `5`. `res = [3, 3, 5, 5]`.
7. **i=6 (num=6):** Verliererprüfung: Pop `3`. Pop `5`. Push `6`. `q=[6]`. `q_vals=[6]`.
   - Maximum ist `6`. `res = [3, 3, 5, 5, 6]`.
8. **i=7 (num=7):** Verliererprüfung: Pop `6`. Push `7`. `q=[7]`. `q_vals=[7]`.
   - Maximum ist `7`. `res = [3, 3, 5, 5, 6, 7]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(K)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(K)$ |
| **Schlechtester Fall** | $O(N)$ | $O(K)$ |

Moment, es gibt eine `while`-Schleife innerhalb der `for`-Schleife! Macht das nicht $O(N \times K)$?
Nein! Bei Anwendung der amortisierten Analyse lässt sich beobachten, dass jeder einzelne Index im Array genau einmal an die Deque `append`ed wird. Er kann daher auch höchstens genau einmal aus der Deque `pop`ped werden. Der Code innerhalb der `while`-Schleife läuft über die *gesamte* Ausführung des Algorithmus hinweg höchstens N-mal. Daher ist die Gesamtlaufzeit strikt $O(N)$.
Die Platzkomplexität beträgt $O(K)$, da die Deque niemals mehr als K Elemente enthalten wird.

## Varianten & Optimierungen

- **2D Sliding Window (Maximum in Matrix-Subgrid):** Eine deutlich schwierigere Variante, bei der man das Maximum in einem sich bewegenden K x K-Kasten finden muss. Dies wird gelöst, indem man den 1D-Monotonic-Deque-Algorithmus horizontal auf jede Zeile anwendet, die Ergebnisse in einer neuen Matrix speichert und anschließend vertikal auf jede Spalte der neuen Matrix anwendet!

## Anwendungen in der Praxis

- **Digitale Signalverarbeitung:** Berechnung der gleitenden Maximum-/Minimum-Hüllkurve einer Audiowelle oder eines Börsentickers, um starke Ausschläge innerhalb eines rollierenden Zeitrahmens zu erkennen.

## Verwandte Algorithmen in cOde(n)

- **[stack_01 - Next Greater Element](../stacks/stack_01_next-greater-element.md)** — Die Grundlage der monotonen Datenstruktur. Die Logik zum Entfernen kleinerer Elemente ist mathematisch identisch.
- **[heap_04 - Median in Stream](heap_04_median-in-a-stream.md)** — Ein weiterer Manager für den Zustand eines rollierenden Fensters.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*