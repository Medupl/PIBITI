import numpy as np
import cupy as cp
import numpy.lib.stride_tricks
import cupy.lib.stride_tricks
from tqdm.notebook import tqdm

from optic.dsp.core import pnorm, grayMapping

def create_windows(x, paramEq):
    """
    xp = np ou xp dependendo da biblioteca usada (cupy ou numpy)
    Cria janelas temporais para polarização X e Y (coluna 0 e coluna 1), organizadas do tap mais antigo → tap mais novo.
    Essas matrizes são usadas posteriormente pelo equalizador adaptativo.

    Parametros
    ----------
    x : xp.ndarray - Sinal recebido, no formato [N_amostras x 2], onde a coluna 0 = polarização X, coluna 1 = polarização Y.
    paramEq : parameters - Estrutura de parâmetros que contém o número de taps (paramEq.nTaps).

    Retorno
    -------
      - xV (xp.ndarray): matriz [N x nTaps] com janelas temporais da polarização X (coluna 0).
      - xH (xp.ndarray): matriz [N x nTaps] com janelas temporais da polarização Y (coluna 1).
    """
    # Decisão entre numpy e cupy para a biblioteca correta
    
    xp = paramEq.xp
    as_strided = xp.lib.stride_tricks.as_strided

    N = x.shape[0] - paramEq.nTaps + 1
    shape = (N, paramEq.nTaps)
    x0 = xp.ascontiguousarray(x[:, 0])                                          # Colocando x[:, 0] como sinal contíguos
    x1 = xp.ascontiguousarray(x[:, 1])                                          # Colocando x[:, 1] como sinal contíguos

    stridesx = x0.itemsize
    xV_ = as_strided(x0, shape=shape, strides=(stridesx,stridesx))
    xV = xV_[:, ::-1]                                                           # Polarização X é a coluna 0

    stridesy = x1.itemsize
    xH_ = as_strided(x1, shape=shape, strides=(stridesy,stridesy))
    xH = xH_[:, ::-1]                                                           # Polarização Y é a coluna 1

    return xV, xH

def ddlmsUp(x, constSymb, nModes, paramEq):
    """
    Equalizador DD-LMS para um sistema MIMO 2x2.
    Implementação amostra-por-amostra com lógica de atualização corrigida.
    Parameters
    ----------
      x : xp.array - Sinal de entrada após o canal (polarizações X e Y nas colunas 0 e 1).
      constSymb : xp.array - Conjunto de símbolos da constelação (ex: QPSK, 16QAM) para decisões bruscas.
      nModes : int - Número de modos/polarizações (tipicamente 2).
      paramEq : parameters - Estrutura contendo parâmetros do equalizador, incluindo:
        - nTaps : número de coeficientes do filtro FIR por ramo.
        - mu : passo de atualização do LMS.
        - progBar : habilita/desabilita barra de progresso.

    Returns
    -------
      - y (xp.array, shape = [N, nModes]): saída estimada do equalizador para cada modo.
      - e (xp.array, shape = [N, nModes]): erro de decisão (diferença entre símbolo decidido e saída).
      - w (xp.array, shape = [nTaps, nModes**2]): matriz de coeficientes do equalizador MIMO 2x2.
      Cada coluna corresponde a um dos quatro ramos do equalizador:
            w[:,0] → w_xx  (entrada X → saída X)
            w[:,1] → w_xy  (entrada Y → saída X)
            w[:,2] → w_yx  (entrada X → saída Y)
            w[:,3] → w_yy  (entrada Y → saída Y)
    """

    # Decisão entre numpy e cupy para a biblioteca correta
    xp = paramEq.xp

    # Parâmetros para o processamento em blocos
    blockSize = paramEq.blockSize
    N = x.shape[0] - paramEq.nTaps + 1
    nBlocks = N // blockSize

    if N <= 0:
      raise ValueError("Sinal curto demais para nTaps")

    # Obtém o atraso da filtragem FIR
    delay = (paramEq.nTaps - 1) // 2

    # --- Pré-alocação de Memória ---
    y = xp.zeros((len(x), nModes), dtype='complex')
    e = xp.zeros((len(x), nModes), dtype='complex')
    w = xp.zeros((paramEq.nTaps, nModes**2), dtype='complex')

    # single spike initialization
    w[delay, 0] = 1                                                             # Filtro principal w_xx (para o Mode 0)
    w[delay, 3] = 1                                                             # Filtro principal w_yy (para o Mode 1)

    for i in tqdm(range(nBlocks), disable=not(paramEq.progBar)):

        n = i * blockSize
        n_delay = delay + n + blockSize
        x_ = x[n : n + blockSize + paramEq.nTaps - 1, :]

        # cria janelas temporais para polarização X e Y (coluna 0 e coluna 1)
        xV, xH = create_windows(x_, paramEq)

        # calcula a saída do equalizador 2x2
        y[delay + n : n_delay, 0] = xV @ w[:, 0] + xH @ w[:, 1]
        y[delay + n : n_delay, 1] = xV @ w[:, 2] + xH @ w[:, 3]

        y0 = y[delay + n : n_delay, 0]
        y1 = y[delay + n : n_delay, 1]

        # decisão brusca
        d0 = constSymb[xp.argmin(xp.abs(y0[:, None] - constSymb), axis = 1)]
        d1 = constSymb[xp.argmin(xp.abs(y1[:, None] - constSymb), axis = 1)]

        e[delay + n : n_delay, 0] = d0 - y[delay + n : n_delay, 0]
        e[delay + n : n_delay, 1] = d1 - y[delay + n : n_delay, 1]

        # atualiza os coeficientes do filtro
        w[:,0] += paramEq.mu[1] * (xV.conj().T @ (e[delay + n : n_delay, 0])) / blockSize    # w_xx = w[:, 0]
        w[:,2] += paramEq.mu[1] * (xV.conj().T @ (e[delay + n : n_delay, 1])) / blockSize    # w_yx = w[:, 2]
        w[:,1] += paramEq.mu[1] * (xH.conj().T @ (e[delay + n : n_delay, 0])) / blockSize    # w_xy = w[:, 1]
        w[:,3] += paramEq.mu[1] * (xH.conj().T @ (e[delay + n : n_delay, 1])) / blockSize    # w_yy = w[:, 3]

    return y, e, w

