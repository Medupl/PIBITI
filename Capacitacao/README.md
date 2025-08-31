## 🏗️ Estrutura do Projeto

O projeto está organizado em notebooks Jupyter, cada um abordando uma etapa fundamental da cadeia de simulação de um sistema de comunicação óptica.

* **# 1: Numpy:** Introdução a biblioteca que é muito utilizada em diversas áreas de comunicações ópticas, simplificando vários cálculos.
* **# 2: Cupy:** Biblioteca muito similar a Numpy, pórem voltada ao uso da **GPU**, importante para as comunicações coerentes.
* **# 3: Git-GitHub:** Algumas dicas importantes para quem está iniciando na programação e precisa aprender a mexer com Git.
* **# 4: Introdução a Optica:** Início aos conteúdos de comunicações ópticas: 
    - [# 4.1 - Analise de Sinais e Sistemas](./Optic/Analise_de_sinais_e_sistemas.ipynb)
    - [# 4.2 - Filtros Adaptativos](./Optic/Filtros_adaptivos.ipynb)
    - [# 4.3 - Processamento de digital de sinal](./Optic/Processamento_digital_de_sinal.ipynb)
* **# 5: Comunicacoes Opticas:** Estudos de todos os processos da fibra óptica, desde a escolha do modulador até as comunicações coerentes.
    - [# 5.1 - Comunicações Opticas](./Comunicacoes-Opticas/Comunicações_Opticas.ipynb.ipynb)
    - [# 5.2 - Exemplos de CO](./Comunicacoes-Opticas/Codigos_de_C_O.ipynb)
    - [# 5.3 - Receptores Opticos e Ruído](./Comunicacoes-Opticas/Receptores_Opticos_e_Ruído.ipynb)
    - [# 5.4 - Fibra Optica](./Comunicacoes-Opticas/Fibra_Optica.ipynb)
    - [# 5.5 - Dispersao e Perda](./Comunicacoes-Opticas/Dispersao_e_Perda.ipynb)
    - [# 5.6 - Propagação de Pulsos ópticos SSFM](./Comunicacoes-Opticas/Propagação_de_Pulsos_ópticos_SSFM.ipynb)
    - [# 5.7 - Amplificador fibra dopada com érbio EDFA](./Comunicacoes-Opticas/Amplificador_fibra_dopada_com_érbio_EDFA.ipynb)
    - [# 5.8 - Comunicações Ópticas Coerentes](./Comunicacoes-Opticas/Comunicações_Ópticas_Coerentes.ipynb)
* **# 6: Equalizadores:** O coração do projeto. Implementação e teste de algoritmos de equalização adaptativa MIMO 2x2 para mitigar distorções do canal, como a Dispersão de Modo de Polarização (PMD).
* Implementação de algoritmos de recuperação de fase (CPR), como o Blind Phase Search (BPS), para compensar o ruído de fase dos lasers e o deslocamento de frequência.
* **Capítulo 7: Recuperação de Clock:** Estudo de técnicas de sincronismo de tempo.
* Cálculo de métricas chave como Taxa de Erro de Bit (BER), Taxa de Erro de Símbolo (SER) e Relação Sinal-Ruído (SNR) para validar o sistema
    * Constant Modulus Algorithm (CMA)
    * Radius-Directed Equalization (RDE)
    * Decision-Directed Least Mean Squares (DD-LMS)YYYYYY
 
---

## 🎯 Objetivos

Este projeto visa atingir os seguintes objetivos:

* **Implementar e Prototipar:** Desenvolver um simulador funcional em Python para os principais blocos de um transceptor óptico coerente.
* **Acelerar com GPU:** Integrar a biblioteca CuPy para portar os algoritmos computacionalmente intensivos (principalmente os equalizadores) para a GPU, visando uma redução drástica no tempo de simulação.
* **Avaliar e Comparar:** Analisar o desempenho de diferentes algoritmos de equalização (CMA, RDE, DD-LMS) na compensação de distorções do canal.
* **Validar a Performance:** Realizar um benchmark comparativo entre a execução em CPU (com NumPy) e em GPU (com CuPy) para quantificar o ganho de aceleração.

---
