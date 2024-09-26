# Punch Clock - PIBIT

Repositório direcionado para registrar a entrada e saída do colaborador do projeto Modelagem de Equalizadores Adaptativos para Comunicações Ópticas Coerentes com Processamento Acelerado por GPU

## Passo a Passo

### 1. Clone o repositório:
> Eu usei o modo SSH, para isso foi necessário criar uma [SSH key](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). Esse link leva até o documento no próprio GitHub que ensina como criar a Key e adicionar na sua conta.

> É possível clonar por meio do HTTPS.

### 2. Comandos:

Após o clone você terá a pasta do punchClock na pasta do projeto no seu diretório. Agora você ira até a pasta do projeto: 
> cd ./PIBIT

#### Atualize o repositório
> git pull

#### Criando um arquivo para registro:
> - cd ./PunchClock
> 
> - touch SEU_NOME.txt

#### Para registrar a entrada:
> python punchClock/punchClock.py SEU_NOME in 

#### Para registrar a saída:
> python punchClock/punchClock.py SEU_NOME out

> Descreva o que você fez dentro daquele ponto.

