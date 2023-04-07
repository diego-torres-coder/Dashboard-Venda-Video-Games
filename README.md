# Dashboard de Vendas de Video Games

Este projeto é um dashboard que foi construído com os dados de vendas de video games disponibilizados na Kaggle neste link: https://www.kaggle.com/datasets/gregorut/videogamesales

Com este dashboard, o usuário pode filtrar os dados usando dois critérios: um intervalo de anos — desde 1980 até 2015 — e uma região — América do Norte, Europa, Japão e demais localidades. 

Na captura de tela a seguir, tem-se o cenário em que o usuário deseja obter o panorama de vendas de video games na América do Norte entre os anos de 1990 e 2010: 

![Vendas de video games na América do Norte entre 1990 e 2010](/dashboard-games.png "Vendas de video games na América do Norte entre 1990 e 2010")

Já na captura de tela a seguir tem-se o panorama de vendas de video games no Japão entre 2000 e 2010

![Vendas de video games no Japão entre 2000 e 2010](/dashboard-games-japao.png "Vendas de video games no Japão entre 2000 e 2010")

## Bibliotecas Usadas

Neste projeto, foram usadas as seguintes bibliotecas:

- pandas
- plotly
- streamlit

## Como Reproduzir este Projeto

Se você deseja reproduzir este projeto em sua máquina, siga o passo a passo a seguir.

Inicialmente, crie uma pasta para abrigar o projeto e navegue até ela. Em seguida, clone este repositório com o seguinte comando:

```bash
git clone https://github.com/diego-torres-coder/Dashboard-Venda-Video-Games.git
```

Navegue para a pasta recém-criada com o comando anterior:

```bash
cd Dashboard-Venda-Video-Games/
```

Crie um ambiente virtual para o projeto:

```bash
conda create -n stenv-dashboard-games python=3.10
```

Com o ambiente já criado, ative-o:

```bash
conda activate stenv-dashboard-games
```

Instale as dependências do projeto:

```bash
pip install numpy openpyxl pandas plotly-express streamlit
```

Em vez de instalar as dependências como sugere o passo anterior, você pode usar o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Por fim, execute o script `app.py`:

```bash
streamlit run app.py
```
