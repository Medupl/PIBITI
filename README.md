# 📡 Modelagem de Equalizadores Adaptativos para Comunicações Ópticas Coerentes com Processamento Acelerado por GPU  

## 🔎 Resumo
A otimização computacional é essencial em sistemas de comunicações ópticas coerentes, que processam grandes volumes de dados em tempo real. Como simulações de receptores ópticos demandam alto custo computacional, o uso de **GPU** surge como solução eficiente.  

Este projeto estuda e implementa modelos numéricos de **equalização adaptativa no domínio da frequência**, utilizando **Python** e a biblioteca **CuPy** para aceleração por GPU. São avaliados algoritmos como **Constant Modulus Algorithm (CMA)** **Radius-Directed Equalizer (RDE)**e **Decision-Directed LMS (DD-LMS)**, comparando desempenho entre CPU e GPU.  

---

<p align="center">
  
<img src="https://github.com/edsonportosilva/OpticalCommunications/blob/cb0be56856b0b5f30779b4464b12055b600c1a56/jupyter%20notebooks/figuras/sistemaCoerente.png" width="800">

</p>

## 📘 Introdução
Sistemas de comunicações ópticas coerentes são fundamentais para atender a crescente demanda por **largura de banda** e **altas taxas de transmissão**. Entretanto, os sinais sofrem com distorções como **dispersão cromática (CD)** e **dispersão de modo de polarização (PMD)**.  

- **Equalizadores estáticos**: parâmetros fixos, adequados para distorções previsíveis.  
- **Equalizadores adaptativos**: ajustam parâmetros em tempo real, compensando distorções dinâmicas.  

O objetivo deste repositório é fornecer **implementações práticas e anotações** sobre equalizadores adaptativos aplicados a comunicações ópticas coerentes, explorando o **processamento acelerado em GPU**.  

---

## 📂 Sumário do Material 
Cada notebook aborda a implementação e a análise de um bloco fundamental de um sistema óptico coerente, desde a geração do sinal QAM no transmissor até a avaliação final de desempenho com o cálculo do BER.

- [# 0: Capacitação](Capacitacao)  
- [# 1: Numpy](Capacitacao/Numpy)  
- [# 2: Cupy](Capacitacao/CudaPy)
- [# 3: Git-GitHub](Capacitacao/Git-GitHub)
- [# 4: Introdução a Optica](Capacitacao/Optic)  
- [# 5: Comunicacoes Opticas](Capacitacao/Comunicacoes-Opticas)  
- [# 6: Equalizadores-Adaptativos](Capacitacao/Equalizadores-Adaptativos)     

---

## Importante

<p align="center">
<img src="https://github.com/edsonportosilva/OptiCommPy/blob/main/figures/logo_OptiCommPy.jpg" width="500">
</p>

Nesse material foi usando a [OptiCommPy](https://github.com/edsonportosilva/OptiCommPy) para implementar as simulações de todos os códigos, desde geração inicial de sinais até simulações de sistemas reias de fibras ópticas coerentes.

