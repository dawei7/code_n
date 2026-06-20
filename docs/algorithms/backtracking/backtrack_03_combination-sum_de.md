# Kombinationssumme

| | |
|---|---|
| **ID** | `backtrack_03` |
| **Kategorie** | Backtracking |
| **Komplexität (erforderlich)** | $O(N^(T/M)$) Zeit, $O(T/M)$ Speicherplatz |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Kombinationssumme](https://leetcode.com/problems/combination-sum/) |

## Aufgabenstellung

Gegeben sei ein Array aus **unterschiedlichen** ganzen Zahlen `candidates` und eine Zielzahl `target`, gib eine Liste aller **eindeutigen Kombinationen** von `candidates` zurück, bei denen die Summe der ausgewählten Zahlen `target` ergibt. Die Kombinationen können in beliebiger Reihenfolge zurückgegeben werden.
Dieselbe Zahl darf aus `candidates` **unbegrenzt oft** ausgewählt werden. Zwei Kombinationen sind einzigartig, wenn die Häufigkeit mindestens einer der ausgewählten Zahlen unterschiedlich ist.

**Eingabe:** Ein Array von Ganzzahlen `candidates` und eine Ganzzahl `target`.
**Ausgabe:** Eine Liste von Listen, die gültige Kombinationen darstellen.

## Wann man es verwendet

- Der kanonische Algorithmus für das **Unbounded Knapsack**-Problem, wenn Sie die *tatsächlichen Pfade/Elemente* zurückgeben müssen und nicht nur die mathematische Minimal- oder Maximalanzahl.
- Er testet Ihre Fähigkeit, den Backtracking-Zustand zu verwalten und gleichzeitig die unbegrenzte Wiederverwendung von Elementen zu ermöglichen.

## Vorgehensweise

**1. Der Entscheidungsbaum:**
Da wir Elemente wiederverwenden können, kann sich der Baum theoretisch unendlich verzweigen! Uns interessieren jedoch nur Pfade, deren Summe genau `target` beträgt. Wenn unsere Summe `target` überschreitet, brechen wir die Erkundung dieses Zweigs sofort ab (dies wird als **Pruning** bezeichnet).
Um zudem doppelte Kombinationen (z. B. `[2, 2, 3]` und `[2, 3, 2]`) zu vermeiden, MÜSSEN wir eine Reihenfolge festlegen. Dies erreichen wir durch die Führung eines `start_index`. Wir dürfen nur das aktuelle Element oder Elemente *rechts* davon auswählen. Wir dürfen niemals nach links zurückblicken!

**2. Der Backtracking-Zustand:**
`backtrack(start_index, current_combo, current_sum)`:
- `start_index`: Verhindert das Zurückblicken (verhindert `[3, 2, 2]`).
- `current_combo`: Die bisher ausgewählten Zahlen.
- `current_sum`: Die Summe der ausgewählten Zahlen.

**3. Basisfälle (das Ausdünnen):**
- Wenn `current_sum == target`: Wir haben eine gültige Kombination gefunden! Eine Kopie an `result` anhängen und zurückkehren.
- Wenn `current_sum > target`: Wir haben das Ziel überschritten. Dieser Zweig ist tot. Sofort zurückkehren!

**4. Der rekursive Schritt:**
Schleife `i` von `start_index` bis `len(candidates)`.
- **Entscheidung treffen:** Füge `candidates[i]` zu unserer Kombination hinzu und summiere.
- **Rekursion:** Rufe `backtrack(i, combo, sum)` auf.
  *(WICHTIG: Beachte, dass wir `i` übergeben, NICHT `i + 1`! Da wir `candidates[i]` unendlich oft wiederverwenden dürfen, müssen wir für die nächste Ebene des Baums bei `i` bleiben).*
- **Zurückverfolgen:** Das Element entfernen und von der Summe subtrahieren.

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

## Schritt-für-Schritt-Anleitung

`candidates = [2, 3]`, `target = 5`.

1. `backtrack(0, [], 0)`:
   - Schleife `i=0`(`num=2`).
     - `backtrack(0, [2], 2)`:
 - Schleife `i=0`(`num=2`).
         - `backtrack(0, [2, 2], 4)`:
 - Schleife `i=0`(`num=2`).
 - `backtrack(0, [2, 2, 2], 6)`: `6 > 5`. Beschneiden! Zurück.
 - Schleife `i=1`(`num=3`).
 - `backtrack(1, [2, 2, 3], 7)`: `7 > 5`. Beschneiden! Zurück.
       - Schleife `i=1`(`num=3`).
 - `backtrack(1, [2, 3], 5)`: `5 == 5`. ERFOLG! Anfügen `[2, 3]`. Zurück.
   - Schleife `i=1`(`num=3`).
 - `backtrack(1, [3], 3)`:
 - Schleife `i=1`(`num=3`).
         - `backtrack(1, [3, 3], 6)`: `6 > 5`. Beschneiden! Zurück.

Ergebnis: `[[2, 3]]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^(T/M)$) | $O(T/M)$ |
| **Durchschnittlicher Fall** | $O(N^(T/M)$) | $O(T/M)$ |
| **Schlechtester Fall** | $O(N^(T/M)$) | $O(T/M)$ |

*Dabei ist N die Anzahl der Kandidaten, T der Zielwert und M der Minimalwert im Kandidaten-Array.*
Die maximale Tiefe des rekursiven Baums beträgt T/M (z. B. wenn das Ziel 10 ist und die kleinste Münze 1, beträgt die Tiefe 10).
An jedem Knoten verzweigt sich der Baum N-mal.
Die Gesamtzeitkomplexität ist äußerst grob geschätzt und wird ungefähr durch $O(N^{\frac{T}{M}})$ begrenzt.
Die Platzkomplexität beträgt $O(T/M)$, entsprechend der maximalen Tiefe des rekursiven Aufrufstapels.

## Varianten & Optimierungen

- **Sortieroptimierung:** Wenn du das `candidates`-Array vor dem Start aufsteigend sortierst, kannst du eine unglaublich wirkungsvolle Pruning-Methode anwenden! Innerhalb der `for`-Schleife kannst du, falls `current_sum + candidates[i] > target`, die gesamte `for`-Schleife sofort `break` überspringen, da alle nachfolgenden Kandidaten noch größer wären!
- **Kombinationssumme II (keine Wiederverwendung, Duplikate in der Eingabe):** Wenn Kandidaten nur EINMAL verwendet werden dürfen, übergebe `i + 1` in der Rekursion. Wenn die Eingabe doppelte Zahlen enthält (z. B. `[10, 1, 2, 7, 6, 1, 5]`), musst du zuerst sortieren und `if i > start_index and candidates[i] == candidates[i-1]: continue` hinzufügen, um doppelte Ergebnismengen zu vermeiden!
- **Münzwechsel:** Wenn in der Aufgabe NUR nach der *minimalen Anzahl an Münzen* gefragt wird, verwende KEIN Backtracking! Das ist ein Problem des unbegrenzten Rucksacks, das mit einem 1D-DP-Array in streng $O(N x T)$ Zeit gelöst werden sollte.

## Anwendungen in der Praxis

- **Abstimmung von Finanzbüchern:** Ermittlung der spezifischen Kombination wiederkehrender, unbegrenzter Transaktionen (z. B. Einzahlungen von 5 $), deren Summe einer beobachteten Diskrepanz in einem Buchhaltungsprotokoll entspricht.

## Verwandte Algorithmen in cOde(n)

- **[backtrack_01 - Teilmengen](backtrack_01_subset-sum-decision.md)** — Das grundlegende Problem, bei dem Elemente nur einmal verwendet werden dürfen.
- **[dp_17 – Partition Equal Subset Sum](../dynamic/dp_17_partition-equal-subset-sum.md)** – Das identische Problem, bei dem jedoch anstelle der tatsächlichen Pfade ein boolescher Wert zurückgegeben wird.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