def rdeUp(x, constSymb, nModes, paramEq, y=None, e=None, w=None, preConv=False):
    """
    Equalizador RDE (Radius-Directed Equalization) para um sistema MIMO 2x2.
    Implementação em blocos com lógica de atualização corrigida.

    Parameters
    ----------
    x : xp.array - Sinal de entrada após o canal (polarizações X e Y nas colunas 0 e 1).
    constSymb : xp.array - Conjunto de símbolos da constelação (ex: 16QAM) para obter os raios ideais.
    nModes : int - Número de modos/polarizações (tipicamente 2).
    paramEq : parameters - Estrutura contendo parâmetros do equalizador, incluindo:
        - nTaps : número de coeficientes do filtro FIR por ramo.
        - mu : passo de atualização do RDE.
        - N1 : iteração para o "kick" de ortogonalidade.
        - progBar : habilita/desabilita barra de progresso.
    y : xp.array, opcional - Array de saída pré-alocado (usado no modo preConv).
    e : xp.array, opcional - Array de erro pré-alocado (usado no modo preConv).
    w : xp.array, opcional - Matriz de pesos pré-convergidos do CMA (usado no modo preConv).
    preConv : bool, opcional - Flag que indica se a função está sendo chamada após uma pré-convergência CMA.

    Returns
    -------
    tuple
        - y (xp.array, shape = [N, nModes]): saída estimada do equalizador para cada modo.
        - e (xp.array, shape = [N, nModes]): erro de decisão do RDE.
        - w (xp.array, shape = [nTaps, nModes**2]): matriz de coeficientes do equalizador MIMO 2x2.
          Cada coluna corresponde a um dos quatro ramos do equalizador:
                w[:,0] → w_xx  (entrada X → saída X)
                w[:,1] → w_xy  (entrada Y → saída X)
                w[:,2] → w_yx  (entrada X → saída Y)
                w[:,3] → w_yy  (entrada Y → saída Y)

    Referências
    -----------
    [1] Digital Coherent Optical Systems, Architecture and Algorithms
    """

    # Decisão entre numpy e cupy para a biblioteca correta
    xp = paramEq.xp

    # Parâmetros para o processamento em blocos
    blockSize = paramEq.blockSize
    N = x.shape[0] - paramEq.nTaps + 1
    nBlocks = N // blockSize

    # Obtém o atraso da filtragem FIR
    delay = (paramEq.nTaps - 1) // 2

    # obtem os raios da constelação M-QAM
    Rrde = xp.unique(xp.abs(constSymb))

    if preConv == False:

        paramEq.N2 = 0

        y = xp.zeros((len(x), nModes), dtype='complex')
        e = xp.zeros((len(x), nModes), dtype='complex')
        w = xp.zeros((paramEq.nTaps, nModes**2), dtype='complex')

        # single spike initialization
        w[delay, 0] = 1                                                             # Filtro principal w_xx (para o Mode 0)
        w[delay, 3] = 1                                                             # Filtro principal w_yy (para o Mode 1)

    N1_block = paramEq.N1 // blockSize if paramEq.N1 > 0 else -1

    for i in tqdm(range(nBlocks), disable=not(paramEq.progBar)):

        n = i * blockSize
        n_delay = delay + n + blockSize
        x_ = x[n : n + blockSize + paramEq.nTaps - 1, :]

        # cria janelas temporais para polarização X e Y (coluna 0 e coluna 1)
        xV, xH = create_windows(x_, paramEq)

        # calcula a saída do equalizador 2x2
        y[delay + n : n_delay, 0] = xV @ w[:, 0] + xH @ w[:, 1]
        y[delay + n : n_delay, 1] = xV @ w[:, 2] + xH @ w[:, 3]

        y0 = xp.abs(y[delay + n : n_delay, 0])
        y1 = xp.abs(y[delay + n : n_delay, 1])

        R1 = xp.argmin(xp.abs(Rrde - y0[:, None]), axis = 1)
        R2 = xp.argmin(xp.abs(Rrde - y1[:, None]), axis = 1)

        # calcula e atualiza erro para cada modo de polarização
        e[delay + n : n_delay, 0] = y[delay + n : n_delay, 0] * (Rrde[R1]**2 - y0**2)
        e[delay + n : n_delay, 1] = y[delay + n : n_delay, 1] * (Rrde[R2]**2 - y1**2)

        # atualiza os coeficientes do filtro
        w[:,0] += paramEq.mu[0] * (xV.conj().T @ (e[delay + n : n_delay, 0])) / blockSize    # w_xx = w[:, 0]
        w[:,2] += paramEq.mu[0] * (xV.conj().T @ (e[delay + n : n_delay, 1])) / blockSize    # w_yx = w[:, 2]
        w[:,1] += paramEq.mu[0] * (xH.conj().T @ (e[delay + n : n_delay, 0])) / blockSize    # w_xy = w[:, 1]
        w[:,3] += paramEq.mu[0] * (xH.conj().T @ (e[delay + n : n_delay, 1])) / blockSize    # w_yy = w[:, 3]

        if i == N1_block:
            # Defina a polarização Y como ortogonal a X para evitar
            # a convergência para a mesma polarização (evitar a singularidade CMA)
            w[:,3] =  xp.conj(w[:,0][::-1])
            w[:,2] = -xp.conj(w[:,1][::-1])

    return y, e, w

