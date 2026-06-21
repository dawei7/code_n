# Combination Sum

| | |
|---|---|
| **ID** | `backtrack_03` |
| **Kategorie** | Backtracking |
| **Komplexität (erforderlich)** | $O(N^(T/M)$) Zeit, $O(T/M)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Combination Sum](https://leetcode.com/problems/combination-sum/) |

## Problemstellung

Gegeben ist ein Array aus **unterschiedlichen** Ganzzahlen `candidates` und eine Ziel-Ganzzahl `target`. Geben Sie eine Liste aller **eindeutigen Kombinationen** von `candidates` zurück, deren Summe `target` ergibt. Die Kombinationen können in beliebiger Reihenfolge zurückgegeben werden.
Dieselbe Zahl aus `candidates` darf **unbegrenzt oft** gewählt werden. Zwei Kombinationen sind eindeutig, wenn sich die Häufigkeit mindestens einer der gewählten Zahlen unterscheidet.

**Eingabe:** Ein Ganzzahl-Array `candidates` und eine Ganzzahl `target`.
**Ausgabe:** Eine Liste von Listen, die gültige Kombinationen repräsentieren.

## Wann man es verwendet

- Der kanonische Algorithmus für das **Unbounded Knapsack**-Problem, wenn Sie die *tatsächlichen Pfade/Elemente* zurückgeben müssen, anstatt nur die mathematische minimale oder maximale Anzahl.
- Es testet Ihre Fähigkeit, den Backtracking-Zustand zu verwalten, während die unendliche Wiederverwendung von Elementen erlaubt ist.

## Ansatz

**1. Der Entscheidungsbaum:**
Da wir Elemente wiederverwenden können, kann der Baum theoretisch unendlich verzweigen! Wir interessieren uns jedoch nur für Pfade, die exakt `target` ergeben. Wenn unsere Summe `target` überschreitet, hören wir sofort auf, diesen Zweig zu untersuchen (dies nennt man **Pruning**).
Um zudem die Generierung doppelter Kombinationen (z. B. `[2, 2, 3]` und `[2, 3, 2]`) zu vermeiden, MÜSSEN wir eine Reihenfolge erzwingen. Dies erreichen wir durch die Beibehaltung eines `start_index`. Wir dürfen nur das aktuelle Element oder Elemente *rechts davon* wählen. Wir dürfen niemals nach links zurückblicken!

**2. Der Backtracking-Zustand:**
`backtrack(start_index, current_combo, current_sum)`:
- `start_index`: Verhindert das Zurückblicken (verhindert `[3, 2, 2]`).
- `current_combo`: Die bisher gewählten Zahlen.
- `current_sum`: Die Summe der gewählten Zahlen.

**3. Basisfälle (Das Pruning):**
- Wenn `current_sum == target`: Wir haben eine gültige Kombination gefunden! Hängen Sie eine Kopie an `result` an und kehren Sie zurück.
- Wenn `current_sum > target`: Wir sind über das Ziel hinausgeschossen. Dieser Zweig ist ungültig. Kehren Sie sofort zurück!

**4. Der rekursive Schritt:**
Schleife `i` von `start_index` bis `len(candidates)`.
- **Wahl treffen:** Fügen Sie `candidates[i]` zu unserer Kombination und Summe hinzu.
- **Rekursion:** Rufen Sie `backtrack(i, combo, sum)` auf.
  *(KRITISCH: Beachten Sie, dass wir `i` übergeben, NICHT `i + 1`! Da wir `candidates[i]` unendlich oft wiederverwenden dürfen, müssen wir für die nächste Tiefe des Baums bei `i` bleiben).*
- **Backtrack:** Entfernen Sie das Element (pop) und subtrahieren Sie es von der Summe.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for backtrack_03: Combination Sum.

Given a list of positive integers and a target, return every
unique combination that sums to target. Each input element may
be used any number of times. Sort the input first and always
recurse forward (i >= start) to avoid duplicates.
"""


def solve(candidates, target, n):
    candidates = sorted(candidates)
    result = []

    def helper(start, remaining, path):
        if remaining == 0:
            result.append(list(path))
            return
        if start == n or remaining < 0:
            return
        for i in range(start, n):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            helper(i, remaining - candidates[i], path)
            path.pop()

    helper(0, target, [])
    return result
```

</details>

## Durchlauf

`candidates = [2, 3]`, `target = 5`.

1. `backtrack(0, [], 0)`:
   - Schleife `i=0` (`num=2`).
     - `backtrack(0, [2], 2)`:
       - Schleife `i=0` (`num=2`).
         - `backtrack(0, [2, 2], 4)`:
           - Schleife `i=0` (`num=2`).
             - `backtrack(0, [2, 2, 2], 6)`: `6 > 5`. Pruning! Zurückkehren.
           - Schleife `i=1` (`num=3`).
             - `backtrack(1, [2, 2, 3], 7)`: `7 > 5`. Pruning! Zurückkehren.
       - Schleife `i=1` (`num=3`).
         - `backtrack(1, [2, 3], 5)`: `5 == 5`. ERFOLG! `[2, 3]` anhängen. Zurückkehren.
   - Schleife `i=1` (`num=3`).
     - `backtrack(1, [3], 3)`:
       - Schleife `i=1` (`num=3`).
         - `backtrack(1, [3, 3], 6)`: `6 > 5`. Pruning! Zurückkehren.

Ergebnis: `[[2, 3]]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^(T/M)$) | $O(T/M)$ |
| **Durchschnittlicher Fall** | $O(N^(T/M)$) | $O(T/M)$ |
| **Schlechtester Fall** | $O(N^(T/M)$) | $O(T/M)$ |

*Wobei N die Anzahl der Kandidaten ist, T der Zielwert und M der kleinste Wert im candidates-Array.*
Die maximale Tiefe des rekursiven Baums beträgt T/M (z. B. wenn das Ziel 10 ist und die kleinste Münze 1, beträgt die Tiefe 10).
An jedem Knoten verzweigt der Baum N-mal.
Die gesamte Zeitkomplexität ist sehr grob und wird ungefähr durch $O(N^{\frac{T}{M}})$ begrenzt.
Die Platzkomplexität beträgt $O(T/M)$, was der maximalen Tiefe des rekursiven Aufruf-Stacks entspricht.

## Varianten & Optimierungen

- **Sortier-Optimierung:** Wenn Sie das `candidates`-Array vor Beginn aufsteigend sortieren, können Sie ein extrem effektives Pruning anwenden! Wenn innerhalb der `for`-Schleife `current_sum + candidates[i] > target` gilt, können Sie die gesamte `for`-Schleife sofort mit `break` abbrechen, da alle nachfolgenden Kandidaten noch größer sein werden!
- **Combination Sum II (Keine Wiederverwendung, Duplikate in der Eingabe):** Wenn Kandidaten nur EINMAL verwendet werden dürfen, übergeben Sie `i + 1` in der Rekursion. Wenn die Eingabe doppelte Zahlen enthält (z. B. `[10, 1, 2, 7, 6, 1, 5]`), müssen Sie zuerst sortieren und `if i > start_index and candidates[i] == candidates[i-1]: continue` hinzufügen, um doppelte Ergebnismengen zu verhindern!
- **Coin Change:** Wenn die Frage NUR nach der *minimalen Anzahl an Münzen* fragt, verwenden Sie KEIN Backtracking! Dies ist ein Unbounded Knapsack-Problem, das mit einem 1D-DP-Array in strikter $O(N x T)$-Zeit gelöst werden sollte.

## Anwendungen in der Praxis

- **Abgleich von Finanzbuchhaltungen:** Finden der spezifischen Kombination von wiederkehrenden, unbegrenzten Transaktionen (z. B. $5 Einzahlungen), die sich zu einer beobachteten Diskrepanz in einem Buchhaltungsprotokoll summieren.

## Verwandte Algorithmen in cOde(n)

- **[backtrack_01 - Subsets](backtrack_01_subset-sum-decision.md)** — Das grundlegende Problem, bei dem Elemente nur einmal verwendet werden können.
- **[dp_17 - Partition Equal Subset Sum](../dynamic/dp_17_partition-equal-subset-sum.md)** — Das identische Problem, gibt jedoch einen booleschen Wert anstelle der tatsächlichen Pfade zurück.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*