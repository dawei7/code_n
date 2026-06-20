# Fehlende Zahl

| | |
|---|---|
| **ID** | `bit_10` |
| **Kategorie** | Bitmanipulation |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Fehlende Zahl](https://leetcode.com/problems/missing-number/) |

## Aufgabenstellung

Gegeben ist ein Array `nums` mit `n` verschiedenen Zahlen im Bereich `[0, n]`. Gib die einzige Zahl im Bereich zurück, die im Array fehlt.

**Eingabe:** Ein Ganzzahl-Array `nums` der Länge `n`.
**Ausgabe:** Eine Ganzzahl, die die fehlende Zahl angibt.

## Anwendungsfälle

- Um die kommutativen und sich gegenseitig aufhebenden Eigenschaften von XOR in einem etwas anderen Kontext als `Single Number` zu veranschaulichen.
- Wenn Sie eine einzelne Abweichung zwischen einer bekannten „erwarteten“ Folge und einer „tatsächlichen“ Folge finden müssen.

## Vorgehensweise

**1. Der mathematische Ansatz (Gaußsche Formel):**
Die Summe der ersten `N` Zahlen ist mathematisch definiert als: \text{Erwartete Summe} = \frac{n(n + 1)}{2}.
Wenn wir das Array durchlaufen und die \text{tatsächliche Summe} berechnen, ist die fehlende Zahl einfach \text{erwartete Summe} - \text{tatsächliche Summe}.
*Warum könnte dies in einem Vorstellungsgespräch schiefgehen?* Wenn N unglaublich groß ist (z. B. 10^5), könnte die mathematische Summe in Sprachen wie Java oder C++ einen Ganzzahlüberlauf verursachen!

**2. Der XOR-Ansatz:**
Aus `bit_03` wissen wir, dass sich jede Zahl, die mit sich selbst XOR-verknüpft wird, zu `0` auflöst (`A ^ A = 0`).
Wenn wir die erwartete Folge `[0, 1, 2, 3]` und die tatsächliche Folge `[0, 1, 3]` haben, was passiert dann, wenn wir ALLE diese Zahlen gleichzeitig miteinander XOR-verknüpfen?
`Expected = 0 ^ 1 ^ 2 ^ 3`
`Actual   = 0 ^ 1 ^     3`
`Result   = (0^0) ^ (1^1) ^ 2 ^ (3^3)`
`Result   =   0   ^   0   ^ 2 ^   0`
`Result   = 2`!

Jede im Array vorhandene Zahl passt perfekt zu ihrer entsprechenden Indexnummer in der erwarteten Folge und hebt sich auf! Die EINZIGE Zahl, die übrig bleibt, ist die fehlende Zahl, da sie im tatsächlichen Array keinen „Zwilling“ hatte, der sie aufheben könnte.

**3. Ausführung:**
Initialisiere eine Variable `missing = len(nums)`. (Da die Schleifenindizes nur von `0` bis `n-1` reichen, müssen wir die letzte erwartete Zahl `n` manuell in den XOR-Akkumulator einfügen).
Schleife `i` von `0` bis `n-1`.
`missing ^= i ^ nums[i]`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_10: Missing Number.

Given an array arr of n distinct integers in
"""


def solve(arr, n):
    """Find the missing integer in arr (length n, values in [0, n])."""
    # XOR all values and all indices 0..n; the missing value
    # is the survivor.
    result = n  # include the index n in the XOR
    for i, v in enumerate(arr):
        result ^= i ^ v
    return result
```

</details>

## Schritt-für-Schritt-Anleitung

`nums = [3, 0, 1]`. N = 3.
Ausgangssituation `missing = 3`.

1. **i = 0:**
   - `missing ^= 0` (Erwarteter Index) -> `3 ^ 0 = 3`
   - `missing ^= nums[0]`(`3`) -> `3 ^ 3 = 0` (Die „3“ hat sich aufgehoben!)
2. **i = 1:**
   - `missing ^= 1` (erwarteter Index) -> `0 ^ 1 = 1`
   - `missing ^= nums[1]`(`0`) -> `1 ^ 0 = 1` (Die „0“ hat sich implizit aufgehoben)
3. **i = 2:**
   - `missing ^= 2` (Erwarteter Index) -> `1 ^ 2 = 3`
   - `missing ^= nums[2]`(`1`) -> `3 ^ 1 = 2` (Die „1“en heben sich auf!)

Ergebnis `missing = 2`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Das Array wird genau einmal durchlaufen. Bitweise XOR-Operationen benötigen $O(1)$ Zeit. Die gesamte Zeitkomplexität beträgt streng $O(N)$.
Es wird nur eine Ganzzahlvariable `missing` verwendet. Die Platzkomplexität beträgt $O(1)$.
Im Gegensatz zur mathematischen Summenformel führen XOR-Operationen NIEMALS zu einem Überlauf der Ganzzahlgrenzen.

## Varianten & Optimierungen

- **Finde die doppelte Zahl:** Dir wird ein Array der Größe N+1 gegeben, das Zahlen im Bereich [1, N] enthält. Es gibt genau EINE doppelte Zahl. Kannst du XOR verwenden? *NEIN!* Denn die doppelte Zahl könnte dreimal oder viermal vorkommen, was die XOR-Ausgleichsregeln verletzen würde. Du musst Floyds Zyklenerkennung (Schildkröte und Hase) oder die binäre Suche verwenden.

## Anwendungen in der Praxis

- **Erkennung von Netzwerkpaketverlusten:** Bei der Übertragung eines fortlaufenden Stroms von UDP-Paketen (mit den Nummern 1 bis N) kann der Empfänger eine fortlaufende XOR-Prüfsumme führen. Wenn genau ein Paket verloren geht, gibt die XOR-Prüfsumme dessen ID sofort preis, ohne dass die gesamte Liste der empfangenen Pakete durchsucht werden muss!

## Verwandte Algorithmen in cOde(n)

- **[bit_03 – Einzelne Zahl (XOR)](bit_03_single-number-xor.md)** — Der grundlegende Vorläuferalgorithmus.
- **[two_pointers_03 – Duplikatzahl finden](../two_pointers/two_pointers_03_find-the-duplicate-number.md)** — Das Problem, das identisch aussieht, aber streng genommen nicht durch Bitmanipulation gelöst werden kann.

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen
Enzyklopädieeintrag finden Sie unter dem Wikipedia-Link oben auf der Seite.
Quell-Repository:
<https://github.com/dawei7/code_n>.*
