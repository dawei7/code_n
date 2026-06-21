# Subsets (Potenzmenge)

| | |
|---|---|
| **ID** | `backtrack_01` |
| **Kategorie** | Backtracking |
| **Komplexität (erforderlich)** | $O(N * 2^N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Subsets](https://leetcode.com/problems/subsets/) |

## Problemstellung

Gegeben ist ein Array `nums` von **eindeutigen** Ganzzahlen. Geben Sie alle möglichen Teilmengen (die Potenzmenge) zurück.
Die Lösungsmenge darf keine doppelten Teilmengen enthalten. Die Lösung kann in einer beliebigen Reihenfolge zurückgegeben werden.

**Eingabe:** Ein Array `nums` von Ganzzahlen.
**Ausgabe:** Eine Liste von Listen, wobei jede innere Liste eine gültige Teilmenge darstellt.

## Wann man es verwendet

- Das absolute Fundament von Backtracking-Algorithmen.
- Verwenden Sie es, um jede mögliche Kombination oder Gruppierung von Elementen zu generieren, ohne Permutationen (Reihenfolge) zu berücksichtigen.

## Ansatz

**1. Der Entscheidungsbaum:**
Für jedes Element im Array haben wir genau zwei Möglichkeiten:
1. **Einschließen:** Das Element in unsere aktuelle Teilmenge aufnehmen.
2. **Ausschließen:** Das Element aus unserer aktuellen Teilmenge weglassen.
Da es N Elemente gibt und für jedes 2 Möglichkeiten bestehen, wird unser Entscheidungsbaum genau 2^N Blätter haben (die Gesamtzahl der Teilmengen).

**2. Der Backtracking-Zustand:**
Wir definieren eine rekursive Funktion `backtrack(index, current_subset)`:
- `index`: Für welches Element aus `nums` treffen wir gerade eine Entscheidung?
- `current_subset`: Eine Liste, die die bisher getroffenen Entscheidungen sammelt.

**3. Basisfall:**
Wenn `index == len(nums)`, bedeutet dies, dass wir für JEDES Element im Array eine Entscheidung (Einschließen/Ausschließen) getroffen haben. Wir haben einen Blattknoten erreicht!
Wir erstellen einen *Snapshot* (Kopie) von `current_subset` und fügen ihn unserer globalen `result`-Liste hinzu. Danach kehren wir zurück, um dem Baum zu ermöglichen, weiter zu explorieren.

**4. Der rekursive Schritt (Backtracking):**
Innerhalb unserer Funktion führen wir unsere zwei Entscheidungen aus:
- **Entscheidung 1 (Einschließen):** Füge `nums[index]` zu `current_subset` hinzu. Rekursion mit `index + 1`.
- **Entscheidung 2 (Ausschließen):** Bevor wir die Rekursion fortsetzen, MÜSSEN wir die gerade getroffene Entscheidung "rückgängig machen"! Wir entfernen `nums[index]` mittels `pop` aus `current_subset` (dies ist die definierende Aktion des Backtrackings). Danach führen wir die Rekursion mit `index + 1` aus.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for backtrack_01: Subset Sum (decision).

Classic backtracking: at each step, try including or excluding
the current element. Prune when the running sum is past the
target. Return True iff a subset sums exactly to target.
"""


def solve(arr, target, n):
    if n == 0:
        return target == 0

    def helper(i, remaining):
        if remaining == 0:
            return True
        if i == n or remaining < 0:
            return False
        # Include arr[i] or skip it.
        return helper(i + 1, remaining - arr[i]) or helper(i + 1, remaining)

    return helper(0, target)
```

</details>

## Durchlauf

`nums = [1, 2]`. N=2.

1. `backtrack(0, [])`:
   - Einschließen 1 -> `subset = [1]`. Aufruf `backtrack(1, [1])`.
     - Einschließen 2 -> `subset = [1, 2]`. Aufruf `backtrack(2, [1, 2])`.
       - Basisfall! Füge `[1, 2]` zum Ergebnis hinzu. Rückkehr.
     - Backtrack -> `pop 2`. `subset = [1]`.
     - Ausschließen 2 -> Aufruf `backtrack(2, [1])`.
       - Basisfall! Füge `[1]` zum Ergebnis hinzu. Rückkehr.
   - Backtrack -> `pop 1`. `subset = []`.
   - Ausschließen 1 -> Aufruf `backtrack(1, [])`.
     - Einschließen 2 -> `subset = [2]`. Aufruf `backtrack(2, [2])`.
       - Basisfall! Füge `[2]` zum Ergebnis hinzu. Rückkehr.
   - Backtrack -> `pop 2`. `subset = []`.
   - Ausschließen 2 -> Aufruf `backtrack(2, [])`.
       - Basisfall! Füge `[]` zum Ergebnis hinzu. Rückkehr.

Ergebnis: `[[1, 2], [1], [2], []]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N * 2^N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N * 2^N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N * 2^N)$ | $O(N)$ |

Es gibt genau 2^N Knoten/Blätter. An jedem Blatt benötigt das Kopieren von `current_subset` $O(N)$ Zeit. Die gesamte Zeitkomplexität beträgt strikt $O(N * 2^N)$.
Die Platzkomplexität beträgt $O(N)$ für den Rekursions-Stack und die `current_subset`-Liste. (Das Ergebnis-Array, das $O(N * 2^N)$ Platz beansprucht, wird bei der Analyse des zusätzlichen Speicherbedarfs üblicherweise nicht mitgezählt).

## Varianten & Optimierungen

- **Subsets II (Mit Duplikaten):** Was, wenn `nums = [1, 2, 2]`? Der Standardalgorithmus würde die Teilmenge `[1, 2]` doppelt generieren! Um dies zu beheben: 1. Sortieren Sie das Array zuerst. 2. Wenn Sie den "Ausschließen"-Zweig ausführen, verwenden Sie eine `while`-Schleife, um alle nachfolgenden Elemente zu überspringen, die identisch mit `nums[index]` sind.
- **Bitmask-Iteration:** Sie können die Rekursion komplett vermeiden! Eine Binärzahl von `0` bis `2^N - 1` repräsentiert perfekt jede Einschließen/Ausschließen-Entscheidung. Das i-te Bit der Zahl bestimmt, ob `nums[i]` in der Teilmenge enthalten ist. Dies erfordert $O(N * 2^N)$ Zeit und $O(1)$ Platz, was es für die wettbewerbsorientierte Programmierung deutlich überlegen macht.

## Anwendungen in der Praxis

- **Datenbank-Abfrageoptimierung:** Generierung der Potenzmenge von Join-Bedingungen, um die Kosten aller möglichen Ausführungspläne für Unterabfragen zu bewerten.
- **Merkmalsauswahl (Machine Learning):** Testen aller möglichen Teilmengen von Variablen, um das Modell mit der höchsten Vorhersagegenauigkeit zu finden.

## Verwandte Algorithmen in cOde(n)

- **[backtrack_02 - Permutations](backtrack_02_permutations.md)** — Der Unterschied zwischen Teilmengen (Reihenfolge spielt keine Rolle) und Permutationen (Reihenfolge spielt eine Rolle).
- **[dp_06 - Subset Sum](../dynamic/dp_06_subset-sum.md)** — Wenn Sie nur wissen müssen, OB eine Teilmenge existiert, die eine Zielsumme ergibt, ist ein $O(N^2)$ DP-Array unendlich viel schneller als $O(2^N)$ Backtracking!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für wettbewerbsorientierte Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*