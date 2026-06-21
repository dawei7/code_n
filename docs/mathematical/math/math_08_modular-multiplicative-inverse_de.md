# Formale mathematische Spezifikation: Modulare multiplikative Inverse

## 1. Definitionen und Notation

Sei $\mathbb{Z}$ die Menge der ganzen Zahlen. Gegeben eine ganze Zahl $a \in \mathbb{Z}$ und ein Modul $m \in \mathbb{Z}^+$, definieren wir die **modulare multiplikative Inverse** als eine ganze Zahl $x$, sodass die Kongruenzrelation gilt:
$$ax \equiv 1 \pmod{m}$$
Der Definitionsbereich der Eingabe ist $(a, m) \in \mathbb{Z} \times \mathbb{Z}^+$. Der Ausgaberaum ist $\mathcal{X} = \{x \in \mathbb{Z} \mid 0 \le x < m\} \cup \{-1\}$, wobei $-1$ die Nichtexistenz einer Inversen kennzeichnet.

Die Existenz von $x$ wird durch die Bedingung $\gcd(a, m) = 1$ bestimmt. Wenn $\gcd(a, m) = d > 1$, dann gilt für jedes $x$, dass $ax \equiv 0 \pmod{d}$, was impliziert, dass $ax \not\equiv 1 \pmod{m}$, da $1 \not\equiv 0 \pmod{d}$. Somit existiert die Inverse genau dann, wenn $a$ und $m$ teilerfremd sind.

## 2. Algebraische Charakterisierung

### Der erweiterte euklidische Ansatz
Die Kongruenz $ax \equiv 1 \pmod{m}$ ist äquivalent zur Existenz einer ganzen Zahl $y \in \mathbb{Z}$, sodass:
$$ax + my = 1$$
Dies ist eine lineare diophantische Gleichung, ein Spezialfall der Bézout-Identität. Der erweiterte euklidische Algorithmus (EEA) berechnet den größten gemeinsamen Teiler $g = \gcd(a, m)$ und die Koeffizienten $(x, y)$, sodass $ax + my = g$.

Der Algorithmus verläuft unter Beibehaltung der Invariante:
$$r_i = s_i a + t_i m$$
wobei $r_i$ der Rest im Schritt $i$ ist. Gegeben die Rekurrenz $r_{i-2} = q_i r_{i-1} + r_i$, werden die Koeffizienten wie folgt aktualisiert:
$$s_i = s_{i-2} - q_i s_{i-1}$$
$$t_i = t_{i-2} - q_i t_{i-1}$$
Nach Abschluss gilt $r_k = \gcd(a, m)$. Wenn $r_k = 1$, ist die modulare Inverse $x \equiv s_k \pmod{m}$. Um sicherzustellen, dass $x \in [0, m-1]$ liegt, berechnen wir $x = (s_k \pmod{m} + m) \pmod{m}$.

### Kleiner Fermatscher Satz (Spezialfall)
Wenn $m = p$ gilt, wobei $p$ eine Primzahl ist und $p \nmid a$, besagt der kleine Fermatsche Satz:
$$a^{p-1} \equiv 1 \pmod{p}$$
Multiplikation mit $a^{-1}$ ergibt:
$$a^{p-2} \equiv a^{-1} \pmod{p}$$
Dies charakterisiert die Inverse als Potenzfunktion in der multiplikativen Gruppe $(\mathbb{Z}/p\mathbb{Z})^\times$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird vom euklidischen Algorithmus dominiert. Sei $T(a, m)$ die Anzahl der Schritte. Nach dem Satz von Lamé ist die Anzahl der Divisionen, die zur Berechnung von $\gcd(a, m)$ erforderlich sind, höchstens $5 \cdot \lfloor \log_{10}(\min(a, m)) \rfloor + 1$.

Da jeder Schritt eine konstante Anzahl an arithmetischen Operationen (Division, Multiplikation, Subtraktion) umfasst, beträgt die gesamte Zeitkomplexität:
$$T(n) = O(\log(\min(a, m)))$$
Im Kontext der Eingabegröße $n = \log_2(m)$ entspricht dies $O(n)$, was linear in Bezug auf die Anzahl der Bits im Modul ist.

### Platzkomplexität
Die iterative Implementierung des erweiterten euklidischen Algorithmus verwaltet eine konstante Anzahl an Variablen ($r, s, q, \text{old\_r}, \text{old\_s}$), unabhängig von der Größe von $a$ oder $m$.

- **Zusätzlicher Speicherplatz:** $O(1)$, da wir nur den aktuellen und den vorherigen Zustand der Rest- und Koeffizientenfolgen speichern.
- **Gesamter Speicherplatz:** $O(1)$ (exklusive des Speicherplatzes, der für die Eingabezahlen selbst benötigt wird).

Bei einer rekursiven Implementierung läge die Platzkomplexität aufgrund der Tiefe des Call Stacks bei $O(\log(\min(a, m)))$, aber die iterative Formulierung erreicht die optimale Schranke von $O(1)$.