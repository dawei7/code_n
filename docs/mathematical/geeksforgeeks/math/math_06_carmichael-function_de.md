# Formale mathematische Spezifikation: Carmichael-Funktion

## 1. Definitionen und Notation

Sei $N \in \mathbb{Z}^+$ eine positive ganze Zahl. Die Carmichael-Funktion, bezeichnet als $\lambda(N)$, ist definiert als der Exponent der multiplikativen Gruppe der ganzen Zahlen modulo $N$, bezeichnet als $(\mathbb{Z}/N\mathbb{Z})^\times$. Formal ist $\lambda(N)$ die kleinste positive ganze Zahl $M$, sodass gilt:
$$a^M \equiv 1 \pmod N \quad \forall a \in \mathbb{Z} \text{ mit } \gcd(a, N) = 1$$

Der Definitionsbereich der Funktion ist $\mathcal{D} = \{N \in \mathbb{Z} \mid N \ge 1\}$ und der Wertebereich ist $\mathcal{C} = \mathbb{Z}^+$.
Sei die Primfaktorzerlegung von $N$ durch die kanonische Darstellung gegeben:
$$N = \prod_{i=1}^{m} p_i^{k_i}$$
wobei $p_i$ verschiedene Primzahlen und $k_i \in \mathbb{Z}^+$ sind.

## 2. Algebraische Charakterisierung

Die Carmichael-Funktion ist eine wohldefinierte arithmetische Funktion, die die Eigenschaft besitzt, das kleinste gemeinsame Vielfache der Carmichael-Werte ihrer Primzahlpotenzkomponenten zu sein.

### Der Fundamentalsatz der $\lambda(N)$
Für $N = p_1^{k_1} p_2^{k_2} \cdots p_m^{k_m}$ ist die Funktion definiert als:
$$\lambda(N) = \text{lcm}(\lambda(p_1^{k_1}), \lambda(p_2^{k_2}), \dots, \lambda(p_m^{k_m}))$$

### Auswertung bei Primzahlpotenzen
Der Wert von $\lambda(p^k)$ wird durch die Struktur der Gruppe $(\mathbb{Z}/p^k\mathbb{Z})^\times$ bestimmt:

1. **Für ungerade Primzahlen ($p > 2$):**
   Die Gruppe ist zyklisch und $\lambda(p^k) = \phi(p^k) = p^{k-1}(p-1)$.

2. **Für die Primzahl $p = 2$:**
   - Wenn $k=1$, $\lambda(2) = 1$.
   - Wenn $k=2$, $\lambda(4) = 2$.
   - Wenn $k \ge 3$, ist die Gruppe $(\mathbb{Z}/2^k\mathbb{Z})^\times$ isomorph zu $C_2 \times C_{2^{k-2}}$. Somit ist der Exponent:
     $$\lambda(2^k) = 2^{k-2}$$

### Rekursive Invariante
Sei $f(n, p)$ eine Funktion, die die Primzahlpotenz $p^k$ aus $n$ extrahiert und das laufende Ergebnis $L$ aktualisiert. Der Zustandsübergang bei jedem Schritt $i$ ist:
$$L_i = \text{lcm}(L_{i-1}, \lambda(p_i^{k_i}))$$
wobei $L_0 = 1$. Der Algorithmus terminiert, wenn $\prod p_i^{k_i} = N$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus stützt sich auf Probedivision, um die Primfaktorzerlegung von $N$ zu bestimmen.

1. **Faktorisierungsphase:** Wir iterieren über potenzielle Teiler $p$, sodass $p \le \sqrt{N}$. Im Schlechtesten Fall (wenn $N$ eine Primzahl ist), führt die Schleife $\lceil \sqrt{N} \rceil$ Iterationen aus. Jede Iteration führt eine konstante Anzahl an arithmetischen Operationen (Modulo und Division) aus. Daher ist die Faktorisierungsphase $O(\sqrt{N})$.
2. **LCM-Phase:** Gegeben die Primfaktorzerlegung gibt es höchstens $\omega(N)$ verschiedene Primfaktoren, wobei $\omega(N) \le \log_2 N$. Die Berechnung von $\text{lcm}(a, b) = \frac{|a \cdot b|}{\gcd(a, b)}$ beinhaltet den euklidischen Algorithmus, welcher $O(\log(\min(a, b)))$ ist. Da $\lambda(N) < N$, ist dies $O(\log N)$.

Addiert man diese, wird die gesamte Zeitkomplexität von der Faktorisierung dominiert:
$$T(N) = O(\sqrt{N}) + O(\omega(N) \log N) = O(\sqrt{N})$$

### Platzkomplexität
Der Algorithmus verwaltet eine konstante Anzahl an Variablen: `temp` (der verbleibende Quotient), `p` (der aktuelle Teiler), `lam` (das laufende LCM) und `pk_lam` (das lokale Ergebnis der Primzahlpotenz).

Da die Speicheranforderungen nicht mit der Größe von $N$ skalieren (unter der Annahme von Ganzzahl-Arithmetik mit fester Breite oder logarithmischem Speicherplatz für beliebig große ganze Zahlen), ist die zusätzliche Platzkomplexität:
$$S(N) = O(1)$$
Wenn wir die Speicherung der Primfaktoren in einem Dictionary/Map berücksichtigen, beträgt die Platzkomplexität $O(\log N)$, um die verschiedenen Primfaktoren zu speichern; die bereitgestellte Implementierung verwendet jedoch einen iterativen Ansatz, der Faktoren "on-the-fly" verarbeitet und somit $O(1)$ Speicherplatz beibehält.