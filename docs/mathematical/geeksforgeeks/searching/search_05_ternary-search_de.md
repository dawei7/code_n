# Formale mathematische Spezifikation: Ternary Search

## 1. Definitionen und Notation

Sei $A = [a_0, a_1, \dots, a_{n-1}]$ eine Sequenz von Elementen aus einer total geordneten Menge $(\mathcal{X}, \leq)$, sodass für alle $i, j \in \{0, \dots, n-1\}$ gilt: Wenn $i < j$, dann $a_i \leq a_j$.

Wir definieren den Suchraum als ein abgeschlossenes Intervall von Indizes $\mathcal{I} = [L, R] \subset \mathbb{Z}$, wobei anfänglich $L = 0$ und $R = n-1$ gilt. Das Ziel ist es, einen Index $k \in \{0, \dots, n-1\}$ zu finden, sodass $a_k = \tau$, wobei $\tau \in \mathcal{X}$ der Zielwert ist. Falls kein solches $k$ existiert, gibt der Algorithmus $-1$ zurück.

Der Zustand des Algorithmus zu einer beliebigen Iteration $t$ ist durch das Tupel $(L_t, R_t)$ definiert. Die Übergangsfunktion bildet den aktuellen Zustand auf einen nachfolgenden Zustand $(L_{t+1}, R_{t+1})$ ab, basierend auf der Auswertung der Partitionspunkte $m_{1,t}$ und $m_{2,t}$, welche wie folgt definiert sind:
$$m_{1,t} = L_t + \left\lfloor \frac{R_t - L_t}{3} \right\rfloor$$
$$m_{2,t} = R_t - \left\lfloor \frac{R_t - L_t}{3} \right\rfloor$$

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf der Invariante, dass wenn $\tau \in \{a_L, \dots, a_R\}$ gilt, dann auch $\tau \in \{a_{L_t}, \dots, a_{R_t}\}$ gilt. Die Übergangslogik wird durch die folgende Partitionierung des Suchraums bestimmt:

1. **Induktionsanfang (Erfolg):** Wenn $a_{m_{1,t}} = \tau$ oder $a_{m_{2,t}} = \tau$, terminiert der Algorithmus und gibt den Index zurück.
2. **Rekursiver Schritt (Reduktion):**
   - Wenn $\tau < a_{m_{1,t}}$, dann kann $\tau$ aufgrund der Monotonie von $A$ nicht im Indexbereich $[m_{1,t}, R_t]$ existieren. Somit gilt $R_{t+1} = m_{1,t} - 1$ und $L_{t+1} = L_t$.
   - Wenn $\tau > a_{m_{2,t}}$, dann kann $\tau$ nicht im Indexbereich $[L_t, m_{2,t}]$ existieren. Somit gilt $L_{t+1} = m_{2,t} + 1$ und $R_{t+1} = R_t$.
   - Wenn $a_{m_{1,t}} < \tau < a_{m_{2,t}}$, dann kann $\tau$ weder in $[L_t, m_{1,t}]$ noch in $[m_{2,t}, R_t]$ existieren. Somit gilt $L_{t+1} = m_{1,t} + 1$ und $R_{t+1} = m_{2,t} - 1$.

Der Algorithmus terminiert, wenn $L_t > R_t$ gilt; zu diesem Zeitpunkt ist die Menge der Kandidatenindizes leer, was impliziert, dass $\tau \notin A$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $N_t = R_t - L_t + 1$ die Anzahl der Elemente im Suchraum zur Iteration $t$. In jeder Iteration führt der Algorithmus eine konstante Anzahl an Vergleichen (höchstens 4) durch, um den Suchraum zu reduzieren. Die neue Suchraumgröße $N_{t+1}$ erfüllt:
$$N_{t+1} \leq \frac{N_t}{3}$$
Die Rekursionsgleichung für die Anzahl der Iterationen im Schlechtesten Fall $T(N)$ lautet:
$$T(N) = T\left(\frac{N}{3}\right) + c$$
Unter Anwendung des Master-Theorems, wobei $a=1, b=3, f(N)=O(1)$, erhalten wir $N^{\log_b a} = N^0 = 1$. Da $f(N) = \Theta(N^{\log_b a})$ gilt, ergibt sich die Komplexität zu:
$$T(N) = \Theta(\log_3 N)$$
Da jede Iteration zwei Vergleiche durchführt, beträgt die Gesamtzahl der Vergleiche näherungsweise $2 \log_3 N$. Unter Verwendung der Basiswechselformel $\log_3 N = \frac{\ln N}{\ln 3}$ beobachten wir:
$$2 \frac{\ln N}{\ln 3} \approx 2 \cdot 0.91 \ln N \approx 1.82 \ln N$$
Im Vergleich zur Binary Search ($\approx \ln N$) ist Ternary Search asymptotisch äquivalent, weist jedoch einen höheren konstanten Faktor bei der Anzahl der Vergleiche auf.

### Platzkomplexität
Der Algorithmus verwaltet unabhängig von der Eingabegröße $N$ nur eine feste Anzahl an Integer-Variablen ($L, R, m_1, m_2$). Es werden keine zusätzlichen Datenstrukturen proportional zur Eingabe alloziert. Somit ist die zusätzliche Platzkomplexität:
$$S(N) = O(1)$$