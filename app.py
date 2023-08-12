# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.



from tkinter.tix import InputOnly
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from flask import Flask


####firebase###




# initialise the flask app
server = Flask(__name__)

#app = Dash(__name__)

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB,
        "https://www.gstatic.com/firebasejs/ui/4.7.1/firebase-ui-auth.css",
                                          dbc.icons.BOOTSTRAP],external_scripts=[
        "https://www.gstatic.com/firebasejs/8.0.1/firebase-auth.js",
        "https://www.gstatic.com/firebasejs/ui/4.7.1/firebase-ui-auth.js",
    ],)








# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# Our dataframe
data1 = pd.read_csv('testeagrupamento.csv',sep=";")
dataR = pd.read_csv('gLinha.csv',sep=";")



#plotagem
figL = px.line(dataR, x="Dias da Semana", y="Quantidade", color='Grupos',color_discrete_sequence=px.colors.qualitative.Plotly)
figL.update_xaxes(title = 'Períodos Mensais')
figL.update_yaxes(title = 'Quantidade Respostas')
figL.update_layout(autosize=False,width=900,height=600)
figL.update_layout(title={
    'text' : 'Tendência de Respostas no Fórum ao Longo do Tempo',
    'y':0.96,
    'x': 0.1
})


figL.update_traces(opacity=.6)


#####

fig = px.area(data1,x='Semanas' ,y='Quantidade', color="Grupos", title="Acesso por dia da semana",color_discrete_sequence=px.colors.qualitative.Plotly)

fig.update_layout(autosize=False,width=900,height=600)
fig.update_layout(title={
    'text' : 'Comparar a Quantidade de Visualização dos Grupos no Ambiente ao Longo do Tempo',
    'y':0.96,
    'x': 0.1
})
fig.update_xaxes(title = 'Períodos Mensais')
fig.update_yaxes(title = 'Quantidade Visualização')



#HTML 


####mexe aqui dentroapenas



######nao mexer abaixo



card_sales = dbc.Card(
    dbc.CardBody(
        [
            html.H1("Total Alunos", className="text-nowrap"),
            html.H3("106.7M"),
            html.Div(
                [html.I("5.8%",
                    className="bi bi-caret-up-fill text-success"),
                " vs LY",]
            ),
        ], className="border-start border-success border-5"
    ),
    className="text-center m-4"
)


card_profit = dbc.Card(
    dbc.CardBody(
        [
            html.H1("Média Avaliações",
                    className="text-nowrap"),
            html.H3("8.3M",),
            html.Div(
                [
                    html.I("12.3%",
                    className="bi bi-caret-down-fill text-danger"),
                    " vs LY",
                ]
            ),
        ], className="border-start border-danger border-5"
    ),
    className="text-center m-4",
)




card_orders = dbc.Card(
    dbc.CardBody(
        [
            html.H1( "Orders",
                    className="text-nowrap"),
            html.H3("91.4K"),
            html.Div(
                [
                 html.I("10.3%",
                     className="bi bi-caret-up-fill text-success"),
                 " vs LY",
                ]
            ),
        ], className="border-start border-success border-5"
    ),
    className="text-center m-4",
),


slider = dcc.Slider(min=0, max=20, step=5, value=10),




app.layout = html.Div(children=[
    html.H1(children='Engajamento em Ambientes EaD'),


    ###


html.Div([
        html.Label(['Escolha a Disciplina:'],style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': 'Metodologia Científica', 'value': 'graph1'},
                {'label': 'Informática Aplicada', 'value': 'graph2'},
                    ],
            value='graph1',
            style={"width": "60%"}),
    

        dcc.Slider(0, 5,
            step=None,
            marks={
                0: 'Agosto',
                1: 'Setembro',
                2: 'Outubro',
                3: 'Novembro',
                4: 'Dezembro'
            },
            value=5,id='my-slider'),
     
        dbc.Container(
            dbc.Row(
                [dbc.Col(card_sales), dbc.Col(card_profit),
                dbc.Col(card_orders)],
            ),
            fluid=True,
        )

]),
 
    html.Div(children='''
        Disciplina: .
    '''),
 
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    dcc.Graph(
        id='graf-linha',
        figure=figL
    )
    
    
])
from dash.dependencies import Input, Output    



@app.callback(
    Output('example-graph', 'figure'),
    [Input(component_id='dropdown', component_property='value')]
)
def select_graph(value):
    if value == 'graph1':
        data1 = pd.read_csv('testeagrupamento.csv',sep=";")
        fig = px.area(data1,x='Semanas' ,y='Quantidade', color="Grupos", title="Acesso por dia da semana",color_discrete_sequence=px.colors.qualitative.Plotly)

        fig.update_layout(autosize=False,width=900,height=600)
        fig.update_layout(title={'text' : 'Comparar a Quantidade de Visualização dos Grupos no Ambiente ao Longo do Tempo', 'y':0.96,'x': 0.1
        })
        fig.update_xaxes(title = 'Períodos Mensais')
        fig.update_yaxes(title = 'Quantidade Visualização')
        return fig
    else:
        data1 = pd.read_csv('testeagrupamento2.csv',sep=";")
        fig1 = px.area(data1,x='Semanas' ,y='Quantidade', color="Grupos", title="Acesso por dia da semana",color_discrete_sequence=px.colors.qualitative.Plotly)

        fig1.update_layout(autosize=False,width=900,height=600)
        fig1.update_layout(title={'text' : 'Comparar a Quantidade de Visualização dos Grupos no Ambiente ao Longo do Tempo', 'y':0.96,'x': 0.1
        })
        fig1.update_xaxes(title = 'Períodos Mensais')
        fig1.update_yaxes(title = 'Quantidade Visualização')
        return fig1



#chamada web
if __name__ == '__main__':
    app.run(debug=True)
