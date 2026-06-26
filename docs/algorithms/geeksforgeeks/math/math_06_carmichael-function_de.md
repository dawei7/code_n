# Carmichael-Funktion

| | |
|---|---|
| **ID** | `math_06` |
| **Kategorie** | math |
| **Komplexität (erforderlich)** | $O(\sqrt{N})$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 1/10 |
| **Wikipedia** | [Carmichael-Funktion](https://de.wikipedia.org/wiki/Carmichael-Funktion) |

## Problemstellung

Gegeben sei eine positive Ganzzahl `N`. Berechne die Carmichael-Funktion \lambda(N).
Die Carmichael-Funktion \lambda(N) liefert die kleinste positive Ganzzahl M, sodass A^M \equiv 1 \pmod N für jede Ganzzahl A gilt, die teilerfremd zu N ist.
(Sie ist eng mit der Eulerschen Phi-Funktion \phi(N) verwandt, liefert jedoch den *absoluten minimalen* Exponenten anstelle eines universell garantierten, größeren Exponenten).

**Eingabe:** Eine Ganzzahl `N`.
**Ausgabe:** Eine Ganzzahl, die \lambda(N) repräsentiert.

## Anwendung

- In extrem fortgeschrittener Zahlentheorie und Kryptographie-Optimierung.
- Wenn die absolut engste Schranke für die Periodizität der modularen Exponentiation benötigt wird. (In der RSA-Kryptographie führt die Verwendung von \lambda(N) anstelle von \phi(N) zu deutlich kleineren, effizienteren privaten Schlüsseln!)

## Ansatz

**1. Die Beziehung zur Eulerschen Phi-Funktion (\phi):**
Die Eulersche Phi-Funktion \phi(N) zählt die Anzahl der zu N teilerfremden Ganzzahlen.
Der Satz von Euler garantiert, dass A^{\phi(N)} \equiv 1 \pmod N gilt.
Allerdings ist \phi(N) manchmal ein unnötig großer Exponent.
Beispiel: N = 8. \phi(8) = 4. Also gilt A^4 \equiv 1 \pmod 8.
Die Carmichael-Funktion zeigt jedoch, dass \lambda(8) = 2 ist! Ein kleinerer Exponent funktioniert einwandfrei: 3^2 \equiv 1 \pmod 8, 5^2 \equiv 1 \pmod 8, 7^2 \equiv 1 \pmod 8.

**2. Die Regeln zur Berechnung von \lambda(N):**
Wie die Phi-Funktion wird \lambda(N) durch die Primfaktorzerlegung von N bestimmt.
Sei N = p_1^{k_1} \cdot p_2^{k_2} \cdots p_m^{k_m}.
Die Carmichael-Funktion für eine zusammengesetzte Zahl ist das **kleinste gemeinsame Vielfache (kgV)** der Carmichael-Funktionen ihrer Primfaktor-Komponenten!
\lambda(N) = \text{kgV}(\lambda(p_1^{k_1}), \lambda(p_2^{k_2}), \dots, \lambda(p_m^{k_m}))

**3. Auswertung von Primzahlpotenzen:**
Für jede Primzahlpotenz p^k ist die Carmichael-Funktion normalerweise identisch mit der Phi-Funktion:
\lambda(p^k) = \phi(p^k) = p^{k-1} \cdot (p - 1).

Es gibt in der gesamten Mathematik genau EINE Ausnahme: wenn p = 2 und k \ge 3.
\lambda(2^k) = \frac{1}{2} \cdot \phi(2^k) = 2^{k-2}.
(Dies ist genau der Grund, warum N=8=2^3 zu \lambda(8) = 2 führte, nicht zu 4).

**4. Der Algorithmus:**
1. Initialisiere ein laufendes `lcm_result = 1`.
2. Extrahiere die Faktoren von 2 aus N. Falls vorhanden, berechne \lambda(2^k) unter Verwendung der speziellen Ausnahmeregeln und aktualisiere `lcm_result`.
3. Iteriere durch alle ungeraden Zahlen P von 3 bis \sqrt{N}. Wenn P ein Teiler von N ist, extrahiere alle Potenzen von P, um P^k zu finden. Berechne \lambda(P^k) = P^{k-1} \cdot (P - 1).
4. Aktualisiere `lcm_result = kgV(lcm_result, \lambda(P^k))`.
5. Wenn nach der Schleife N > 1 gilt, ist das verbleibende N selbst eine Primzahl! \lambda(N) = N - 1. Aktualisiere das kgV.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for math_06: Carmichael Function.

Factor n. lambda per prime power: p^(k-1) * (p-1) for odd
primes, 2^(k-2) for n=2^k (k>=3). Combine via lcm.
"""


def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 4:
        return 2
    temp = n
    factors = {}
    p = 2
    while p * p <= temp:
        while temp % p == 0:
            factors[p] = factors.get(p, 0) + 1
            temp //= p
        p += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    from math import gcd
    lam = 1
    for p, k in factors.items():
        if p == 2:
            if k == 1:
                pk_lam = 1
            elif k == 2:
                pk_lam = 2
            else:
                pk_lam = 2 ** (k - 2)
        else:
            pk_lam = (p ** (k - 1)) * (p - 1)
        lam = lam * pk_lam // gcd(lam, pk_lam)
    return lam
```

</details>

## Durchlauf

Berechne \lambda(15). (N=15). `result = 1`.

1. `15 % 2 != 0`. Überspringe Faktor 2.
2. `p = 3`: 3 x 3 \le 15.
   - `15 % 3 == 0`.
   - `k = 1`, `n = 15 // 3 = 5`.
   - `lambda_val = (3^0) * (3-1) = 2`.
   - `result = kgV(1, 2) = 2`.
3. `p = 5`: 5 x 5 \not\le 5. Schleife terminiert!
4. Überprüfe verbleibendes N: `5 > 1`. `5` ist prim!
   - `lambda_val = 5 - 1 = 4`.
   - `result = kgV(2, 4) = 4`.

Ergebnis: \lambda(15) = 4. ✓
*(Überprüfung: \phi(15) = \phi(3) \cdot \phi(5) = 2 \cdot 4 = 8. Also gilt A^8 \equiv 1 \pmod{15}. Aber Carmichael sagt, ein Exponent von 4 reicht aus! 2^4 = 16 \equiv 1 \pmod{15}. Korrekt!)*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\log N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\sqrt{N})$ | $O(1)$ |
| **Schlechtester Fall** | $O(\sqrt{N})$ | $O(1)$ |

Die Zeitkomplexität ist identisch mit der Standard-Primfaktorzerlegung. Die `while`-Schleife prüft alle ungeraden Zahlen bis \sqrt{N}. Wenn N prim ist, benötigt sie exakt \sqrt{N} Prüfungen. Wenn N hochgradig zusammengesetzt ist (z. B. 2^{30}), reduziert es N in $O(\log N)$ Zeit sofort auf 1.
Daher ist die Zeitkomplexität im schlechtesten Fall $O(\sqrt{N})$.
Die Platzkomplexität ist $O(1)$ konstant.

## Varianten & Optimierungen

- **Pollard-Rho-Algorithmus:** Wenn N astronomisch groß ist (z. B. eine 100-stellige Zahl), würde das Prüfen bis \sqrt{N} (10^{50} Iterationen) Billionen von Jahren dauern. Fortgeschrittene probabilistische Faktorisierungsalgorithmen wie Pollard-Rho oder das Zahlkörpersieb (General Number Field Sieve) sind erforderlich, um N zu faktorisieren, bevor die Carmichael-Funktion berechnet werden kann.

## Anwendungen in der Praxis

- **RSA-Schlüsselerzeugung (PKCS#1):** Moderne Implementierungen der RSA-Kryptographie (wie OpenSSL) verwenden explizit \lambda(N) anstelle von \phi(N), um den privaten Entschlüsselungsschlüssel d zu berechnen. Da \lambda(N) oft viel kleiner als \phi(N) ist, führt dies zu einem strikt kleineren privaten Schlüssel, was die Entschlüsselung auf leistungsschwachen Geräten erheblich beschleunigt, ohne die mathematische Sicherheit zu beeinträchtigen!

## Verwandte Algorithmen in cOde(n)

- **[math_10 - Eulersche Phi-Funktion](math_10_euler-totient-function.md)** — Der einfachere, universell gelehrte Vorgänger dieser Funktion.
- **[math_01 - GGT](math_01_gcd-euclidean.md)** — Erforderlich zur Berechnung des kgV beim Zusammenführen der Ergebnisse der Primfaktoren.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*