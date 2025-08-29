# 📡 Modelagem de Equalizadores Adaptativos para Comunicações Ópticas Coerentes com Processamento Acelerado por GPU  

## 🔎 Resumo
A otimização computacional é essencial em sistemas de comunicações ópticas coerentes, que processam grandes volumes de dados em tempo real. Como simulações de receptores ópticos demandam alto custo computacional, o uso de **GPU** surge como solução eficiente.  

Este projeto estuda e implementa modelos numéricos de **equalização adaptativa no domínio da frequência**, utilizando **Python** e a biblioteca **CuPy** para aceleração por GPU. São avaliados algoritmos como **Constant Modulus Algorithm (CMA)** e **Decision-Directed LMS (DD-LMS)**, comparando desempenho entre CPU e GPU.  

---

## 📘 Introdução
Sistemas de comunicações ópticas coerentes são fundamentais para atender a crescente demanda por **largura de banda** e **altas taxas de transmissão**. Entretanto, os sinais sofrem com distorções como **dispersão cromática (CD)** e **dispersão de modo de polarização (PMD)**.  

- **Equalizadores estáticos**: parâmetros fixos, adequados para distorções previsíveis.  
- **Equalizadores adaptativos**: ajustam parâmetros em tempo real, compensando distorções dinâmicas.  

O objetivo deste repositório é fornecer **implementações práticas e anotações** sobre equalizadores adaptativos aplicados a comunicações ópticas coerentes, explorando o **processamento acelerado em GPU**.  

---

## 📑 Sumário do Material
Os principais blocos de DSP foram organizados em cadernos Jupyter, baseados no livro *Digital Coherent Optical Systems Architecture and Algorithms*:  

- [Chapter 2: The Optical Transmitter](Capacitacao/Comunicacoes-Opticas/Codigos_de_C_O.ipynb)  
- [Chapter 3: The Optical Channel](./Optic)  
- [Chapter 4: The Receiver Front-End, Orthogonalization, and Deskew](./Numpy)  
- [Chapter 5: Equalization](./Equalizadores-Adaptativos)  
- [Chapter 6: Carrier Recovery](./CudaPy)  
- [Chapter 7: Clock Recovery](./Comunicacoes-Opticas)  
- [Chapter 8: Performance Evaluation](./Git-GitHub)  

---

## 📂 Estrutura do Repositório
