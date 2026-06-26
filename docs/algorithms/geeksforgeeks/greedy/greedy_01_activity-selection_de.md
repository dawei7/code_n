# Activity Selection Problem

| | |
|---|---|
| **ID** | `greedy_01` |
| **Kategorie** | greedy |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/) |

## Problemstellung

Gegeben sind `N` Aktivitäten mit ihren Start- und Endzeiten. Wählen Sie die maximale Anzahl an Aktivitäten aus, die von einer einzelnen Person durchgeführt werden können, unter der Annahme, dass eine Person immer nur an einer Aktivität gleichzeitig arbeiten kann.
Zwei Aktivitäten `i` und `j` sind konfliktfrei, wenn finish\_time[i] \le start\_time[j] gilt.

**Eingabe:** Zwei Arrays `start[]` und `finish[]`, die die Start- und Endzeiten von `N` Aktivitäten repräsentieren.
**Ausgabe:** Eine Ganzzahl, die die maximale Anzahl der ausführbaren Aktivitäten repräsentiert.

## Wann ist es anzuwenden?

- Jedes Problem, bei dem es darum geht, die maximale Anzahl nicht überlappender Intervalle zu planen (Meetings, Aufgaben, Pair Chains).
- Der absolute Inbegriff eines einführenden Greedy-Algorithmus.

## Ansatz

**1. Die Greedy-Entscheidung:**
Wenn Sie so viele Aktivitäten wie möglich in Ihren Tag packen möchten, welche Aktivität sollten Sie immer zuerst wählen?
- Diejenige, die am frühesten beginnt? Nein, eine Aktivität könnte um 8:00 Uhr beginnen und 10 Stunden dauern, was Ihren ganzen Tag ruinieren würde!
- Die kürzeste Aktivität? Nein, eine kurze Aktivität könnte genau in der Mitte des Tages liegen und Sie dazu zwingen, zwei längere, aber perfekt platzierte Aktivitäten fallen zu lassen.
- **Diejenige, die am frühesten endet!** Je früher eine Aktivität endet, desto mehr "Freizeit" bleibt Ihnen für den Rest des Tages, um weitere Aktivitäten unterzubringen!

**2. Der Algorithmus:**
Kombinieren Sie die Arrays `start[]` und `finish[]` zu einer Liste von Tupeln `(start, finish)`.
Sortieren Sie die Liste der Tupel rein nach ihrer **Endzeit** in aufsteigender Reihenfolge.
Wählen Sie immer die allererste Aktivität in der sortierten Liste.
Iterieren Sie dann durch den Rest der Liste. Wenn die Startzeit einer Aktivität \ge der Endzeit der *zuletzt gewählten Aktivität* ist, wählen Sie diese aus! Aktualisieren Sie Ihre "letzte Endzeit" auf die Endzeit dieser neuen Aktivität.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for greedy_01: Activity Selection.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(start, finish, n):
    pairs = sorted(zip(start, finish), key=lambda p: p[1])
    if not pairs:
        return 0
    count = 1
    last_finish = pairs[0][1]
    for s, f in pairs[1:]:
        if s >= last_finish:
            count += 1
            last_finish = f
    return count
```

</details>

## Durchlauf

`start = [1, 3, 0, 5, 8, 5]`, `finish = [2, 4, 6, 7, 9, 9]`.

1. Zippen und Sortieren nach Endzeit:
   `[(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]`
2. Wähle die erste Aktivität: `(1, 2)`.
   `count = 1`. `last_finish = 2`.
3. Prüfe `(3, 4)`. Start `3 >= 2`? JA!
   `count = 2`. `last_finish = 4`.
4. Prüfe `(0, 6)`. Start `0 >= 4`? NEIN! Überspringen.
5. Prüfe `(5, 7)`. Start `5 >= 4`? JA!
   `count = 3`. `last_finish = 7`.
6. Prüfe `(8, 9)`. Start `8 >= 7`? JA!
   `count = 4`. `last_finish = 9`.
7. Prüfe `(5, 9)`. Start `5 >= 9`? NEIN! Überspringen.

Ergebnis `count = 4`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(N)$ |

Das Zippen der Arrays und das Iterieren durch diese benötigt $O(N)$ Zeit.
Das Sortieren des Arrays von Tupeln benötigt $O(N \log N)$ Zeit.
Daher dominiert der Sortiervorgang. Die Zeitkomplexität beträgt $O(N \log N)$.
Die Platzkomplexität beträgt $O(N)$, um das kombinierte Array von Tupeln zu speichern (obwohl der Platzbedarf $O(1)$ betragen kann, falls die Eingabe bereits als ein einzelnes Array von Objekten vorliegt und ein In-Place-Sortieralgorithmus wie Quicksort/Heapsort verwendet wird).

## Varianten & Optimierungen

- **Nicht überlappende Intervalle (LeetCode 435):** Hier wird nach der minimalen Anzahl an Intervallen gefragt, die *entfernt* werden müssen, damit der Rest nicht überlappt. Dies ist exakt dasselbe Problem in umgekehrter Form! Die Antwort lautet `N - max_activities()`.
- **Minimale Anzahl an Meetingräumen:** Eine berühmte Variation! Wenn Sie gefragt werden, wie viele parallele Räume Sie benötigen, um ALLE Aktivitäten unterzubringen, schlägt das Sortieren nach Endzeit fehl. Stattdessen müssen Sie Start- und Endzeiten in zwei separate sortierte Arrays trennen und einen Two-Pointer-Ansatz (Sliding Window) verwenden, um gleichzeitige Überschneidungen zu verfolgen!

## Anwendungen in der Praxis

- **CPU-Task-Scheduling:** Der Job-Scheduler eines Betriebssystems, der den Durchsatz von Batch-Prozessen auf einer Single-Core-Maschine maximiert.

## Verwandte Algorithmen in cOde(n)

- **[greedy_04 - Job Sequencing Problem](greedy_04_job-sequencing.md)** — Ein etwas fortgeschritteneres Scheduling-Problem, bei dem Jobs Deadlines und monetäre Gewinne haben.
- **[sort_04 - Merge Sort](../sorting/sort_04_merge-sort.md)** — Der $O(N \log N)$ Sortieralgorithmus, der im Hintergrund von `activities.sort()` läuft.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*