# Candy Distribution Problem

| | |
|---|---|
| **ID** | `greedy_08` |
| **Kategorie** | greedy |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Candy](https://leetcode.com/problems/candy/) |

## Problemstellung

Es gibt `N` Kinder, die in einer Reihe stehen. Jedem Kind wird ein Bewertungswert zugewiesen, der in einem Integer-Array `ratings` gegeben ist.
Sie verteilen Süßigkeiten an diese Kinder unter Einhaltung der folgenden Anforderungen:
1. Jedes Kind muss mindestens eine Süßigkeit erhalten.
2. Kinder mit einer höheren Bewertung müssen *mehr* Süßigkeiten erhalten als ihre unmittelbaren Nachbarn.

Finden Sie die absolute Mindestanzahl an Süßigkeiten, die Sie verteilen müssen.

**Eingabe:** Ein Integer-Array `ratings` der Größe `N`.
**Ausgabe:** Ein Integer, der die Mindestanzahl an Süßigkeiten repräsentiert.

## Wann ist es zu verwenden

- Das klassische "Two-Pass Greedy Array Sweep"-Problem.
- Zur Lösung voneinander abhängiger lokaler Beziehungen (bei denen ein Element gleichzeitig von seinem linken und rechten Nachbarn abhängt).

## Ansatz

**1. Das Interdependenz-Problem:**
Wenn wir einfach von links nach rechts iterieren, geben wir Kind 2 möglicherweise mehr Süßigkeiten als Kind 1. Aber was ist, wenn Kind 3 eine niedrigere Bewertung als Kind 2 hat? Wir müssen sicherstellen, dass Kind 2 *auch* mehr Süßigkeiten als Kind 3 hat! Die Anpassung von Kind 2 könnte die Beziehung zu Kind 1 stören!
Der Versuch, sowohl die linken als auch die rechten Beziehungen in einem einzigen Durchlauf zu lösen, ist extrem fehleranfällig.

**2. Die Two-Pass-Lösung (Divide and Conquer der Regeln):**
Anstatt beide Bedingungen gleichzeitig zu lösen, entkoppeln wir sie!
**Pass 1 (Links-nach-Rechts):** Wir achten nur darauf, dass ein Kind mehr Süßigkeiten als sein **LINKER** Nachbar hat.
- Initialisieren Sie ein `candies`-Array mit `1` für jedes Kind.
- Schleife `i` von 1 bis N-1: Wenn `ratings[i] > ratings[i-1]`, setzen Sie `candies[i] = candies[i-1] + 1`.

**Pass 2 (Rechts-nach-Links):** Wir achten nur darauf, dass ein Kind mehr Süßigkeiten als sein **RECHTER** Nachbar hat, *ohne die linke Regel zu verletzen*.
- Schleife `i` von N-2 bis 0: Wenn `ratings[i] > ratings[i+1]`, verdient das Kind mehr Süßigkeiten als der rechte Nachbar.
- **Der Haken:** Was, wenn `candies[i]` aufgrund des ersten Durchlaufs BEREITS größer als `candies[i+1]` ist? Wir wollen den Wert nicht verringern! Wir aktualisieren ihn nur, wenn es notwendig ist: `candies[i] = max(candies[i], candies[i+1] + 1)`.

**3. Das Ergebnis:**
Durch einen Durchlauf, der strikt die linken Nachbarn beachtet, und einen zweiten Rückwärtsdurchlauf, der strikt die rechten Nachbarn beachtet (unter Verwendung von `max`), erfüllt das finale Array perfekt beide Bedingungen! Summieren Sie einfach das Array.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for greedy_08: Candy Distribution.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n) time.
"""


def solve(ratings, n):
    if n == 0:
        return 0
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    total = candies[-1]
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
        total += candies[i]
    return total
```

</details>

## Durchlauf

`ratings = [1, 0, 2, 5, 3]`. Länge 5.
`candies = [1, 1, 1, 1, 1]`.

**Pass 1 (Links nach Rechts):**
- `i=1`: `ratings[1] > ratings[0]`? (0 > 1) NEIN.
- `i=2`: `ratings[2] > ratings[1]`? (2 > 0) JA. `candies[2] = 1 + 1 = 2`.
- `i=3`: `ratings[3] > ratings[2]`? (5 > 2) JA. `candies[3] = 2 + 1 = 3`.
- `i=4`: `ratings[4] > ratings[3]`? (3 > 5) NEIN.
`candies` nach Pass 1: `[1, 1, 2, 3, 1]`.

**Pass 2 (Rechts nach Links):**
- `i=3`: `ratings[3] > ratings[4]`? (5 > 3) JA.
  - `candies[3] = max(3, candies[4] + 1)` -> `max(3, 2) = 3`.
- `i=2`: `ratings[2] > ratings[3]`? (2 > 5) NEIN.
- `i=1`: `ratings[1] > ratings[2]`? (0 > 2) NEIN.
- `i=0`: `ratings[0] > ratings[1]`? (1 > 0) JA.
  - `candies[0] = max(1, candies[1] + 1)` -> `max(1, 2) = 2`.

`candies` nach Pass 2: `[2, 1, 2, 3, 1]`.
Summe = `2 + 1 + 2 + 3 + 1 = 9`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Wir iterieren genau dreimal durch das Array (Links-nach-Rechts-Durchlauf, Rechts-nach-Links-Durchlauf und ein abschließender `sum()`-Durchlauf). Die Operationen bei jedem Schritt sind $O(1)$. Die gesamte Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität beträgt $O(N)$, da wir das `candies`-Array instanziieren müssen, um die Zwischenzustände zwischen den Durchläufen zu speichern.

## Varianten & Optimierungen

- **Single-Pass-Optimierung (Peaks and Valleys):** Es ist technisch möglich, dies mit $O(1)$ Platz und einem einzigen Durchlauf zu lösen, indem man die Steigungen (aufsteigende vs. absteigende Sequenzen) verfolgt. Man zählt die Höhe eines "Aufstiegs" und eines "Abstiegs" und berechnet die benötigten Süßigkeiten mathematisch unter Verwendung von Dreieckszahlen (1+2+3+...). Es ist bekanntermaßen schwierig, dies ohne Fehler bei Randfällen zu programmieren, und wird in Vorstellungsgesprächen normalerweise nicht gegenüber dem Two-Pass-Ansatz erwartet.
- **Trapping Rain Water (`two_pointers_01`):** Verwendet ein nahezu identisches Konzept von "Left Max Array, Right Max Array", um das Wasservolumen zu berechnen, entkoppelt in zwei separate Durchläufe.

## Anwendungen in der Praxis

- **Gehalts-/Bonus-Normalisierung:** Verteilung von Leistungsboni in einer nach Rang geordneten Abteilung, in der Mitarbeiter nur die Gehälter ihrer unmittelbaren Kollegen kennen, um Fairness zu gewährleisten (höherer Rang = höheres Gehalt als Kollegen) und gleichzeitig das Unternehmensbudget zu minimieren.

## Verwandte Algorithmen in cOde(n)

- **[greedy_06 - Gas Station](greedy_06_gas-station.md)** — Ein weiterer Greedy $O(N)$-Sweep-Algorithmus.
- **[two_pointers_01 - Trapping Rain Water](../two_pointers/two_pointers_01_trapping-rain-water.md)** — Die Pre-Computation-Arrays bei Trapping Rain Water nutzen exakt dieselbe entkoppelte Links-nach-Rechts / Rechts-nach-Links-Logik.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*