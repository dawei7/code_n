# Formale mathematische Spezifikation: Größter gemeinsamer Teiler (Euklidischer Algorithmus)

## 1. Definitionen und Notation

Sei $\mathbb{Z}^+$ die Menge der positiven ganzen Zahlen $\{1, 2, 3, \dots\}$ und $\mathbb{N}_0$ die Menge der nicht-negativen ganzen Zahlen $\{0, 1, 2, \dots\}$.

Der größte gemeinsame Teiler (ggT) zweier ganzer Zahlen $a, b \in \mathbb{Z}^+$ ist definiert als die eindeutige positive ganze Zahl $g = \gcd(a, b)$, für die gilt:
1. $g \mid a$ und $g \mid b$ (Eigenschaft des gemeinsamen Teilers).
2. Für jedes $d \in \mathbb{Z}^+$, falls $d \mid a$ und $d \mid b$, dann gilt $d \mid g$ (Eigenschaft der Maximalität).

Der Algorithmus operiert auf einem Zustandsraum $\mathcal{S} \subset \mathbb{N}_0 \times \mathbb{N}_0$. Gegeben eine Eingabe $(a_0, b_0) \in \mathbb{Z}^+ \times \mathbb{Z}^+$, erzeugt der Algorithmus eine Folge von Zuständen $(a_k, b_k)$, wobei $k \in \mathbb{N}_0$.

## 2. Algebraische Charakterisierung

Die Korrektheit des Euklidischen Algorithmus basiert auf dem Divisionstheorem und den Eigenschaften der ggT-Funktion.

**Theorem (Euklidische Reduktion):** Für beliebige $a, b \in \mathbb{N}_0$ mit $b > 0$, sei $a = qb + r$, wobei $q = \lfloor a/b \rfloor$ und $r = a \pmod b$. Dann gilt:
$$\gcd(a, b) = \gcd(b, r)$$

**Beweisskizze:**
Sei $d_1 = \gcd(a, b)$ und $d_2 = \gcd(b, r)$. 
Da $d_1 \mid a$ und $d_1 \mid b$, gilt auch $d_1 \mid (a - qb)$, was $d_1 \mid r$ impliziert. Somit ist $d_1$ ein gemeinsamer Teiler von $b$ und $r$, woraus $d_1 \leq d_2$ folgt.
Umgekehrt gilt, da $d_2 \mid b$ und $d_2 \mid r$, auch $d_2 \mid (qb + r)$, was $d_2 \mid a$ impliziert. Somit ist $d_2$ ein gemeinsamer Teiler von $a$ und $b$, woraus $d_2 \leq d_1$ folgt.
Daraus ergibt sich $d_1 = d_2$.

**Schleifeninvariante:**
Sei $(a_k, b_k)$ der Zustand in Iteration $k$. Die Invariante $\gcd(a_k, b_k) = \gcd(a_0, b_0)$ gilt für alle $k$, bis $b_k = 0$.
Die Übergangsfunktion $f: \mathcal{S} \to \mathcal{S}$ ist definiert als:
$$f(a, b) = (b, a \pmod b)$$
Der Algorithmus terminiert beim kleinsten $k$, für das $b_k = 0$ gilt, und liefert $\gcd(a_k, 0) = a_k$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der Iterationen bestimmt, die erforderlich sind, um $b_k = 0$ zu erreichen. 

**Theorem (Satz von Lamé):** Sei $a > b \geq 1$. Die Anzahl der Schritte $n$, die der Euklidische Algorithmus zur Berechnung von $\gcd(a, b)$ benötigt, beträgt höchstens $5 \cdot \log_{10}(b)$.

**Herleitung:**
Betrachten wir die Folge der Reste $r_0, r_1, \dots, r_n$ mit $r_0 = a, r_1 = b$ und $r_{i+1} = r_{i-1} \pmod{r_i}$. 
Da $r_{i-1} = q_i r_i + r_{i+1}$ und $q_i \geq 1$, gilt $r_{i-1} \geq r_i + r_{i+1}$. 
Definiert man die Fibonacci-Folge $F_n$ mit $F_0=0, F_1=1, F_2=1, \dots$, lässt sich durch vollständige Induktion zeigen, dass $r_{n-i+1} \geq F_{i+1}$. 
Für den schlechtesten Fall gilt $b < F_{n+2}$. Unter Verwendung der Binet-Formel $F_n \approx \frac{\phi^n}{\sqrt{5}}$ mit $\phi = \frac{1+\sqrt{5}}{2} \approx 1.618$ und durch Logarithmieren ergibt sich $n \approx \log_{\phi}(b) \approx 1.44 \log_2(b)$.
Somit ist die Zeitkomplexität $O(\log(\min(a, b)))$.

### Platzkomplexität
Die iterative Implementierung verwaltet lediglich zwei Integer-Variablen $a$ und $b$ im Zustandsraum $\mathcal{S}$. 
Der benötigte zusätzliche Speicherplatz ist unabhängig von der Größe der Eingabewerte, da die Variablen in-place aktualisiert werden.
Daher beträgt die Platzkomplexität $O(1)$. 

(Hinweis: Eine rekursive Implementierung würde $O(\log(\min(a, b)))$ Stack-Speicher benötigen, um die Aktivierungsdatensätze der Rekursionstiefe zu speichern.)