def cmaUp(x, constSymb, nModes, paramEq, preConv=False):
    """
    Equalizador CMA (Constant-Modulus Algorithm) para um sistema MIMO 2x2.

    Esta função implementa o algoritmo CMA usando uma abordagem de
    processamento em blocos para alta performance em GPU. Ela é projetada
    para realizar a convergência cega inicial, separando as polarizações
    e compensando o deslocamento de frequência.

    Parameters
    ----------
    x : xp.array - Sinal de entrada após o canal (polarizações X e Y nas colunas 0 e 1).
    constSymb : xp.array - Conjunto de símbolos da constelação (ex: 16QAM) para obter os raios ideais.
    nModes : int - Número de modos/polarizações (tipicamente 2).
    paramEq : parameters - Estrutura contendo parâmetros do equalizador, incluindo:
        - nTaps : número de coeficientes do filtro FIR por ramo.
        - mu : passo de atualização do RDE.
        - N1 : iteração para aplicar o "kick" de ortogonalidade.
        - N2 : iteração para parar a fase de pré-convergência do CMA.
        - progBar : booleano para habilitar/desabilitar a barra de progresso.
    preConv : bool, opcional - Flag que ativa o modo de pré-convergência. Se True, o loop para na iteração N2. O padrão é False.

    Returns
    -------
      - y (xp.array, shape = [N, nModes]): saída estimada do equalizador para cada modo.
      - e (xp.array, shape = [N, nModes]): erro de decisão (diferença entre símbolo decidido e saída).
      - w (xp.array, shape = [nTaps, nModes**2]): matriz de coeficientes do equalizador MIMO 2x2.
      Cada coluna corresponde a um dos quatro ramos do equalizador:
            w[:,0] → w_xx  (entrada X → saída X)
            w[:,1] → w_xy  (entrada Y → saída X)
            w[:,2] → w_yx  (entrada X → saída Y)
            w[:,3] → w_yy  (entrada Y → saída Y)

    Referências
    -----------
    [1] Digital Coherent Optical Systems, Architecture and Algorithms
    """

    # Decisão entre numpy e cupy para a biblioteca correta
    xp = paramEq.xp

    # Parâmetros para o processamento em blocos
    blockSize = paramEq.blockSize
    N = x.shape[0] - paramEq.nTaps + 1
    blocks_default = N // blockSize

    if N <= 0:
      raise ValueError("Sinal curto demais para nTaps")

    # Obtém o atraso da filtragem FIR
    delay = (paramEq.nTaps - 1) // 2

    y = xp.zeros((len(x), nModes),  dtype='complex')
    e = xp.zeros((len(x), nModes),  dtype='complex')
    w = xp.zeros((paramEq.nTaps, nModes**2),  dtype='complex')

    # single spike initialization
    w[delay, 0] = 1                                                             # Filtro principal w_xx (para o Mode 0)
    w[delay, 3] = 1                                                             # Filtro principal w_yy (para o Mode 1)

    # constante relacionada às características da modulação para o algoritmo CMA
    R = xp.mean(xp.abs(constSymb)**4) / xp.mean(xp.abs(constSymb)**2)

    N1_block = paramEq.N1 // blockSize if paramEq.N1 > 0 else -1
    nBlocks = paramEq.N2 // blockSize if preConv else blocks_default

    for i in tqdm(range(nBlocks), disable=not(paramEq.progBar)):

        n = i * blockSize
        n_delay = delay + n + blockSize
        x_ = x[n : n + blockSize + paramEq.nTaps - 1, :]

        # cria janelas temporais para polarização X e Y (coluna 0 e coluna 1)
        xV, xH = create_windows(x_, paramEq)

        # calcula a saída do equalizador 2x2
        y[delay + n : n_delay, 0] = xV @ w[:, 0] + xH @ w[:, 1]
        y[delay + n : n_delay, 1] = xV @ w[:, 2] + xH @ w[:, 3]

        # calcula e atualiza erro para cada modo de polarização
        e[delay + n : n_delay, 0] = y[delay + n : n_delay, 0] * (R - xp.abs(y[delay + n : n_delay, 0])**2)
        e[delay + n : n_delay, 1] = y[delay + n : n_delay, 1] * (R - xp.abs(y[delay + n : n_delay, 1])**2)

        # atualiza os coeficientes do filtro
        w[:,0] += paramEq.mu[0] * (xV.conj().T @ (e[delay + n : n_delay, 0])) / blockSize    # w_xx = w[:, 0]
        w[:,2] += paramEq.mu[0] * (xV.conj().T @ (e[delay + n : n_delay, 1])) / blockSize    # w_yx = w[:, 2]
        w[:,1] += paramEq.mu[0] * (xH.conj().T @ (e[delay + n : n_delay, 0])) / blockSize    # w_xy = w[:, 1]
        w[:,3] += paramEq.mu[0] * (xH.conj().T @ (e[delay + n : n_delay, 1])) / blockSize    # w_yy = w[:, 3]

        # Ortogonalização CMA apenas uma vez quando N1 for atingido
        if i == N1_block:
            w[:,3] =  xp.conj(w[:,0][::-1])
            w[:,2] = -xp.conj(w[:,1][::-1])

    if preConv:
        w_ = xp.max(xp.abs(w))
        w = w/w_ if w_ > 1e-6 else w
        y, e, w = rdeUp(x, constSymb, nModes, paramEq, y, e, w, preConv=True)

    return y, e, w

