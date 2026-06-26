# Tim Sort (vereinfacht)

| | |
|---|---|
| **ID** | `sort_13` |
| **Kategorie** | Sortieren |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Timsort](https://en.wikipedia.org/wiki/Timsort) |

## Problemstellung

Gegeben ist ein Array von Integern `arr`. Sortieren Sie das Array in aufsteigender Reihenfolge.
Sie müssen einen hybriden Algorithmus verwenden, der im Schlechtesten Fall eine Zeitkomplexität von $O(N \log N)$ garantiert, aber für bereits teilweise sortierte Daten auf $O(N)$ optimiert ist.

**Eingabe:** Ein unsortiertes Array von Integern `arr`.
**Ausgabe:** Ein sortiertes Array.

## Wann man es verwendet

- Wenn Sie in Python `arr.sort()` oder in Java `Arrays.sort()` aufrufen. Dies IST der Algorithmus, der im Hintergrund ausgeführt wird!
- Um tiefgreifendes Systemwissen darüber zu demonstrieren, wie rein akademische Algorithmen (Merge Sort / Insertion Sort) für reale Hardware kombiniert werden.

## Ansatz

**1. Die Realität realer Daten:**
Merge Sort ist mathematisch brillant, da es Arrays bis auf die Größe 1 unterteilt und dann wieder zusammenführt. Das rekursive Zerlegen eines Arrays bis zur Größe 1 verursacht jedoch einen massiven Overhead durch den Call Stack.
Darüber hinaus sind reale Daten selten zu 100 % zufällig. Sie enthalten meist lange "Runs" (Läufe) von Daten, die bereits perfekt sortiert sind! Merge Sort reißt diese sortierten Läufe blind bis zur Größe 1 auseinander und zerstört damit die bestehende Ordnung vollständig.

**2. Die hybride Strategie von Tim Sort:**
Tim Sort wurde 2002 von Tim Peters für Python erfunden und ist eine elegante Verbindung von **Insertion Sort** und **Merge Sort**.
Insertion Sort ist bei kleinen Arrays (Größe \le 32) unglaublich schnell und theoretisch $O(N)$ bei Arrays, die bereits weitgehend sortiert sind!
Merge Sort ist perfekt stabil und garantiert $O(N \log N)$ für extrem große Arrays.
Wir unterteilen das große Array also einfach in feste Blöcke der Größe 32 (genannt "Runs"). Wir sortieren jeden 32-Elemente-Run einzeln mittels Insertion Sort. Danach verwenden wir die `merge()`-Funktion von Merge Sort, um die sortierten Blöcke nahtlos zusammenzufügen!

**3. Die Schritte des Algorithmus:**
1. Wählen Sie eine `RUN`-Größe (typischerweise 32 oder 64).
2. Iterieren Sie in `RUN`-großen Stücken durch das Array.
3. Rufen Sie `insertion_sort` für jedes Stück auf.
4. Initialisieren Sie eine `size`-Variable mit `RUN`.
5. Iterieren Sie durch das Array, nehmen Sie zwei benachbarte Stücke der Größe `size` und führen Sie diese zu einem Stück der Größe `size * 2` zusammen.
6. Verdoppeln Sie die `size` und wiederholen Sie die Zusammenführungsphase, bis `size > N`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_13: Tim Sort (Simplified).

Identify natural runs, extend to minrun, merge pairwise.
"""


def solve(data, n):
    if n <= 1:
        return data
    work = list(data)
    RUN = max(1, min(32, n // 4))
    runs = []
    i = 0
    while i < n:
        j = i + 1
        while j < n and work[j] >= work[j - 1]:
            j += 1
        runs.append((i, j))
        if j - i < RUN:
            end = min(i + RUN, n)
            sub = work[i:end]
            sub.sort()
            work[i:end] = sub
            j = end
            runs[-1] = (runs[-1][0], j)  # update with extended end
        i = j
    while len(runs) > 1:
        new_runs = []
        for k in range(0, len(runs), 2):
            if k + 1 < len(runs):
                lo1, hi1 = runs[k]
                lo2, hi2 = runs[k + 1]
                merged = []
                a, b = lo1, lo2
                while a < hi1 and b < hi2:
                    if work[a] <= work[b]:
                        merged.append(work[a])
                        a += 1
                    else:
                        merged.append(work[b])
                        b += 1
                merged.extend(work[a:hi1])
                merged.extend(work[b:hi2])
                work[lo1:hi2] = merged
                new_runs.append((lo1, hi2))
            else:
                new_runs.append(runs[k])
        runs = new_runs
    return work
```

</details>

## Durchlauf

`arr = [5, 21, 7, 23, 19, 11, 3, 17]`. `N = 8`.
Setzen wir für dieses Beispiel künstlich `MIN_MERGE = 4`.

**Phase 1: Insertion Sort Runs**
- Stück 1: `[5, 21, 7, 23]` (Indizes 0 bis 3).
  - Insertion Sort sortiert dies perfekt zu `[5, 7, 21, 23]`.
- Stück 2: `[19, 11, 3, 17]` (Indizes 4 bis 7).
  - Insertion Sort sortiert dies perfekt zu `[3, 11, 17, 19]`.
Das Array besteht nun aus zwei sortierten Blöcken: `[5, 7, 21, 23 | 3, 11, 17, 19]`.

**Phase 2: Zusammenführen (Merging)**
- `size = 4`.
- `left = 0`, `mid = 3`, `right = 7`.
- Zusammenführen von `[5, 7, 21, 23]` mit `[3, 11, 17, 19]`.
  - Vergleicht Pointer und fügt die Elemente korrekt ineinander.
Das Array ist perfekt sortiert: `[3, 5, 7, 11, 17, 19, 21, 23]`. ✓
- `size = 8`. `size < N` ist falsch. Die Schleife terminiert!

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(N)$ |

Das Array wird in N/32 Blöcke unterteilt. Insertion Sort sortiert jeden Block in konstanter Zeit $O(32^2) \approx O(1)$. Über N/32 Blöcke hinweg benötigt diese Initialphase $O(N)$ Zeit.
Die Zusammenführungsphase verdoppelt die Blockgröße bei jedem Schritt, was genau $\log_2(N/32)$ Durchläufe erfordert. Jeder Durchlauf berührt jedes Element, was $O(N)$ Zeit in Anspruch nimmt.
Die gesamte Zeitkomplexität im Schlechtesten Fall beträgt $O(N \log N)$.
Wenn das Array jedoch vollständig sortiert ist, wird Phase 1 in genau $O(N)$ Zeit ausgeführt, und die fortgeschrittene Logik zum Zusammenführen erkennt, dass keine Merges erforderlich sind, wodurch der Algorithmus sofort im Bestfall mit $O(N)$ Zeit terminiert!
Die Platzkomplexität beträgt $O(N)$, da die `merge`-Subroutine zwingend die Erstellung temporärer linker/rechter Arrays erfordert.

## Varianten & Optimierungen

- **Natürliche Runs (Der echte Tim Sort):** Die Python-Implementierung schneidet nicht blind Blöcke der Größe 32 ab. Sie scannt das Array sequenziell, um "natürliche Runs" (bereits sortierte Sequenzen) zu finden. Wenn ein natürlicher Run kleiner als 32 ist, wird Insertion Sort verwendet, um ihn auf 32 aufzufüllen. Wenn ein natürlicher Run 1000 Elemente lang ist, lässt der Algorithmus ihn vollständig intakt und führt ihn später einfach als massiven Block zusammen!
- **Galloping Mode (`search_07`):** Während der `merge`-Subroutine, wenn Tim Sort bemerkt, dass der Pointer auf dem `left_arr` 7 Mal hintereinander gewinnt, nimmt er mathematisch an, dass das `left_arr` wesentlich kleiner ist. Er wechselt von $O(1)$ linearen Pointer-Inkrementen zu einer $O(\log N)$ exponentiellen Suche, um die Einfügegrenze sofort zu finden, was Tausende von Vergleichen einspart!

## Anwendungen in der Praxis

- **Python, Java, Android, V8 Engine:** Er ist der unbestrittene König des stabilen Sortierens. Wenn eine Sprache ein unglaublich schnelles, stabiles Sortieren für Objekte verspricht, verwendet sie Tim Sort.

## Verwandte Algorithmen in cOde(n)

- **[sort_03 - Insertion Sort](sort_03_insertion-sort.md)** — Die Engine für die kleinen Runs.
- **[sort_04 - Merge Sort](sort_04_merge-sort.md)** — Die Engine für das Kombinieren der Runs.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*