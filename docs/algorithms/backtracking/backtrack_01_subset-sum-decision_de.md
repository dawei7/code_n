# Teilmengen (Potenzmenge)

| | |
|---|---|
| **ID** | `backtrack_01` |
| **Kategorie** | Backtracking |
| **Komplexität (erforderlich)** | $O(N * 2^N)$ Zeit, $O(N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Subsets](https://leetcode.com/problems/subsets/) |

## Aufgabenstellung

Gegeben ist ein Array `nums` aus **eindeutigen** ganzen Zahlen. Gib alle möglichen Teilmengen (die Potenzmenge) zurück.
Die Lösungsmenge darf keine doppelten Teilmengen enthalten. Geben Sie die Lösung in beliebiger Reihenfolge zurück.

**Eingabe:** Ein Array von Ganzzahlen `nums`.
**Ausgabe:** Eine Liste von Listen, wobei jede innere Liste eine gültige Teilmenge ist.

## Anwendungsfälle

- Die absolute Grundlage von Backtracking-Algorithmen.
- Verwende diesen Algorithmus, um jede mögliche Kombination oder Gruppierung von Elementen zu generieren, ohne dabei auf Permutationen (Reihenfolge) zu achten.

## Vorgehensweise

**1. Der Entscheidungsbaum:**
Für jedes Element im Array haben wir genau zwei Möglichkeiten:
1. Das Element in unsere aktuelle Teilmenge **aufnehmen**.
2. Das Element aus unserer aktuellen Teilmenge **ausschließen**.
Da es N Elemente gibt und für jedes zwei Möglichkeiten bestehen, wird unser Entscheidungsbaum genau 2^N Blätter haben (die Gesamtzahl der Teilmengen).

**2. Der Backtracking-Zustand:**
Wir definieren eine rekursive Funktion `backtrack(index, current_subset)`:
- `index`: Über welches Element aus `nums` treffen wir gerade eine Entscheidung?
- `current_subset`: Eine Liste, in der die bisher getroffenen Entscheidungen gesammelt werden.

**3. Basisfall:**
Wenn `index == len(nums)`, bedeutet dies, dass wir für JEDES Element im Array eine Entscheidung (Aufnehmen/Ausschließen) getroffen haben. Wir haben einen Blattknoten erreicht!
Wir erstellen einen *Snapshot* (eine Kopie) von `current_subset` und fügen ihn unserer globalen Liste `result` hinzu. Anschließend kehren wir zurück, damit der Baum die Suche fortsetzen kann.

**4. Der rekursive Schritt (Backtracking):**
Innerhalb unserer Funktion führen wir unsere beiden Optionen aus:
- **Option 1 (Aufnehmen):** Füge `nums[index]` zu `current_subset` hinzu. Führe eine Rekursion zu `index + 1` durch.
- **Option 2 (Ausschluss):** Bevor wir rekursiv fortfahren können, MÜSSEN wir die gerade getroffene Entscheidung „rückgängig machen“! Wir entfernen `nums[index]` aus `current_subset` (dies ist die charakteristische Aktion des Backtracking). Anschließend führen wir eine rekursive Suche nach `index + 1` durch.

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

## Schritt-für-Schritt-Anleitung

`nums = [1, 2]`. N=2.

1. `backtrack(0, [])`:
   - 1 einfügen -> `subset = [1]`. `backtrack(1, [1])` aufrufen.
 - 2 einfügen -> `subset = [1, 2]`. `backtrack(2, [1, 2])` aufrufen.
 - Basisfall! `[1, 2]` an das Ergebnis anhängen. Zurückkehren.
 - Backtracking -> `2` entfernen. `subset = [1]`.
     - 2 ausschließen -> `backtrack(2, [1])` aufrufen.
 - Basisfall! `[1]` an das Ergebnis anhängen. Zurückkehren.
   - Zurückverfolgen -> `1` entfernen. `subset = []`.
   - 1 ausschließen -> `backtrack(1, [])` aufrufen.
 - 2 einbeziehen -> `subset = [2]`. `backtrack(2, [2])` aufrufen.
       - Basisfall! `[2]` an das Ergebnis anhängen. Zurückkehren.
 - Rückverfolgung -> `2` vom Stack nehmen. `subset = []`.
     - 2 ausschließen -> `backtrack(2, [])` aufrufen.
 - Basisfall! `[]` an das Ergebnis anhängen. Zurückkehren.

Ergebnis: `[[1, 2], [1], [2], []]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N * 2^N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N * 2^N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N * 2^N)$ | $O(N)$ |

Es gibt genau 2^N Knoten/Blätter. An jedem Blatt dauert das Kopieren des `current_subset` $O(N)$ Zeit. Die gesamte Zeitkomplexität beträgt streng $O(N x 2^N)$.
Die Platzkomplexität beträgt $O(N)$ für den Rekursionsaufrufstapel und die `current_subset`-Liste. (Das Ausgabearray, das $O(N x 2^N)$ Speicherplatz beansprucht, wird bei der Analyse des Hilfsraums in der Regel nicht berücksichtigt).

## Varianten & Optimierungen

- **Teilmengen II (mit Duplikaten):** Was ist, wenn `nums = [1, 2, 2]`? Der Standardalgorithmus erzeugt doppelte Teilmengen `[1, 2]` zweimal! Um dies zu beheben: 1. Sortiere das Array zunächst. 2. Verwende bei der Ausführung des „Exclude“-Zweigs eine `while`-Schleife, um alle nachfolgenden Elemente zu überspringen, die mit `nums[index]` identisch sind.
- **Bitmasken-Iteration:** Du kannst Rekursion komplett vermeiden! Eine Binärzahl von `0` bis `2^N - 1` stellt jede „Include“- bzw. „Exclude“-Entscheidung perfekt dar. Das i-te Bit der Zahl bestimmt, ob `nums[i]` in der Teilmenge enthalten ist. Dies erfordert $O(N x 2^N)$ Zeit und $O(1)$ Speicherplatz, was diese Methode für den Programmierwettbewerb deutlich überlegen macht.

## Anwendungen in der Praxis

- **Optimierung von Datenbankabfragen:** Erzeugung der Potenzmenge der Join-Bedingungen, um die Kosten aller möglichen Ausführungspläne für Unterabfragen zu bewerten.
- **Merkmalsauswahl (Maschinelles Lernen):** Testen aller möglichen Teilmengen von Variablen, um das Modell mit der höchsten Vorhersagegenauigkeit zu finden.

## Verwandte Algorithmen in cOde(n)

- **[backtrack_02 – Permutationen](backtrack_02_permutations.md)** — Der Unterschied zwischen Teilmengen (Reihenfolge spielt keine Rolle) und Permutationen (Reihenfolge spielt eine Rolle).
- **[dp_06 – Teilmenge-Summe](../dynamic/dp_06_subset-sum.md)** — Wenn man nur wissen muss, OB eine Teilmenge existiert, deren Summe einem Zielwert entspricht, ist ein $O(N^2)$ DP-Array unendlich viel schneller als $O(2^N)$ Backtracking!

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
