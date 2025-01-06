# Modelagem de Equalizadores Adaptativos para Comunicações Ópticas Coerentes com Processamento Acelerado por GPU

## - Resumo

A importância da otmização computacional em sistemas de comunicações ópticas coerentes é crucial, pois precisam de grandes volumes de dados m tempo real. Devido o desenvolvimento de circuitos integrados para receptores ópticos exigirem simulações demoradas e alto custo computacional, a $GPU$ se destaca como solução eficiente.

O projeto visa o estudo e a implementação de modelos numéricos para equalização adaptativa no dominio da frequência aplicado às comunicações opticas coerentes. As etapas iniciais envolvem revisão da literatura para identificar métodos mais relevantes, seguidos pela implementação dos algoritmos em $Python$. A fase final envolve a implementação da biblioteca $Cupy$ para aproveitar o processamento acelerado por $GPU$.

## - Introdução

As comunicações coerentes tem se destacado à crescente demamda por largura de banda e alta velociade em transmissão. Um dos desafios enfrentados são as distorções causadas aos sinais, que podem ser solucionadas por meio de qequalizadores baseados em processamento digital de sinais.

Os equalizadores podem ser estáticos ou dinânmicos. Um equalizador estático possui seus parâmetros predefinidos, adequados para sistemas estáveis e previsíves, no caso de dispersão cromática. Um equalizador adaptativo, ou dinâmico, o algoritmo atualiza seus parâmetros em tempo real para compensar as distorções do sinal, permitindo uma compensação eficaz e com isso porpocional um melhor desempenho.

Este projeto visa desenvolver e implementar equalizadores adaptativos para sistemas de comunicações ópticas coerentes, utilizando Python e processamento acelerado por GPU, com bibliotecas como CuPy. O foco está em compensar distorções causadas por fenômenos como dispersão de modo de polarização (PMD) e dispersão cromática (CD). O objetivo é melhorar o desempenho dos sistemas de comunicação óptica através da otimização de algoritmos de processamento digital de sinais (DSP), essenciais para a recuperação precisa de dados em sistemas de alta velocidade. O projeto envolve a implementação de algoritmos adaptativos, como o Constant Modulus Algorithm (CMA) e o Decision-Directed Least Mean Square (DD-LMS), e seu desempenho será comparado com versões tradicionais em CPU.
