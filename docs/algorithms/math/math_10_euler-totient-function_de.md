# Eulers Totient-Funktion

| | |
|---|---|
| **ID** | `math_10` |
| **Kategorie** | math |
| **Komplexität (erforderlich)** | $O(\sqrt{N})$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Eulersche Phi-Funktion](https://en.wikipedia.org/wiki/Euler%27s_totient_function) |

## Problemstellung

Gegeben ist eine positive Ganzzahl `N`. Berechne die Eulersche Totient-Funktion, notiert als \phi(N) oder \text{phi}(N).
Die Totient-Funktion zählt die Anzahl der Ganzzahlen von 1 bis N, die teilerfremd zu N sind.
(Zwei Zahlen sind teilerfremd, wenn ihr größter gemeinsamer Teiler 1 ist).

**Eingabe:** Eine Ganzzahl `N`.
**Ausgabe:** Eine Ganzzahl, die \phi(N) repräsentiert.

## Wann man sie verwendet

- Berechnung der Anzahl möglicher modularer multiplikativer Inverser für einen gegebenen Modulo.
- Das fundamentale Theorem, das der RSA-Public-Key-Verschlüsselung zugrunde liegt.

## Ansatz

**1. Der Brute-Force-Ansatz:**
Man könnte einfach von i=1 bis N iterieren, den GCD-Algorithmus `math_01(i, N)` ausführen und einen Zähler erhöhen, falls das Ergebnis 1 ist. Dies benötigt $O(N \log N)$ Zeit, was für N=10^{12} bei weitem zu langsam ist.

**2. Die mathematische Formel:**
Euler entdeckte eine direkte Formel unter Verwendung der Primfaktorzerlegung.
Wenn p_1, p_2, \dots, p_k die eindeutigen Primfaktoren von N sind, dann gilt:
$\phi(N) = N \cdot \left(1 - \frac{1}{p_1}\right) \cdot \left(1 - \frac{1}{p_2}\right) \cdots \left(1 - \frac{1}{p_k}\right)$

Warum funktioniert das?
Beginne mit insgesamt N Zahlen.
Wenn `2` ein Primfaktor ist, sind exakt \frac{1}{2} aller Zahlen bis N durch 2 teilbar. Wir entfernen diese! Es bleiben N \cdot (1 - \frac{1}{2}) übrig.
Wenn `3` ein Primfaktor ist, sind exakt \frac{1}{3} der *verbleibenden* Zahlen durch 3 teilbar. Wir entfernen diese! Wir multiplizieren den Rest mit (1 - \frac{1}{3}).
Wir entfernen einfach die Vielfachen jedes Primfaktors.

**3. Der Algorithmus:**
Wir benötigen kein separates Array von Primzahlen! Wir führen einfach eine Standard-Primfaktorzerlegung durch.
1. Initialisiere `result = N`.
2. Iteriere `p` beginnend bei 2 bis \sqrt{N}.
3. Wenn N \pmod p == 0, dann ist p ein Primfaktor!
   - Wende Eulers Formel auf unser Ergebnis an: `result = result - (result // p)`. (Dies ist mathematisch identisch zu result \cdot (1 - \frac{1}{p}), verhindert jedoch Fehler durch Fließkommapräzision).
   - Dividiere N so oft wie möglich durch p, um diesen Primfaktor vollständig aus der Zahl zu entfernen (genau wie bei der Standard-Faktorisierung).
4. Wenn nach der Schleife das verbleibende N > 1 ist, bedeutet dies, dass der letzte verbleibende Teil selbst eine Primzahl ist! Wir wenden die Formel ein letztes Mal für diesen finalen Primfaktor an.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for math_10: Euler Totient Function.

Given a positive integer n, return phi(n): the
"""


def solve(n_val):
    """Euler's totient function phi(n) via prime factorization."""
    if n_val <= 0:
        return 0
    if n_val == 1:
        return 1
    result = n_val
    p = 2
    temp = n_val
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        # temp is a prime factor > sqrt(original n).
        result -= result // temp
    return result
```

</details>

## Durchlauf

`N = 12`. `result = 12`.

1. `p = 2`:
   - 2 \times 2 \le 12.
   - `12 % 2 == 0`. Wir haben einen Primfaktor gefunden!
   - `result -= 12 // 2` \implies `result = 12 - 6 = 6`.
   - Entferne `2` aus `N`: `12 // 2 = 6`, `6 // 2 = 3`. Jetzt ist `n = 3`.
2. `p = 3`:
   - 3 \times 3 \not\le 3. Schleife terminiert!
3. Abschließende Prüfung: `n = 3`. `3 > 1` ist wahr!
   - Wir müssen den letzten Primfaktor `3` verarbeiten.
   - `result -= 6 // 3` \implies `result = 6 - 2 = 4`.

Ergebnis: `4`. ✓
*(Verifizierung: Die Zahlen von 1 bis 12, die teilerfremd zu 12 sind, sind `1, 5, 7, 11`. Exakt 4 Zahlen!)*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\log N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\sqrt{N})$ | $O(1)$ |
| **Schlechtester Fall** | $O(\sqrt{N})$ | $O(1)$ |

Die `while`-Schleife läuft bis \sqrt{N}. Wenn N eine Primzahl ist, benötigt sie exakt \sqrt{N} Iterationen. Wenn N hochgradig zusammengesetzt ist (z. B. 2^{30}), reduziert die innere `while`-Schleife N sofort in $O(\log N)$ Zeit auf 1. Daher ist die Zeitkomplexität im schlechtesten Fall durch $O(\sqrt{N})$ begrenzt.
Die Platzkomplexität ist strikt $O(1)$ konstanter Platz, da wir nur drei Ganzzahlvariablen (`n`, `result`, `p`) verfolgen.

## Varianten & Optimierungen

- **Berechnung von 1 bis N (Sieb-Methode):** Wenn ein Problem erfordert, den Totient für *jede* Zahl von 1 bis 10^5 zu berechnen, benötigt ein $O(\sqrt{N})$-Aufruf in einer Schleife $O(N \sqrt{N})$ Zeit. Dies kann auf $O(N \log(\log N))$ optimiert werden, indem man ein Array verwendet, das exakt dem Sieb des Eratosthenes (`math_02`) entspricht. Man initialisiert `phi[i] = i`, und wenn man eine Primzahl findet, iteriert man durch deren Vielfache M und führt `phi[M] -= phi[M] // p` aus.
- **Carmichael-Funktion (`math_06`):** Die fortgeschrittene Variante der Totient-Funktion, die den kleinstmöglichen Exponenten anstelle des garantierten Euler-Exponenten findet.

## Anwendungen in der Praxis

- **RSA-Kryptographie:** Um ein RSA-Schlüsselpaar zu generieren, wählt man zwei riesige Primzahlen P und Q. Man berechnet N = P \times Q. Anschließend muss man explizit den Eulerschen Totient von N berechnen: \phi(N) = (P-1)(Q-1). Dieser Wert \phi(N) wird verwendet, um die öffentlichen und privaten Verschlüsselungsschlüssel zu generieren!

## Verwandte Algorithmen in cOde(n)

- **[math_06 - Carmichael-Funktion](math_06_carmichael-function.md)** — Die mathematisch überlegene, aber wesentlich komplexere Alternative zur Totient-Funktion.
- **[math_02 - Sieb des Eratosthenes](math_02_sieve-of-eratosthenes.md)** — Die optimale Strategie zur massenhaften Berechnung von Totienten.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*