# Miller-Rabin-Primzahltest

| | |
|---|---|
| **ID** | `math_09` |
| **Kategorie** | math |
| **Komplexität (erforderlich)** | $O(K \log^3 N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 1/10 |
| **Wikipedia** | [Miller–Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) |

## Problemstellung

Gegeben sei eine extrem große Ganzzahl `N` (z. B. 10^{18} oder größer). Bestimmen Sie, ob `N` eine Primzahl ist.
Die standardmäßige $O(\sqrt{N})$-Teilbarkeitsprüfung erfordert für 10^{18} eine Milliarde Operationen, was zu langsam ist.
Das Sieb des Eratosthenes (`math_02`) erfordert die Allokation eines Arrays der Größe 10^{18}, was physikalisch unmöglich ist.
Sie müssen dies in extrem schneller logarithmischer Zeit mithilfe eines probabilistischen Algorithmus lösen.

**Eingabe:** Eine Ganzzahl `N` und eine Ganzzahl `K` (Anzahl der Testrunden).
**Ausgabe:** Ein Boolean. `True`, wenn `N` *mit an Sicherheit grenzender Wahrscheinlichkeit* prim ist, `False`, wenn `N` *definitiv* zusammengesetzt ist.

## Wann man ihn verwendet

- Bei der Überprüfung der Primzahleigenschaft einer einzelnen, astronomisch großen Zahl (z. B. 64-Bit-Grenzen und darüber hinaus).
- Er ist der Grundpfeiler der modernen RSA-Kryptographie bei der Schlüsselgenerierung.

## Ansatz

**1. Der kleine Fermatsche Satz (Der erste Filter):**
Fermat stellte fest, dass wenn N prim ist, dann gilt A^{N-1} \equiv 1 \pmod N für jede zufällige Basis A.
Wir können also einfach eine Zufallszahl A wählen, A^{N-1} \pmod N mittels modularer Exponentiation (`math_03`) berechnen, und wenn das Ergebnis nicht 1 ist, ist N DEFINITIV zusammengesetzt!
*Der Fehler:* Carmichael-Zahlen (wie 561) sind zusammengesetzt, erfüllen aber auf magische Weise Fermats Test und liefern trotzdem 1! Sie sind "Pseudoprimzahlen", die den Test austricksen.

**2. Die nicht-triviale Quadratwurzel (Die Miller-Rabin-Korrektur):**
Miller und Rabin fügten eine zweite mathematische Regel hinzu, um die "Lügner" zu entlarven.
In der Modulo-Arithmetik hat die Gleichung X^2 \equiv 1 \pmod N zwei triviale Wurzeln, wenn N prim ist: X=1 und X=N-1 (was -1 entspricht).
Wenn wir JEMALS eine Zahl X finden, für die X^2 \equiv 1 \pmod N gilt, X aber WEDER 1 noch N-1 ist, dann ist N mathematisch garantiert zusammengesetzt!

**3. Der Algorithmus (Faktorisierung von N-1):**
Da N ungerade ist, ist N-1 gerade. Wir können N-1 in 2^D \cdot R faktorisieren (wobei R ungerade ist).
Wir wählen eine zufällige Basis A. Wir berechnen X = A^R \pmod N.
Wenn X == 1 oder X == N-1, ist diese Runde bestanden! N könnte prim sein.
Falls nicht, quadrieren wir X wiederholt (D-mal): X = (X \cdot X) \pmod N.
Bei jedem Quadrieren prüfen wir, ob wir 1 erreichen.
- Wenn wir N-1 erreichen, ist es eine gültige Wurzel! Die Runde ist bestanden.
- Wenn wir alle D Quadrierungen abschließen und niemals N-1 erreichen, dann ist N DEFINITIV zusammengesetzt!

**4. Probabilistische Runden (K):**
Eine Testrunde könnte von 1/4 der zusammengesetzten Zahlen ausgetrickst werden. Wenn wir den Test jedoch K-mal mit K verschiedenen zufälligen Basen A durchführen, beträgt die Wahrscheinlichkeit, dass eine zusammengesetzte Zahl alle K Runden überlebt, (\frac{1}{4})^K.
Wenn K=40, liegt die Fehlerwahrscheinlichkeit bei 1 zu 10^{24} (praktisch unmöglich). Daher erklären wir die Zahl für "mit an Sicherheit grenzender Wahrscheinlichkeit prim".

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for math_09: Miller-Rabin Primality Test.

Given a positive integer n, return True iff n is
"""


def solve(n_val, k):
    """Miller-Rabin primality test with k random witnesses."""
    if n_val < 2:
        return False
    if n_val < 4:
        return True
    if n_val % 2 == 0:
        return False
    # Write n - 1 = 2^r * d with d odd.
    r, d = 0, n_val - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    # Test with k random witnesses.
    import random
    rng = random.Random(12345)  # deterministic for testing
    for _ in range(k):
        a = rng.randrange(2, n_val - 1)
        x = pow(a, d, n_val)
        if x == 1 or x == n_val - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n_val
            if x == n_val - 1:
                break
        else:
            return False
    return True
```

</details>

## Durchlauf

Ist `N = 13` prim? `k = 1`.
`N - 1 = 12`.
12 = 2^2 \cdot 3. Also `d = 3`, `r = 2`.

1. **Runde 1:** Wähle zufällig `a = 2`.
   - Berechne X = 2^3 \pmod{13} = 8 \pmod{13} = 8.
   - X ist nicht 1 oder 12.
   - Gehe in die Quadrierungsschleife (`r-1 = 1` Mal).
   - X = (8 \cdot 8) \pmod{13} = 64 \pmod{13} = 12.
   - X == 12 (N-1). Runde bestanden! `break`.
2. Alle Runden beendet. Gib `True` zurück! ✓

*Was ist, wenn `N = 15` (zusammengesetzt)?*
`N - 1 = 14 = 2^1 \cdot 7`. `d = 7`, `r = 1`.
1. **Runde 1:** Wähle `a = 2`.
   - X = 2^7 \pmod{15} = 128 \pmod{15} = 8.
   - X ist nicht 1 oder 14.
   - Die Quadrierungsschleife läuft `r-1 = 0` Mal. (Läuft nicht).
   - `round_passed = False`. Gib `False` zurück. (Zusammengesetzt!) ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\log N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(K \log^3 N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(K \log^3 N)$ | $O(1)$ |

Wir führen K Iterationen durch.
In jeder Iteration benötigt `power_mod` $O(\log N)$ arithmetische Operationen.
Das Quadrieren der Zahlen benötigt $O(\log N)$ arithmetische Operationen.
Wenn die Zahlen extrem groß sind (und BigInteger-Objekte erfordern), benötigt jede Multiplikationsoperation selbst $O(\log^2 N)$ Zeit.
Daher beträgt die gesamte Zeitkomplexität $O(K \log^3 N)$. Wenn die Ganzzahlen in 64-Bit-Register passen, vereinfacht sich dies zu $O(K \log N)$.
Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Deterministischer Miller-Rabin:** Wenn N < 2^{64}, benötigen Sie keine zufälligen Basen! Es wurde mathematisch bewiesen, dass man nur genau 7 spezifische Basen testen muss: `[2, 3, 5, 7, 11, 13, 17]`. Wenn eine Zahl < 2^{64} diese 7 spezifischen Tests besteht, ist sie zu 100 % mathematisch bewiesen prim. Keine Zufälligkeit oder Wahrscheinlichkeit erforderlich!

## Anwendungen in der Praxis

- **RSA-Schlüsselgenerierung:** OpenSSL verwendet genau diesen Algorithmus, um 2048-Bit-Primzahlen zu generieren. Es rät zufällig eine ungerade 2048-Bit-Zahl und führt Miller-Rabin darauf aus. Wenn der Test fehlschlägt, wird 2 addiert und es wird erneut versucht, bis eine Zahl den Test besteht.

## Verwandte Algorithmen in cOde(n)

- **[math_03 - Modular Exponentiation](math_03_modular-exponentiation.md)** — Die Engine, die die Berechnung X = A^R \pmod N antreibt.
- **[math_02 - Sieve of Eratosthenes](math_02_sieve-of-eratosthenes.md)** — Die deterministische, Array-basierte Alternative, wenn Sie ALLE Primzahlen bis zu einem kleinen N benötigen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*