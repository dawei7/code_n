# Gas Station (Circular Tour)

| | |
|---|---|
| **ID** | `greedy_06` |
| **Kategorie** | greedy |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Gas Station](https://leetcode.com/problems/gas-station/) |

## Problemstellung

Es gibt `N` Tankstellen entlang einer kreisförmigen Route. Gegeben sind zwei Integer-Arrays:
1. `gas[i]`: Die Menge an Benzin, die an Station i verfügbar ist.
2. `cost[i]`: Die Menge an Benzin, die benötigt wird, um von Station i zur nächsten Station (i+1) \pmod N zu gelangen.

Du startest mit einem leeren Tank. Gib den Index der Start-Tankstelle zurück, falls du die Strecke genau einmal im Uhrzeigersinn umrunden kannst. Falls dies unmöglich ist, gib `-1` zurück.
*Bedingung:* Falls eine Lösung existiert, ist sie garantiert eindeutig.

**Eingabe:** Zwei Arrays `gas` und `cost` der Größe `N`.
**Ausgabe:** Ein Integer, der den Start-Index repräsentiert, oder `-1`.

## Wann man es verwendet

- Dies ist die klassische "$O(N^2)$ zu $O(N)$ Greedy Single-Pass"-Interviewfrage.
- Immer wenn ein Problem das Abschließen einer kreisförmigen Sequenz beinhaltet, bei der kumulative Ressourcengewinne die kumulativen Ressourcenverbräuche übersteigen müssen.

## Ansatz

**1. Der Brute-Force-Ansatz:**
Starte bei Index 0. Simuliere die Fahrt im Kreis. Wenn dir das Benzin ausgeht, halte an, verschiebe den Startpunkt auf Index 1 und simuliere den Kreis erneut. Dies benötigt $O(N^2)$ Zeit.

**2. Greedy-Erkenntnis 1 (Die Unmöglichkeitsbedingung):**
Wenn die gesamte verfügbare Benzinmenge auf der gesamten Route strikt KLEINER ist als die Gesamtkosten für die Fahrt der gesamten Route, ist eine Rundreise mathematisch unmöglich, egal wo man startet!
Daher: Wenn `sum(gas) < sum(cost)`, gib sofort `-1` zurück.
*Folgerung:* Wenn `sum(gas) >= sum(cost)`, ist die Existenz eines gültigen Startpunkts mathematisch garantiert!

**3. Greedy-Erkenntnis 2 (Die Rücksetzbedingung):**
Angenommen, wir starten bei Station 0 und fahren erfolgreich zu Station 1, 2 und 3. Aber wenn wir versuchen, von 3 nach 4 zu fahren, fällt unser Tank unter 0. Wir sind gescheitert.
Sollten wir versuchen, bei Station 1 zu starten? NEIN!
Da wir bei 0 mit 0 Benzin gestartet sind und bei 1 mit \ge 0 Benzin angekommen sind, ist ein Start bei 1 mit 0 Benzin strikt schlechter! Die exakt gleiche Logik gilt für Station 2 und 3.
**Wenn ein Start bei `A` nicht ausreicht, um `B` zu erreichen, dann wird JEDE Station zwischen `A` und `B` ebenfalls daran scheitern, `B` zu erreichen!**
Der nächste logische Ort für einen Startversuch ist `B + 1`!

**4. Der Single-Pass-Algorithmus:**
Iteriere durch das Array. Führe einen `current_tank` mit.
An jeder Station gilt: `current_tank += gas[i] - cost[i]`.
Wenn `current_tank` unter 0 fällt, haben wir es nicht geschafft, i+1 zu erreichen. Wir setzen unseren `start_index` auf i+1 und setzen `current_tank` auf 0 zurück!
Aufgrund von Erkenntnis 1 gilt: Wenn wir das Array durchlaufen haben und die globale Summe \ge 0 ist, ist der Wert, auf den `start_index` aktuell zeigt, mathematisch garantiert die korrekte Antwort! Wir müssen den "kreisförmigen" Abschluss nicht einmal explizit simulieren!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for greedy_06: Gas Station.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n) time.
"""


def solve(gas, cost, n):
    if sum(gas) < sum(cost):
        return -1
    tank = 0
    start = 0
    for i in range(n):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start
```

</details>

## Durchlauf

`gas = [1, 2, 3, 4, 5]`, `cost = [3, 4, 5, 1, 2]`.

1. `i=0` (gas=1, cost=3). `tank = -2`.
   - `tank < 0`! Reset: `start_index = 1`. `tank = 0`.
2. `i=1` (gas=2, cost=4). `tank = -2`.
   - `tank < 0`! Reset: `start_index = 2`. `tank = 0`.
3. `i=2` (gas=3, cost=5). `tank = -2`.
   - `tank < 0`! Reset: `start_index = 3`. `tank = 0`.
4. `i=3` (gas=4, cost=1). `tank = 3`.
   - `tank >= 0`. Weiterfahren!
5. `i=4` (gas=5, cost=2). `tank = 3 + (5-2) = 6`.
   - `tank >= 0`. Schleife endet.

Überprüfung der Summen:
`total_gas = 15`. `total_cost = 15`.
`15 >= 15`. Gib `start_index = 3` zurück. ✓
*(Start bei Index 3: Benzinverlauf 4->7->6->4->3. Fällt nie unter 0!)*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Der Algorithmus iteriert exakt einmal in einem linearen Durchlauf durch die Arrays. Bei jedem Schritt werden $O(1)$ arithmetische Operationen durchgeführt. Die Zeitkomplexität ist strikt $O(N)$.
Es werden nur primitive Integer-Variablen verwendet (`current_tank`, `total`, `start_index`), daher ist die Platzkomplexität perfekt $O(1)$.

## Varianten & Optimierungen

- **Mehrere gültige Starts:** Das LeetCode-Problem garantiert eine *eindeutige* Lösung. Wenn mehrere Lösungen möglich sind und du alle zurückgeben musst, funktioniert der $O(N)$-Single-Pass-Trick nicht. Du kannst das Array an sich selbst anhängen (`gas + gas`), um einen Kreis zu simulieren, und einen Sliding-Window- oder Two-Pointer-Ansatz verwenden, um alle gültigen Fenster der Größe N in $O(N)$ Zeit zu finden!

## Anwendungen in der Praxis

- **Raumschiff-Orbit-Transfers:** Berechnung des spezifischen Orbit-Eintrittspunkts (Hohmann-Transfer), bei dem die Treibstoffgewinne der Triebwerke (durch gravitative Swing-by-Manöver) die kontinuierlichen Kosten für Lebenserhaltung und Luftwiderstand übersteigen, um einen stabilen Orbit zu erreichen, ohne dass der Treibstoff ausgeht.

## Verwandte Algorithmen in cOde(n)

- **[dp_06 - Kadane's Algorithm](../dynamic/dp_06_kadanes-algorithm.md)** — Exakt dieselbe Logik des "Zurücksetzens auf 0, wenn ein Schwellenwert unterschritten wird", angewandt auf die Suche nach dem Maximum Subarray!
- **[greedy_07 - Jump Game](greedy_07_jump-game.md)** — Ein weiteres Problem, bei dem ein einzelner $O(N)$-Durchlauf einen "Max-Reach"-Zustand verfolgt, der beim Erreichen einer Barriere zurückgesetzt wird oder fehlschlägt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Seiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*