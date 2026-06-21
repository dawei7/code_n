# Maximale Anzahl an Zügen für einen Halt

| | |
|---|---|
| **ID** | `greedy_12` |
| **Kategorie** | greedy |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **GeeksForGeeks Äquivalent** | [Maximum trains for which stoppage can be provided](https://www.geeksforgeeks.org/maximum-trains-stoppage-can-provided/) |

## Problemstellung

Gegeben sind `N` Züge mit ihren jeweiligen `[arrival_time, departure_time, platform_number]`.
Ein Bahnhof verfügt über `P` Bahnsteige. Ein Bahnsteig kann jeweils nur einen Zug abfertigen. Zwei Züge auf demselben Bahnsteig sind konfliktfrei, wenn departure\_time[train_1] \le arrival\_time[train_2] gilt.
Ermitteln Sie die maximale Anzahl an Zügen, die erfolgreich am Bahnhof halten können, ohne dass es zu Konflikten kommt. (Falls ein Zug auf seinem zugewiesenen Bahnsteig einen Konflikt verursacht, fährt er ohne Halt am Bahnhof vorbei).

**Eingabe:** Anzahl der Bahnsteige `P` und eine Liste von `N` Zügen, wobei jeder Zug als `(arrival, departure, platform)` definiert ist.
**Ausgabe:** Eine Ganzzahl, die die maximale Anzahl der Züge repräsentiert, die halten können.

## Wann ist dieses Problem zu verwenden?

- Wenn Sie auf ein Aktivitätsauswahlproblem (Activity Selection) stoßen, das in mehrere unabhängige "Buckets" oder "Kanäle" unterteilt ist.

## Ansatz

**1. Die Erkenntnis der "unabhängigen Buckets":**
Dieses Problem klingt auf den ersten Blick wie das "Minimum Meeting Rooms"-Problem. Es gibt jedoch einen entscheidenden Haken! Die Züge sind fest an bestimmte Bahnsteige gebunden. Zug A ist Bahnsteig 1 zugewiesen. Wir können Zug A NICHT einfach auf Bahnsteig 2 verlegen, nur weil Bahnsteig 1 belegt ist!
Da die Bahnsteige sich gegenseitig ausschließen und Züge nicht neu zugewiesen werden können, handelt es sich hierbei nicht um ein einziges großes Problem, sondern um `P` vollständig unabhängige, kleinere Probleme!

**2. Aktivitätsauswahl pro Bahnsteig:**
Für einen einzelnen Bahnsteig lautet das Problem buchstäblich: "Gegeben X Züge mit Start- und Endzeiten, wählen Sie die maximale Anzahl an sich nicht überschneidenden Zügen aus."
Dies ist die exakte Definition des **Activity Selection (`greedy_01`)** Algorithmus!

**3. Der Algorithmus:**
1. Erstellen Sie eine 2D-Liste `platforms_list` der Größe `P+1` (unter Verwendung einer 1-basierten Indizierung zur Vereinfachung).
2. Iterieren Sie durch die `N` Züge und fügen Sie das Tupel `(arrival, departure)` der spezifischen Unterliste `platforms_list[train.platform]` hinzu.
3. Initialisieren Sie einen globalen `count = 0`.
4. Durchlaufen Sie jeden einzelnen Bahnsteig von 1 bis `P`.
5. Sortieren Sie die Unterliste jedes Bahnsteigs nach der **Abfahrtszeit** (Endzeit).
6. Führen Sie die standardmäßige Greedy-Logik der Aktivitätsauswahl aus: Wählen Sie den ersten Zug. Iterieren Sie dann durch den Rest. Wenn die Ankunftszeit des nächsten Zuges \ge der Abfahrtszeit des zuletzt gewählten Zuges ist, wählen Sie ihn aus und aktualisieren Sie den Tracker! Erhöhen Sie `count`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for greedy_12: Max Trains for Stoppage.

A single platform can hold one train at a time. Given arrival
and departure times for n trains, find the maximum number that
can be served without overlap. Greedy: sort by departure, accept
a train iff its arrival is after the last accepted departure.
O(n log n) for the sort.
"""


def solve(arrivals, departures, n):
    if n == 0:
        return 0
    order = sorted(range(n), key=lambda i: (departures[i], arrivals[i]))
    count = 0
    last_departure = -1
    for i in order:
        if arrivals[i] >= last_departure:
            count += 1
            last_departure = departures[i]
    return count
```

</details>

## Durchlauf

`P = 2`. Züge: `T1(10:00, 10:30, p=1)`, `T2(10:10, 10:20, p=1)`, `T3(10:25, 10:40, p=1)`, `T4(11:00, 11:30, p=2)`.
Konvertierung der Zeiten in Ganzzahlen zur Vereinfachung: `T1(1000, 1030, 1)`, `T2(1010, 1020, 1)`, `T3(1025, 1040, 1)`, `T4(1100, 1130, 2)`.

1. **Züge in Buckets sortieren:**
   - `Bahnsteig 1`: `[(1000, 1030), (1010, 1020), (1025, 1040)]`.
   - `Bahnsteig 2`: `[(1100, 1130)]`.

2. **Verarbeitung von Bahnsteig 1:**
   - Sortierung nach Abfahrt: `[(1010, 1020), (1000, 1030), (1025, 1040)]`.
   - Ersten wählen: `(1010, 1020)`. `count = 1`. `last_dep = 1020`.
   - Prüfung `(1000, 1030)`: `1000 >= 1020` NEIN.
   - Prüfung `(1025, 1040)`: `1025 >= 1020` JA. `count = 2`. `last_dep = 1040`.
   - Bahnsteig 1 ergibt `2` Züge.

3. **Verarbeitung von Bahnsteig 2:**
   - Sortierung nach Abfahrt: `[(1100, 1130)]`.
   - Ersten wählen. `count = 1`.
   - Bahnsteig 2 ergibt `1` Zug.

Ergebnis: `total_trains = 2 + 1 = 3`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N + P)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N + P)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(N + P)$ |

Das Einordnen der Züge in Buckets benötigt $O(N)$.
Sortieren der Unterlisten: Im schlechtesten Fall sind alle N Züge einem einzigen Bahnsteig zugewiesen. Das Sortieren dieses Bahnsteigs benötigt $O(N \log N)$.
Die Verarbeitung der Unterlisten benötigt $O(N)$ über alle Bahnsteige hinweg.
Daher ist die Zeitkomplexität strikt durch den Sortierschritt begrenzt: $O(N \log N)$.
Die Platzkomplexität beträgt $O(N + P)$, um das 2D-Array für die Buckets zu verwalten, das die N Zug-Tupel enthält.

## Varianten & Optimierungen

- **Minimale Anzahl benötigter Bahnsteige:** Eine deutlich schwierigere Variante, bei der Züge KEINE vorab zugewiesenen Bahnsteige haben und Sie die minimale Anzahl an dynamischen Bahnsteigen berechnen müssen, sodass 0 Züge abgewiesen werden. Dies wird gelöst, indem alle Ankunfts- und Abfahrtszeiten in zwei sortierte Arrays getrennt werden und mittels Two Pointers die maximale gleichzeitige Überschneidung verfolgt wird (oft als Meeting Rooms II Problem bezeichnet).

## Anwendungen in der Praxis

- **Flughafen-Start- und Landebahnplanung:** Start- und Landebahnen (Bahnsteige) werden bestimmten Flugklassen zugewiesen (z. B. schwere Großraumflugzeuge vs. leichte Propellermaschinen). Fluglotsen müssen den Durchsatz auf jeder physischen Landebahn unabhängig maximieren.

## Verwandte Algorithmen in cOde(n)

- **[greedy_01 - Activity Selection](greedy_01_activity-selection.md)** — Der buchstäblich exakte Algorithmus, der in der inneren Schleife dieses Problems ausgeführt wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*