# Überprüfung der Zweierpotenz

| | |
|---|---|
| **ID** | `bit_02` |
| **Kategorie** | Bitmanipulation |
| **Komplexität (erforderlich)** | $O(1)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Zweierpotenz](https://leetcode.com/problems/power-of-two/) |

## Aufgabenstellung

Gegeben sei eine ganze Zahl `n`. Schreibe eine Funktion, die feststellt, ob es sich um eine Zweierpotenz handelt.
Eine ganze Zahl `n` ist eine Zweierpotenz, wenn es eine ganze Zahl `x` gibt, sodass n == 2^x gilt.

**Eingabe:** Eine ganze Zahl `n`.
**Ausgabe:** Ein boolescher Wert: `True`, wenn `n` eine Zweierpotenz ist, andernfalls `False`.

## Wann man es verwendet

- Als einzeiligen Zaubertrick in Vorstellungsgesprächen, um die Beherrschung der Bitmanipulation auf niedriger Ebene zu demonstrieren.
- Eine grundlegende Eigenschaft, die zum Lösen schwierigerer Aufgaben zur Bitmanipulation erforderlich ist.

## Vorgehensweise

**1. Die mathematische Eigenschaft:**
Wie sieht eine Zweierpotenz im Binärsystem aus?
- 2^0 = 1 -> `0001`
- 2^1 = 2 -> `0010`
- 2^2 = 4 -> `0100`
- 2^3 = 8 -> `1000`

Fällt euch das Muster auf? Eine Zweierpotenz im Binärsystem hat IMMER genau **ein einziges `1` Bit**!

**2. Der bitweise Trick:**
Wir kennen bereits Brian Kernighans Algorithmus (`bit_01`)! Die Operation `n & (n - 1)` löscht das Bit ganz rechts `1` aus `n`.
Wenn `n` eine Zweierpotenz ist, hat sie NUR ein `1` Bit. Daher wird durch das Löschen seines rechtesten `1` Bits die Zahl vollständig ausgelöscht und in genau `0` umgewandelt!
Ist `n` KEINE Zweierpotenz, so hat es mehrere `1` Bits. Das Löschen eines davon lässt die anderen unberührt, sodass das Ergebnis `> 0` lautet.

**3. Grenzfälle:**
Ist `0` eine Zweierpotenz? Nein! Es gibt kein x, für das 2^x = 0 gilt.
Wenn wir jedoch `0 & (0 - 1)` ausführen, ergibt dies in den meisten Sprachen `0`, was unsere Prüfung fälschlicherweise auslösen würde! Daher müssen wir `n > 0` explizit überprüfen, bevor wir die bitweise Operation durchführen.
Ebenso können negative Zahlen in diesem Zusammenhang keine Zweierpotenzen sein.

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

## Schritt-für-Schritt-Anleitung

**Beispiel 1:** `n = 8`(`1000`).
1. `8 > 0` (Wahr).
2. `n - 1 = 7`(`0111`).
3. `8 & 7` -> `1000 & 0111 = 0000`(`0`).
4. `0 == 0` (Wahr). Ergebnis: `True`. ✓

**Beispiel 2:** `n = 10`(`1010`).
1. `10 > 0` (Wahr).
2. `n - 1 = 9`(`1001`).
3. `10 & 9` -> `1010 & 1001 = 1000`(`8`).
4. `8 == 0` (Falsch). Ergebnis: `False`. ✓

**Beispiel 3:** `n = 0`.
1. `0 <= 0` (Wahr). Gibt sofort `False` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(1)$ |
| **Schlechtester Fall** | $O(1)$ | $O(1)$ |

Dies ist die schnellstmögliche theoretische Ausführung. Sie erfordert genau eine bedingte Prüfung und eine bitweise `AND`-Operation und läuft in genau $O(1)$ CPU-Zyklen.
Die Platzkomplexität beträgt streng $O(1)$.

## Varianten & Optimierungen

- **Potenz von 4:** Bei einer gegebenen ganzen Zahl wird geprüft, ob es sich um eine Potenz von 4 handelt (4^0, 4^1, 4^2\dots). Eine Potenz von 4 ist IMMER eine Potenz von 2, daher muss sie den `(n & (n - 1)) == 0`-Test bestehen. Zusätzlich muss das einzelne `1`-Bit an einem **geraden Index** (0, 2, 4...) stehen. Wir können dies überprüfen, indem wir eine bitweise `AND` mit einer Maske aus abwechselnden Bits `01010101...`(`0x55555555`) durchführen.
  `return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) == n`.

## Anwendungen in der Praxis

- **Speicherzuordner:** Betriebssystemkerne und Speicherpools (wie `malloc`) runden Speicheranforderungen oft auf die nächste Zweierpotenz auf, um Fragmentierung zu vermeiden. Diese Prüfung stellt sicher, ob die Anforderung bereits perfekt ausgerichtet ist.
- **Hash-Maps:** Die interne Array-Kapazität einer HashMap (wie in Java `HashMap`) wird stets als Potenz von zwei gehalten, damit die Modulo-Operation `hash % capacity` stark zu einer blitzschnellen bitweisen Operation `AND` optimiert werden kann: `hash & (capacity - 1)`.

## Verwandte Algorithmen in cOde(n)

- **[bit_01 – Count Set Bits](bit_01_count-set-bits.md)** — Stellt den hier verwendeten Kern-Trick `n & (n - 1)` vor.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
