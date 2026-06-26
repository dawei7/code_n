# Cycle Sort

| | |
|---|---|
| **ID** | `sort_11` |
| **Kategorie** | Sortieren |
| **Komplexität (erforderlich)** | $O(N^2)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Missing Number](https://leetcode.com/problems/missing-number/) |

## Problemstellung

Gegeben ist ein Array von Ganzzahlen `arr`. Sortieren Sie das Array in aufsteigender Reihenfolge.
Sie müssen das Array unter Verwendung der absolut theoretischen mathematischen Mindestanzahl an Speicherzugriffen (Schreibvorgängen/Swaps) sortieren.
(D. h.: Wenn ein Element bereits an der richtigen Position ist, sollte es NIEMALS überschrieben oder getauscht werden. Wenn es an der falschen Position ist, sollte es in genau einem Schreibvorgang an seine korrekte Position bewegt werden.)

**Eingabe:** Ein unsortiertes Array von Ganzzahlen `arr`.
**Ausgabe:** Ein sortiertes Array.

## Wann sollte man es verwenden?

- **EEPROM / Flash-Speicher:** Wenn das Schreiben von Daten das Speichermedium physisch beschädigt oder abnutzt. Cycle Sort garantiert die absolut minimale Anzahl an Schreibvorgängen, um die Lebensdauer der Hardware zu verlängern.
- **Das 1-bis-N-Array-Muster:** Ein unglaublich häufiges Muster in Vorstellungsgesprächen, bei dem die Array-Werte perfekt mit den Array-Indizes übereinstimmen (z. B. „Gegeben ist ein Array der Länge N mit Zahlen von 1 bis N, finde die doppelte/fehlende Zahl“). Cycle Sort löst dies in $O(N)$ Zeit!

## Ansatz

**1. Der mathematische Graph-Zyklus:**
Stellen Sie sich vor, jedes Element im Array zeigt mit einem Pfeil auf den Index, an dem es sich theoretisch befinden *sollte*.
Da jedes Element ein einzigartiges Ziel hat und jeder Index nur ein Element aufnehmen kann, bilden die Pfeile perfekt geschlossene Schleifen (Zyklen) über das gesamte Array hinweg!
Wenn ein Element bereits an der richtigen Position ist, zeigt es auf sich selbst (ein Zyklus der Länge 1).

**2. Der Standard $O(N^2)$ Cycle Sort Algorithmus:**
Wir beginnen bei Index `0`. Wir nehmen das Element auf und hinterlassen ein „Loch“.
Wir durchsuchen das gesamte Array, um genau zu zählen, wie viele Elemente kleiner sind als dieses. Wenn es `K` kleinere Elemente gibt, ist seine korrekte Position der Index `K`.
Wir gehen zu Index `K`, nehmen das dort befindliche Element heraus und lassen unser Element in das Loch fallen!
Nun haben wir ein neues Element in der Hand. Wir wiederholen den Vorgang! Wir zählen, wie viele Elemente kleiner sind als dieses, finden seinen korrekten Index, nehmen das dortige Element heraus und lassen unseres hineinfallen.
Wir verfolgen diesen Zyklus von Verschiebungen weiter, bis wir ein Element herausziehen, das an Index `0` gehört! Wir legen es an Index `0` ab und schließen den Zyklus perfekt ab.
Wir gehen zu Index `1` über und wiederholen den Vorgang.

**3. Die 1-bis-N-Optimierung ($O(N)$):**
Wenn das Problem garantiert, dass die Zahlen im Array im Bereich `[1, N]` liegen, MÜSSEN WIR NICHT SCANNEN, um kleinere Elemente zu zählen!
Wenn wir die Zahl `5` in der Hand halten, muss sie mathematisch gesehen an Index `4` gehören!
Der $O(N)$-Scan verwandelt sich in einen direkten $O(1)$-Array-Zugriff!
Wir nehmen einfach `nums[i]`. Ist es an Index `nums[i] - 1`? Wenn nein, tauschen wir es an Index `nums[i] - 1`! Wir tauschen so lange weiter, welche Zahl auch immer bei `nums[i]` landet, bis die korrekte Zahl dort schließlich ankommt. Dann gehen wir zu `i+1` weiter.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_11: Cycle Sort.

In-place, write-optimal sort. For each position, count elements
smaller than it to find its final index, then place the value
there. The displaced value starts a new cycle. O(n^2) time,
O(1) extra space, and at most n-1 writes.
"""


def solve(data, n):
    for cycle_start in range(n - 1):
        item = data[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if data[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        # Skip past duplicates of `item` already at `pos`.
        while item == data[pos]:
            pos += 1
        data[pos], item = item, data[pos]
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if data[i] < item:
                    pos += 1
            while item == data[pos]:
                pos += 1
            data[pos], item = item, data[pos]
    return data
```

</details>

## Durchlauf (1-bis-N optimiert)

`arr = [3, 4, -1, 1]`.

1. `i = 0`: `arr[0]` ist `3`. Es gehört an Index `2`.
   - Tausche `arr[0]` und `arr[2]`.
   - `arr` wird zu `[-1, 4, 3, 1]`.
2. `i = 0` (Warten Sie, wir erhöhen `i` nicht! Wir müssen das neue Element verarbeiten!):
   - `arr[0]` ist `-1`. Außerhalb des Bereichs!
   - `i += 1`.
3. `i = 1`: `arr[1]` ist `4`. Es gehört an Index `3`.
   - Tausche `arr[1]` und `arr[3]`.
   - `arr` wird zu `[-1, 1, 3, 4]`.
4. `i = 1` (Verarbeite neues Element):
   - `arr[1]` ist `1`. Es gehört an Index `0`.
   - Tausche `arr[1]` und `arr[0]`.
   - `arr` wird zu `[1, -1, 3, 4]`.
5. `i = 1` (Verarbeite neues Element):
   - `arr[1]` ist `-1`. Außerhalb des Bereichs!
   - `i += 1`.
6. `i = 2`: `arr[2]` ist `3`. Korrekte Position! `i += 1`.
7. `i = 3`: `arr[3]` ist `4`. Korrekte Position! `i += 1`.
Die Schleife endet. `arr = [1, -1, 3, 4]`. ✓
*(Dies ist die exakte Logik, die verwendet wird, um die erste fehlende positive Ganzzahl in $O(N)$-Zeit zu finden! Die fehlende Ganzzahl ist einfach der erste Index, an dem `arr[i] != i + 1` gilt. In diesem Fall hat Index 1 eine `-1` anstelle einer `2`. Die fehlende positive Zahl ist 2!)*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^2)$ oder $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N^2)$ oder $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N^2)$ oder $O(N)$ | $O(1)$ |

Beim Standard-Cycle-Sort erfordert das Finden der korrekten Position für ein Element einen linearen Scan des restlichen Arrays. Über N Elemente hinweg garantiert dies eine Zeitkomplexität von $O(N^2)$.
Beim 1-bis-N-Cycle-Sort wird der Zielindex durch $O(1)$-Arithmetik berechnet. Da jeder einzelne Tausch physisch genau ein Element an seinen für immer korrekten Platz bringt, kann es höchstens N Tauschvorgänge geben! Auch wenn es eine `while`-Schleife gibt, die `i` nicht inkrementiert, ist die Gesamtzahl der Operationen über die gesamte Ausführung hinweg strikt auf $O(N)$ begrenzt.
Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Find the Duplicate Number:** Wenn das Array N+1 Zahlen im Bereich [1, N] enthält, muss eine Zahl doppelt vorkommen. Wenn Sie den 1-bis-N-Cycle-Sort ausführen, ist das Duplikat das Element, das im allerletzten Index gefangen bleibt!

## Anwendungen in der Praxis

- **NASA / Satelliten-Hardware:** Flash-Speichermodule in Raumsonden für den tiefen Weltraum haben stark begrenzte Schreibzyklen. Um lokale Sensordaten zu sortieren, stellt Cycle Sort eine absolut minimale Abnutzung der Speichersektoren sicher.

## Verwandte Algorithmen in cOde(n)

- **[arrays_06 - Find Missing Positive](../arrays/arrays_06_first-missing-positive.md)** — Das LeetCode-Hard-Problem, das durch die Verwendung der 1-bis-N-Cycle-Sort-Variante trivialisiert wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*