def mimoAdaptEq(x, paramEq):
    """
    Equalizador adaptativo MIMO 2x2

    Returns
    -------
    tuple
        - y (np.array): estimativa dos símbolos.
        - e (np.array): erro associado a cada modo de polarização.
        - w (np.array): matriz de coeficientes.

    Raises
    ------
    ValueError
        Caso o sinal não possua duas polarizações.

    ValueError
        Caso o algoritmo seja especificado incorretamente.
    """

    if x.shape[1] != 2:
        raise ValueError("O sinal deve conter duas polarizações")

    nModes = x.shape[1]

    # obtem os símbolos da constelação
    constSymb = grayMapping(paramEq.M, paramEq.constType)
    # normaliza os símbolos da constelação
    constSymb = pnorm(constSymb)
    
    if isinstance(x, cp.ndarray):
      constSymb = cp.asarray(constSymb)
      paramEq.xp = cp
    elif isinstance(x, np.ndarray):
      paramEq.xp = np

    if paramEq.alg == 'cma':
        y, e, w = cmaUp(x, constSymb, nModes, paramEq)
    elif paramEq.alg == 'rde':
        y, e, w = rdeUp(x, constSymb, nModes, paramEq)
    elif paramEq.alg == 'cma-to-rde':
        y, e, w = cmaUp(x, constSymb, nModes, paramEq, preConv=True)
    elif paramEq.alg == 'dd-lms':
        y, e, w = ddlmsUp(x, constSymb, nModes, paramEq)
    else:
        raise ValueError("Algoritmo de equalização especificado incorretamente.")

    return y, e, w