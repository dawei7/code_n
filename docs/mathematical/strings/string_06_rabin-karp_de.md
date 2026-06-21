# Formale mathematische Spezifikation: Rabin-Karp-Algorithmus

## 1. Definitionen und Notation
Sei $T \in \Sigma^*$ ein Text der Länge $n$ und $W \in \Sigma^*$ ein Muster der Länge $m$.
Sei $b$ die Basis (z. B. $b = 256$) und $q$ ein großer Primzahlmodul.

## 2. Polynomielle Rolling-Hash-Funktion
Für einen String $S$ der Länge $m$ definieren wir seinen Hash-Wert $H(S) \in \mathbb{Z}_q$:
$$ H(S) = \left( \sum_{i=1}^m S[i] \cdot b^{m-i} \right) \pmod q $$

## 3. Algebraische Charakterisierung (Rolling-Hash-Eigenschaft)
Der Hash-Wert für die nächste Verschiebung $s+1$ in $T$ kann aus der Verschiebung $s$ in $O(1)$-Zeit berechnet werden:
$$ H(T[s+2 \dots s+m+1]) = \left( (H(T[s+1 \dots s+m]) - T[s+1] \cdot b^{m-1}) \cdot b + T[s+m+1] \right) \pmod q $$
wobei alle arithmetischen Operationen in $\mathbb{Z}_q$ ausgeführt werden.

## 4. Formalisierung des Algorithmus
1. Berechne $h_M = b^{m-1} \pmod q$ im Voraus.
2. Berechne $H(W)$ und $H_0 = H(T[1 \dots m])$.
3. Für $s = 0, \dots, n-m$:
   - Falls $H_s = H(W)$, führe eine deterministische Verifikation $T[s+1 \dots s+m] \stackrel{?}{=} W[1 \dots m]$ durch.
   - Wenn die Verifikation erfolgreich ist, ist die Verschiebung $s$ gültig.
   - Falls $s < n-m$, berechne $H_{s+1}$ unter Verwendung der Rolling-Hash-Formel.

## 5. Komplexitätsanalyse
- **Zeitkomplexität:** Die Vorberechnung benötigt $O(m)$ Zeit. Das Fortrollen des Hashes (Hash-Rolling) benötigt $O(n-m)$ Zeit. Die deterministische Verifikation benötigt $O(m)$ Zeit, wird jedoch nur ausgeführt, wenn $H_s = H(W)$ gilt. Unter der Annahme einer gleichmäßigen Hash-Verteilung über $\mathbb{Z}_q$ ist die erwartete Anzahl von Scheintreffern (Spurious Hits) $O(n/q)$. Folglich beträgt die erwartete Zeitkomplexität $O(n + m)$. Die Zeitkomplexität im schlechtesten Fall (wenn alle Hashes kollidieren) beträgt $O(nm)$.
- **Platzkomplexität:** Der Algorithmus verwaltet ganzzahlige Hash-Variablen. Die Platzkomplexität ist strikt $O(1)$.