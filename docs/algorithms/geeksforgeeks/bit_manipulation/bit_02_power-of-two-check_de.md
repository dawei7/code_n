# Power of Two Check

| | |
|---|---|
| **ID** | `bit_02` |
| **Kategorie** | bit_manipulation |
| **Komplexität (erforderlich)** | $O(1)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Power of Two](https://leetcode.com/problems/power-of-two/) |

## Problemstellung

Gegeben ist eine Ganzzahl `n`. Schreiben Sie eine Funktion, die bestimmt, ob es sich um eine Zweierpotenz handelt.
Eine Ganzzahl `n` ist eine Zweierpotenz, wenn eine Ganzzahl `x` existiert, sodass n == 2^x gilt.

**Eingabe:** Eine Ganzzahl `n`.
**Ausgabe:** Ein Boolean: `True`, falls `n` eine Zweierpotenz ist, andernfalls `False`.

## Anwendung

- Als einzeiliger "Zaubertrick" in Vorstellungsgesprächen, um die Beherrschung von Bitmanipulation auf niedriger Ebene zu demonstrieren.
- Eine grundlegende Eigenschaft, die für die Lösung komplexerer Probleme der Bitmanipulation erforderlich ist.

## Ansatz

**1. Die mathematische Eigenschaft:**
Wie sieht eine Zweierpotenz im Binärsystem aus?
- 2^0 = 1 -> `0001`
- 2^1 = 2 -> `0010`
- 2^2 = 4 -> `0100`
- 2^3 = 8 -> `1000`

Fällt das Muster auf? Eine Zweierpotenz hat im Binärsystem IMMER genau **ein einzelnes `1`-Bit**!

**2. Der bitweise Trick:**
Wir kennen bereits den Algorithmus von Brian Kernighan (`bit_01`)! Die Operation `n & (n - 1)` löscht das am weitesten rechts stehende `1`-Bit von `n`.
Wenn `n` eine Zweierpotenz ist, hat es NUR ein einziges `1`-Bit. Das Löschen dieses am weitesten rechts stehenden `1`-Bits führt daher dazu, dass die Zahl vollständig ausgelöscht wird und genau `0` ergibt!
Wenn `n` KEINE Zweierpotenz ist, hat es mehrere `1`-Bits. Das Löschen eines dieser Bits lässt die anderen intakt, sodass das Ergebnis `> 0` bleibt.

**3. Randfälle:**
Ist `0` eine Zweierpotenz? Nein! Es gibt kein x, für das 2^x = 0 gilt.
Wenn wir jedoch `0 & (0 - 1)` berechnen, ergibt dies in den meisten Programmiersprachen `0`, was unsere Prüfung fälschlicherweise als wahr bestätigen würde! Daher müssen wir explizit sicherstellen, dass `n > 0` gilt, bevor wir die bitweise Operation durchführen.
Ebenso können negative Zahlen in diesem Kontext keine Zweierpotenzen sein.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_02: Power of Two Check.

Return True iff the input n is a power of two.
"""


def solve(n):
    """True iff n is a power of two (n >= 1)."""
    return n > 0 and (n & (n - 1)) == 0
```

</details>

## Durchlauf

**Beispiel 1:** `n = 8` (`1000`).
1. `8 > 0` (True).
2. `n - 1 = 7` (`0111`).
3. `8 & 7` -> `1000 & 0111 = 0000` (`0`).
4. `0 == 0` (True). Ergebnis: `True`. ✓

**Beispiel 2:** `n = 10` (`1010`).
1. `10 > 0` (True).
2. `n - 1 = 9` (`1001`).
3. `10 & 9` -> `1010 & 1001 = 1000` (`8`).
4. `8 == 0` (False). Ergebnis: `False`. ✓

**Beispiel 3:** `n = 0`.
1. `0 <= 0` (True). Gibt sofort `False` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(1)$ |
| **Schlechtester Fall** | $O(1)$ | $O(1)$ |

Dies ist die theoretisch schnellstmögliche Ausführung. Sie erfordert genau eine bedingte Prüfung und eine bitweise `AND`-Operation, die in exakt $O(1)$ CPU-Zyklen abläuft.
Die Platzkomplexität ist strikt $O(1)$.

## Varianten & Optimierungen

- **Viererpotenz:** Gegeben eine Ganzzahl, prüfen Sie, ob es sich um eine Potenz von 4 handelt (4^0, 4^1, 4^2\dots). Eine Potenz von 4 ist IMMER auch eine Zweierpotenz, daher muss sie den Test `(n & (n - 1)) == 0` bestehen. Zusätzlich muss das einzelne `1`-Bit an einer **geraden Position** (0, 2, 4...) stehen. Wir können dies prüfen, indem wir eine bitweise `AND`-Operation mit einer Maske aus alternierenden Bits `01010101...` (`0x55555555`) durchführen.
  `return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) == n`.

## Anwendungen in der Praxis

- **Speicherverwaltung:** Betriebssystem-Kernel und Speicher-Pools (wie `malloc`) runden Speicheranforderungen oft auf die nächste Zweierpotenz auf, um Fragmentierung zu vermeiden. Diese Prüfung verifiziert, ob die Anforderung bereits perfekt ausgerichtet ist.
- **Hash Maps:** Die interne Array-Kapazität einer HashMap (wie Javas `HashMap`) wird immer als Zweierpotenz gehalten, sodass die Modulo-Operation `hash % capacity` stark zu einer blitzschnellen bitweisen `AND`-Operation optimiert werden kann: `hash & (capacity - 1)`.

## Verwandte Algorithmen in cOde(n)

- **[bit_01 - Count Set Bits](bit_01_count-set-bits.md)** — Führt den grundlegenden `n & (n - 1)`-Trick ein, der hier verwendet wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*