# 🧠 Equalizadores Adaptativos

Esta pasta contém notebooks dedicados ao estudo, implementação e análise de **algoritmos de equalização adaptativa** para sistemas de comunicação óptica coerente.  
O foco está na **mitigação de distorções do canal** — como Dispersão de Modo de Polarização (PMD) e ruído de fase — utilizando modelos MIMO 2×2 e técnicas de aprendizado adaptativo.

---

## 🏗️ Estrutura dos Notebooks

Cada notebook aborda uma etapa específica do pipeline de simulação e compensação digital.

| Notebook | Descrição |
|-----------|------------|
| [#1 - Equalização](./Equalização.ipynb) | Implementação dos algoritmos de equalização adaptativa, com recuperação de fase (CPR) e análise de constelações. |
| [#2 - MIMO_2x2](./MIMO_2x2.ipynb) | Estrutura completa do equalizador MIMO 2×2 para compensação de PMD e rotação de polarização. |
| [`Revisao_Implementacao_Cupy.ipynb`](./Revisao_Implementacao_Cupy.ipynb) | Versão otimizada em GPU utilizando **CuPy**, explorando aceleração via CUDA. |
| [`Desempenho_CPU_GPU.ipynb`](./Desempenho_CPU_GPU.ipynb) | Análise comparativa de desempenho entre CPU (NumPy) e GPU (CuPy), incluindo tempo de execução, convergência e métricas de BER/SNR. |

---

## 🧩 Algoritmos Implementados

Os equalizadores utilizam técnicas clássicas de adaptação e compensação de canal óptico:

- **CMA** – *Constant Modulus Algorithm*  
  Reduz a variação de módulo para convergência cega inicial.
- **RDE** – *Radius-Directed Equalization*  
  Aperfeiçoa a convergência usando os raios da constelação QAM.
- **DD-LMS** – *Decision-Directed Least Mean Squares*  
  Fase final de refinamento baseada nas decisões de símbolo.
- **CPR (BPS)** – *Blind Phase Search*  
  Recupera a fase do portador e corrige o deslocamento de frequência residual.

---

## 📊 Métricas de Desempenho

Os resultados são avaliados a partir de:
- **Taxa de Erro de Símbolo (SER)**  
- **Taxa de Erro de Bit (BER)**  
- **Relação Sinal-Ruído (SNR)**  
- **Tempo de Execução (CPU × GPU)**  

Essas métricas permitem validar a eficiência dos algoritmos e quantificar o ganho da aceleração por GPU.

---
