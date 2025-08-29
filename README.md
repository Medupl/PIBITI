# Modelagem e Aceleração por GPU de Equalizadores Adaptativos para Comunicações Ópticas Coerentes

Este repositório documenta o projeto de pesquisa e desenvolvimento focado na modelagem, implementação e otimização de algoritmos de equalização adaptativa para sistemas de comunicação óptica coerente, com ênfase na aceleração de performance utilizando Unidades de Processamento Gráfico (GPUs).

O projeto utiliza a linguagem Python e a biblioteca CuPy como ferramentas para prototipagem rápida e computação de alta performance. A principal referência teórica para os algoritmos implementados é o livro "Digital Coherent Optical Systems: Architecture and Algorithms".

---

## 🏗️ Estrutura do Projeto

O projeto está organizado em notebooks Jupyter, cada um abordando uma etapa fundamental da cadeia de simulação de um sistema de comunicação óptica.

* **Capítulo 2: O Transmissor Óptico:** Geração de sequências de bits, mapeamento para constelações complexas (ex: 64-QAM com código Gray) e formatação de pulso (RRC).
* **Capítulo 3: O Canal Óptico:** Simulação da propagação do sinal através da fibra óptica monomodo, modelando efeitos lineares como a Dispersão Cromática (CD).
* **Capítulo 4: O Receptor Coerente:** Modelagem do receptor óptico coerente com diversidade de polarização, incluindo o Oscilador Local (LO) e os fotodetectores balanceados.
* **Capítulo 5: Equalização:** O coração do projeto. Implementação e teste de algoritmos de equalização adaptativa MIMO 2x2 para mitigar distorções do canal, como a Dispersão de Modo de Polarização (PMD).
    * Constant Modulus Algorithm (CMA)
    * Radius-Directed Equalization (RDE)
    * Decision-Directed Least Mean Squares (DD-LMS)
* **Capítulo 6: Recuperação de Portadora:** Implementação de algoritmos de recuperação de fase (CPR), como o Blind Phase Search (BPS), para compensar o ruído de fase dos lasers e o deslocamento de frequência.
* **Capítulo 7: Recuperação de Clock:** Estudo de técnicas de sincronismo de tempo.
* **Capítulo 8: Avaliação de Desempenho:** Cálculo de métricas chave como Taxa de Erro de Bit (BER), Taxa de Erro de Símbolo (SER) e Relação Sinal-Ruído (SNR) para validar o sistema.

---

## 🎯 Objetivos

Este projeto visa atingir os seguintes objetivos:

* **Implementar e Prototipar:** Desenvolver um simulador funcional em Python para os principais blocos de um transceptor óptico coerente.
* **Acelerar com GPU:** Integrar a biblioteca CuPy para portar os algoritmos computacionalmente intensivos (principalmente os equalizadores) para a GPU, visando uma redução drástica no tempo de simulação.
* **Avaliar e Comparar:** Analisar o desempenho de diferentes algoritmos de equalização (CMA, RDE, DD-LMS) na compensação de distorções do canal.
* **Validar a Performance:** Realizar um benchmark comparativo entre a execução em CPU (com NumPy) e em GPU (com CuPy) para quantificar o ganho de aceleração.

---

## 📈 Resultados Visuais

A eficácia da cadeia de Processamento Digital de Sinais (DSP) pode ser visualizada através da evolução da constelação do sinal em diferentes etapas do receptor. Um sinal que chega completamente distorcido é gradualmente "limpo" por cada bloco de DSP.

| 1. Sinal Detectado (Após o Canal) | 2. Após Compensação de Dispersão | 3. Após Equalização Cega (CMA/RDE) | 4. Após Recuperação de Fase (CPR) |
| :---: | :---: | :---: | :---: |
| ![Sinal Detectado](https://googleusercontent.com/file_content/48) | ![Após EDC](https://googleusercontent.com/file_content/49) | ![Após EQ](https://googleusercontent.com/file_content/50) | ![Após CPR](https://googleusercontent.com/file_content/51) |
| O sinal chega como uma "nuvem" disforme devido à dispersão e mistura de polarizações. | O EDC remove o "borrão" temporal, revelando uma estrutura de anéis giratórios causada pelo offset de frequência. | O equalizador MIMO separa as polarizações e trava a frequência, resultando em anéis estáticos mas borrados. | O CPR remove o ruído de fase, fazendo os anéis "colapsarem" nos pontos da constelação QAM. |

---

## 🚀 Como Executar

Para executar esta simulação, siga os passos abaixo.

### Pré-requisitos
* Python 3.8+
* Git
* Uma GPU NVIDIA com a plataforma CUDA instalada (para a versão acelerada)

### Instalação
1.  Clone este repositório:
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DA_PASTA]
    ```
2.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    .\venv\Scripts\activate    # No Windows
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Uso
Navegue pelos notebooks Jupyter na ordem dos capítulos para acompanhar o desenvolvimento e a análise de cada bloco do sistema. O notebook principal, que integra todos os componentes, pode ser encontrado em `[caminho/para/seu/notebook_final.ipynb]`.
