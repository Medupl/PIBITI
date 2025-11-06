## 🏗️ Estrutura do Projeto

O projeto está organizado em notebooks Jupyter, cada um abordando uma etapa fundamental da cadeia de simulação de um sistema de comunicação óptica.


* **# Equalizadores:** O coração do projeto. Implementação e teste de algoritmos de equalização adaptativa MIMO 2x2 para mitigar distorções do canal, como a Dispersão de Modo de Polarização (PMD). Implementação de algoritmos de recuperação de fase (CPR), como o Blind Phase Search (BPS), para compensar o ruído de fase dos lasers e o deslocamento de frequência. Cálculo de métricas chave como Taxa de Erro de Bit (BER), Taxa de Erro de Símbolo (SER) e Relação Sinal-Ruído (SNR) para validar o sistema. Algoritmos: Constant Modulus Algorithm (CMA) ;  Radius-Directed Equalization (RDE) ;  Decision-Directed Least Mean Squares (DD-LMS)
    - [# 6.1 - Equalização    ](./Equalizadores-Adaptativos/Equalização.ipynb)
    - [# 6.2 - MIMO_2x2](./Equalizadores-Adaptativos/MIMO_2x2.ipynb)
    - [# 6.3 - Revisao Implementacao Cupy](./Equalizadores-Adaptativos/Revisao_Implementacao_Cupy.ipynb)
    - [# 6.4 - Desempenho CPU_GPU](./Equalizadores-Adaptativos/Desempenho_CPU_GPU.ipynb)
---
