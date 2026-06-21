# Lemonade Change

| | |
|---|---|
| **ID** | `greedy_09` |
| **Kategorie** | greedy |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **LeetCode-Äquivalent** | [Lemonade Change](https://leetcode.com/problems/lemonade-change/) |

## Problemstellung

An einem Limonadenstand kostet jede Limonade `5`. Kunden stehen in einer Queue, um bei Ihnen zu kaufen, und bestellen nacheinander.
Jeder Kunde kauft nur eine Limonade und bezahlt entweder mit einem `5`, `10` oder `20` Schein. Sie müssen jedem Kunden das korrekte Wechselgeld herausgeben, sodass die Netto-Transaktion exakt `5` beträgt.
Sie beginnen mit KEINEM Wechselgeld in Ihrer Kasse.
Geben Sie `true` zurück, wenn Sie jedem Kunden das korrekte Wechselgeld geben können, andernfalls `false`.

**Input:** Ein Integer-Array `bills`, wobei `bills[i]` entweder 5, 10 oder 20 ist.
**Output:** Ein Boolean.

## Wann man es verwendet

- Um die einfachste mögliche Anwendung einer Greedy-Entscheidung bei der Stückelung von Geldbeträgen zu demonstrieren.
- Wird oft als Aufwärmübung verwendet, bevor man zu schwierigeren DP-Problemen (Coin Change) übergeht.

## Ansatz

Wir simulieren einfach den Prozess der Bedienung der Kunden, während wir die Anzahl der `5`er und `10`er Scheine in unserer Kasse verfolgen. (Wir müssen `20`er Scheine nicht verfolgen, da wir sie niemals als Wechselgeld verwenden werden).

**1. Der 5er Schein:**
Wenn der Kunde `5` gibt, akzeptieren wir ihn einfach. Kein Wechselgeld erforderlich. Erhöhen Sie unseren `5`er-Zähler.

**2. Der 10er Schein:**
Wenn der Kunde `10` gibt, schulden wir ihm `5` als Wechselgeld.
Wir MÜSSEN ihm einen `5`er Schein geben. Wenn wir keinen haben, geben wir sofort `False` zurück.
Wenn wir einen haben, verringern wir unseren `5`er-Zähler und erhöhen unseren `10`er-Zähler.

**3. Der 20er Schein (Die Greedy-Entscheidung):**
Wenn der Kunde `20` gibt, schulden wir ihm `15` als Wechselgeld.
Es gibt zwei mathematische Möglichkeiten, `15` zu bilden:
1. Ein `10`er Schein und ein `5`er Schein.
2. Drei `5`er Scheine.

**Die Greedy-Entscheidung:** Welche Methode ist strikt besser?
Ein `5`er Schein ist weitaus vielseitiger als ein `10`er Schein! Ein `5`er Schein kann verwendet werden, um Wechselgeld für einen `10`er ODER einen `20`er zu bilden. Ein `10`er Schein ist nutzlos, um Wechselgeld für einen `10`er zu bilden!
Daher sollten wir **immer gierig zuerst unsere 10er Scheine loswerden!**
Wenn wir einen `10`er und einen `5`er haben, geben wir diese heraus.
Wenn wir keinen `10`er haben, sind wir gezwungen, drei `5`er Scheine zu geben.
Wenn wir keine der beiden Kombinationen haben, geben wir `False` zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for greedy_09: Lemonade Change.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n) time.
"""


def solve(bills, n):
    fives = 0
    tens = 0
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives == 0:
                return False
            fives -= 1
            tens += 1
        else:  # 20
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True
```

</details>

## Durchlauf

`bills = [5, 5, 5, 10, 20]`.
`fives = 0`, `tens = 0`.

1. Kunde 1 (5): `fives = 1`.
2. Kunde 2 (5): `fives = 2`.
3. Kunde 3 (5): `fives = 3`.
4. Kunde 4 (10):
   - Schulde 5. Wir haben sie!
   - `fives = 3 - 1 = 2`.
   - `tens = 1`.
5. Kunde 5 (20):
   - Schulde 15.
   - Haben wir einen 10er und einen 5er? Ja! (`tens=1, fives=2`).
   - `tens = 0`. `fives = 1`.

Queue beendet. Gib `True` zurück. ✓

*(Kontrast: Wenn wir die Greedy-Regel nicht verwendet hätten und dem Kunden 5 stattdessen drei 5er gegeben hätten, würde es hier immer noch funktionieren. Aber wenn `bills = [5, 5, 10, 20, 10]` wäre, würde das Herausgeben von drei 5ern für den `20`er dazu führen, dass wir `tens=2, fives=0` hätten, was dazu führen würde, dass wir beim letzten `10`er sofort scheitern!)*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Wir iterieren genau einmal durch das `bills`-Array und führen bei jedem Schritt arithmetische Prüfungen mit $O(1)$ Zeitaufwand durch. Die Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität ist $O(1)$, da wir unabhängig von der Größe des Input-Arrays nur zwei Integer-Variablen (`five_count`, `ten_count`) verfolgen.

## Varianten & Optimierungen

- **Wechselgeld für beliebige Stückelungen:** Wenn die Scheine beliebige Werte wie `[1, 5, 10, 25, 50]` hätten, funktioniert die Greedy-Logik (immer den größtmöglichen Schein zurückgeben, der in den geschuldeten Betrag passt) NUR, wenn das Stückelungssystem "kanonisch" ist (wie bei der US-Währung). Wenn das System nicht-kanonisch ist (z. B. `[1, 3, 4]`), schlägt Greedy fehl und Sie müssen Dynamic Programming (`dp_05`) verwenden.

## Anwendungen in der Praxis

- **Verkaufsautomaten:** Standard-algorithmische Logik, die auf den Mikrocontrollern von physischen Verkaufsautomaten und Kassen läuft, um die minimale Anzahl an physischen Münzen an einen Kunden auszugeben, wodurch die Häufigkeit verringert wird, mit der die Maschine nachgefüllt werden muss.

## Verwandte Algorithmen in cOde(n)

- **[greedy_10 - Minimum Coins](greedy_10_minimum-coins.md)** — Die verallgemeinerte mathematische Version genau dieses Problems unter Verwendung von Standard-Währungsstückelungen.
- **[dp_05 - Coin Change Problem](../dynamic/dp_05_coin-change.md)** — Die Dynamic-Programming-Variante, die erforderlich ist, wenn die Greedy-Logik aufgrund von nicht-standardmäßigen Stückelungen fehlschlägt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*