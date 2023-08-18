# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.



#from tkinter.tix import InputOnly
from dash import Dash, html, dcc, State, dash_table
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
#from flask import Flask
from dash.dependencies import Input, Output




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',dbc.themes.SPACELAB,dbc.icons.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets)
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

######              dataframe               ##############
dataA1 = pd.read_csv('disc57GArea.csv',sep=";")
dataL1 = pd.read_csv('disc57GLinha.csv',sep=";")
dataMCA1 = pd.read_csv('disc57MCAtividade.csv',sep=";")
dataMCF1 = pd.read_csv('disc57MCForum.csv',sep=";")
dataD1 = pd.read_csv('disc57GDispersao.csv',sep=";")
dataB1 = pd.read_csv('disc57GBarra.csv',sep=";")
dataalunos1 = pd.read_csv('disc57Alunos.csv',sep=";")
#
dataA2 = pd.read_csv('disc64GArea.csv',sep=";")
dataL2 = pd.read_csv('disc64GLinha.csv',sep=";")
dataMCA2 = pd.read_csv('disc64MCAtividade.csv',sep=";")
dataMCF2 = pd.read_csv('disc64MCForum.csv',sep=";")
dataD2 = pd.read_csv('disc64GDispersao.csv',sep=";")
dataB2 = pd.read_csv('disc64GBarra.csv',sep=";")
dataalunos2 = pd.read_csv('disc64Alunos.csv',sep=";")




#####           plotagem             #########
#linha
figL = px.line(dataL1, x="Dias da Semana", y="Quantidade", color='Grupos',color_discrete_sequence=px.colors.qualitative.Plotly)
figL.update_xaxes(title = 'Períodos Mensais')
figL.update_yaxes(title = 'Quantidade Respostas')
figL.update_layout(autosize=True)
figL.update_layout(font = dict(size=10) ,title={
    'text' : 'Tendência de Respostas no Fórum ao Longo do Tempo'})
figL.update_traces(opacity=.6)

#area

fig = px.area(dataA1,x='Semanas' ,y='Quantidade', color="Grupos", title="Acesso por dia da semana",color_discrete_sequence=px.colors.qualitative.Plotly)
fig.update_layout(autosize=True)
fig.update_layout(font = dict(size=10),title={
    'text' : 'Comparar a Quantidade de Visualização dos Grupos no Ambiente ao Longo do Tempo'})
fig.update_xaxes(title = 'Períodos Mensais')
fig.update_yaxes(title = 'Quantidade Visualização')

#mapa de calor
heatmap_data = pd.pivot_table(dataMCA1, values='Quantidade',
                              index='Grupos',
                              columns='Semanas')


figMCA = px.imshow(heatmap_data,
                labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
'01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
'01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
'01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
'01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
               )
figMCA.update_layout(
    title='Quantidade de Acesso nas Atividades ao Longo do Tempo',
    xaxis_nticks=36)
figMCA.update_xaxes(title = 'Períodos Mensais')

#Mapa de calor forum
heatmap_data = pd.pivot_table(dataMCF1, values='Quantidade',
                              index='Grupos',
                              columns='Semanas')



figMCF = px.imshow(heatmap_data,
                labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
               x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
'01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
'01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
'01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
'01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
               )
figMCF.update_layout(
    title='Quantidade de Acesso ao Fórum ao Longo dos Meses',
    xaxis_nticks=36)
figMCF.update_xaxes(title = 'Períodos Mensais')



#Dispersão
figD = px.scatter(dataD1, x = "Nota", y = "Quantidade de Alunos", color="Grupos", size_max = 80, facet_col = 'Tipo de Avaliação',
                 color_discrete_sequence=px.colors.qualitative.Plotly)
figD.update_traces(marker = dict(size = 10,line = dict(width = 2)),selector = dict(mode = 'markers'))
figD.update_xaxes(title = 'Notas')
figD.update_layout(title={'text':'Distribuição da Quantidade de Alunos por Notas nas Avaliações'}
)
figD.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

#barra
figB = px.histogram(dataB1, x='Média', y="Quantidade",
             color='Grupos', barmode='group')

figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
figB.update_layout(autosize=True)
figB.update_layout(title={
    'text' : 'Composição de Alunos por Notas na Avaliação Checklist'})
figB.update_xaxes(title = 'Intervalo de Notas')
figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
figB.update_yaxes(title = 'Quantidade Alunos')





summary = {"Alunos": "100K", "Mensagens": "5K",
           "Acessos": "6K"}
def make_card(title, amount):
    return dbc.Card(
        [
            dbc.CardHeader(html.H2(title)),
            dbc.CardBody(html.H3(amount, id=title)),
        ],
        className="text-center shadow",
    )









#####                    HTML                     ##########
app.layout = html.Div(children=[
    html.H1(children='Engajamento em Ambientes EaD'), 
    html.Hr(),



    html.Div(
        [
        html.Div([
            html.Label(['Escolha a Disciplina:'],style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'Metodologia Científica', 'value': 'graph1'},
                    {'label': 'Informática Aplicada', 'value': 'graph2'},
                        ],
                value='graph1',
                style={"width": "100%"})],className='six columns'),

        html.Div([
            html.Label(['Escolha o Grupo:'],style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='demo_dropdown_grupo',
                options=[
                    {'label': 'Todos', 'value': 'Todos'},
                    {'label': 'Grupo 0', 'value': 'Grupo 0'},
                    {'label': 'Grupo 1', 'value': 'Grupo 1'},
                        ],
                value='Todos',
                style={"width": "100%"})],className='six columns')
    ],className='row'),

    html.Hr(),



    html.Label(['Informações Gerais:'],style={'font-weight': 'bold'}),
    
    html.Div(
        [

        html.Div([
            dbc.Container(
                dbc.Row([dbc.Col(make_card(k, v)) for k, v in summary.items()],
                        className="my-4"),
                fluid=True,
            style={"width": "90%"})],className='six columns'),

        html.Div([
                dash_table.DataTable(
                    dataalunos1.to_dict("records"),
                    [{"name": i, "id": i} for i in dataalunos1.columns],
                    id="table_cb",
                    #page_size=20,
                    style_table={'height': '200px', "width": "90%",'overflowY': 'auto'}
                    #style_cell_conditional=[
                    #    {'if': {'column_id': 'Alunos'},
                    #    'width': '130px'},
                    #    {'if': {'column_id': 'Grupo'},
                    #    'width': '130px'},

                )],className='six columns'),            

    ],className='row'),
    html.Hr(),



    html.Div(
        [
        html.Div([
            dcc.Graph(
                id='example-graph',
                figure=fig, 
                style={"width": "100%"})],className='six columns'),

        html.Div([
            dcc.Graph(
                id='graf-linha',
                figure=figL,
                style={"width": "100%"})],className='six columns')
    ],className='row'),
 

    html.Div(
        [
        html.Div([
            dcc.Graph(
                id='graf-MCF',
                figure=figMCF,
                style={"width": "100%"})],className='six columns'),

        html.Div([
            dcc.Graph(
                id='graf-MCA',
                figure=figMCA,
                style={"width": "100%"})],className='six columns'),

    ],className='row'),

    html.Div(
        [
        html.Div([
            dcc.Graph(
                id='graf-Dispersao',
                figure=figD,
                style={"width": "100%"})],className='six columns'),

        html.Div([
            dcc.Graph(
                id='graf-Barra',
                figure=figB,
                style={"width": "100%"})],className='six columns'),

    ],className='row'),
    
    
    
])


######          chamadas            ############


@app.callback([

    Output('example-graph', 'figure'),
    Output('graf-linha', 'figure'),
    Output('graf-MCA', 'figure'),
    Output('graf-Dispersao', 'figure'),
    Output('graf-Barra', 'figure'),
    Output('graf-MCF', 'figure'),
    Output("table_cb", "data"),

], [Input('dropdown', 'value'), Input("demo_dropdown_grupo", "value")])




#######             funçoes de atualizações         #############

#
#def update_table(value, valueg):
#    dff = dataalunos1.copy()
#    if str(value) == "Grupo 0":
#        dff = dff[dff["Grupo"] == "Grupo 0"]
#    elif str(value) == "Grupo 1":
#        dff = dff[dff["Grupo"] == "Grupo 1"]
#    elif str(value) == "Todos":
#        pass
#    return dff.to_dict("records")



def multi_output(input_dropdown,input_demo_dropdown_grupo):
    if input_dropdown == 'graph1' and input_demo_dropdown_grupo == 'Todos':
        
        #data1 = pd.read_csv('testeagrupamento.csv',sep=";")
        fig = px.area(dataA1,x='Semanas' ,y='Quantidade', color="Grupos", title="Acesso por dia da semana",color_discrete_sequence=px.colors.qualitative.Plotly)

        fig.update_layout(autosize=True)
        fig.update_layout(font = dict(size=10) , title={'text' : 'Comparar a Quantidade de Visualização dos Grupos no Ambiente ao Longo do Tempo'})
        fig.update_xaxes(title = 'Períodos Mensais')
        fig.update_yaxes(title = 'Quantidade Visualização')
        #
        figL = px.line(dataL1, x="Dias da Semana", y="Quantidade", color='Grupos',color_discrete_sequence=px.colors.qualitative.Plotly)
        figL.update_xaxes(title = 'Períodos Mensais')
        figL.update_yaxes(title = 'Quantidade Respostas')
        figL.update_layout(autosize=True)
        figL.update_layout(font = dict(size=10),title={'text' : 'Tendência de Respostas no Fórum ao Longo do Tempo'})
        #
        heatmap_data = pd.pivot_table(dataMCA1, values='Quantidade',
                                    index='Grupos',
                                    columns='Semanas')


        figMCA = px.imshow(heatmap_data,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                        x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
                    )
        figMCA.update_layout(font = dict(size=10) ,
            title='Quantidade de Acesso nas Atividades ao Longo do Tempo')
        figMCA.update_xaxes(title = 'Períodos Mensais')      
        #
        figD = px.scatter(dataD1, x = "Nota", y = "Quantidade de Alunos", color="Grupos", size_max = 80, facet_col = 'Tipo de Avaliação',
                        color_discrete_sequence=px.colors.qualitative.Plotly)
        figD.update_traces(marker = dict(size = 10,line = dict(width = 2)),selector = dict(mode = 'markers'))
        figD.update_xaxes(title = 'Notas')
        figD.update_layout(font = dict(size=10) ,title={'text':'Distribuição da Quantidade de Alunos por Notas nas Avaliações'}
        )
        figD.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))  
        #
        figB = px.histogram(dataB1, x='Média', y="Quantidade",
                    color='Grupos', barmode='group',
                    height=400)

        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_layout(autosize=True)
        figB.update_layout(font = dict(size=10) ,title={
            'text' : 'Composição de Alunos por Notas na Avaliação Checklist',

        })
        figB.update_xaxes(title = 'Intervalo de Notas')
        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_yaxes(title = 'Quantidade Alunos')

        #
        heatmap_data = pd.pivot_table(dataMCF1, values='Quantidade',
                              index='Grupos',
                              columns='Semanas')
        
        figMCF = px.imshow(heatmap_data,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                    x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
                    )
        figMCF.update_layout(font = dict(size=10),
            title='Quantidade de Acesso ao Fórum ao Longo dos Meses')
        figMCF.update_xaxes(title = 'Períodos Mensais')
        
        return fig,figL,figMCA,figD,figB,figMCF, dataalunos1.to_dict("records")
    
    ########
    elif input_dropdown == 'graph1' and input_demo_dropdown_grupo == 'Grupo 0':
        #data1 = pd.read_csv('testeagrupamento.csv',sep=";")
        fig = px.area(dataA1[dataA1["Grupos"]== 'Grupo 0'],x='Semanas' ,y='Quantidade', title="Acesso por dia da semana",color_discrete_sequence=px.colors.qualitative.Plotly)

        fig.update_layout(autosize=True)
        fig.update_layout(font = dict(size=10) ,title={'text' : 'Comparar a Quantidade de Visualização dos Grupos no Ambiente ao Longo do Tempo'})
        fig.update_xaxes(title = 'Períodos Mensais')
        fig.update_yaxes(title = 'Quantidade Visualização')
        #
        figL = px.line(dataL1[dataL1["Grupos"]== 'Grupo 0'], x="Dias da Semana", y="Quantidade",color_discrete_sequence=px.colors.qualitative.Plotly)
        figL.update_xaxes(title = 'Períodos Mensais')
        figL.update_yaxes(title = 'Quantidade Respostas')
        figL.update_layout(autosize=True)
        figL.update_layout(font = dict(size=10) ,title={
                'text' : 'Tendência de Respostas no Fórum ao Longo do Tempo'})
        #
        heatmap_data = pd.pivot_table(dataMCA1[dataMCA1["Grupos"]== 'Grupo 0'], values='Quantidade',
                                    columns='Semanas')


        figMCA = px.imshow(heatmap_data,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                        x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
                    )
        figMCA.update_layout(font = dict(size=10) ,
            title='Quantidade de Acesso nas Atividades ao Longo do Tempo')
        figMCA.update_xaxes(title = 'Períodos Mensais')      
        #
        figD = px.scatter(dataD1[dataD1["Grupos"]== 'Grupo 0'], x = "Nota", y = "Quantidade de Alunos", size_max = 80, facet_col = 'Tipo de Avaliação',
                        color_discrete_sequence=px.colors.qualitative.Plotly)
        figD.update_traces(marker = dict(size = 10,line = dict(width = 2)),selector = dict(mode = 'markers'))
        figD.update_xaxes(title = 'Notas')
        figD.update_layout(font = dict(size=10) ,title={'text':'Distribuição da Quantidade de Alunos por Notas nas Avaliações'})
        figD.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))  
        #
        figB = px.histogram(dataB1[dataB1["Grupos"]== 'Grupo 0'], x='Média', y="Quantidade", barmode='group')

        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_layout(autosize=True)
        figB.update_layout(font = dict(size=10) ,title={
            'text' : 'Composição de Alunos por Notas na Avaliação Checklist'
        })
        figB.update_xaxes(title = 'Intervalo de Notas')
        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_yaxes(title = 'Quantidade Alunos')

        #
        heatmap_data = pd.pivot_table(dataMCF1[dataMCF1["Grupos"]== 'Grupo 0'], values='Quantidade',
                              columns='Semanas')
        
        figMCF = px.imshow(heatmap_data,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                    x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
                    )
        figMCF.update_layout(font = dict(size=10) ,
            title='Quantidade de Acesso ao Fórum ao Longo dos Meses')
        figMCF.update_xaxes(title = 'Períodos Mensais')
        
        return fig,figL,figMCA,figD,figB,figMCF, dataalunos1[dataalunos1["Grupo"]== 'Grupo 0'].to_dict("records")
    
    #########
    elif input_dropdown == 'graph1' and input_demo_dropdown_grupo == 'Grupo 1':
        #data1 = pd.read_csv('testeagrupamento.csv',sep=";")
        fig = px.area(dataA1[dataA1["Grupos"]== 'Grupo 1'],x='Semanas' ,y='Quantidade', title="Acesso por dia da semana",color_discrete_sequence=px.colors.qualitative.Set1)

        fig.update_layout(autosize=True)
        fig.update_layout(font = dict(size=10) ,title={'text' : 'Comparar a Quantidade de Visualização dos Grupos no Ambiente ao Longo do Tempo'})
        fig.update_xaxes(title = 'Períodos Mensais')
        fig.update_yaxes(title = 'Quantidade Visualização')
        #
        figL = px.line(dataL1[dataL1["Grupos"]== 'Grupo 1'], x="Dias da Semana", y="Quantidade",color_discrete_sequence=px.colors.qualitative.Set1)
        figL.update_xaxes(title = 'Períodos Mensais')
        figL.update_yaxes(title = 'Quantidade Respostas')
        figL.update_layout(autosize=True)
        figL.update_layout(font = dict(size=10) ,title={
                'text' : 'Tendência de Respostas no Fórum ao Longo do Tempo'})
        #
        heatmap_data = pd.pivot_table(dataMCA1[dataMCA1["Grupos"]== 'Grupo 1'], values='Quantidade',
                                    columns='Semanas')


        figMCA = px.imshow(heatmap_data,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                        x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
                    )
        figMCA.update_layout(font = dict(size=10) ,
            title='Quantidade de Acesso nas Atividades ao Longo do Tempo')
        figMCA.update_xaxes(title = 'Períodos Mensais')      
        #
        figD = px.scatter(dataD1[dataD1["Grupos"]== 'Grupo 1'], x = "Nota", y = "Quantidade de Alunos", size_max = 80, facet_col = 'Tipo de Avaliação',
                        color_discrete_sequence=px.colors.qualitative.Set1)
        figD.update_traces(marker = dict(size = 10,line = dict(width = 2)),selector = dict(mode = 'markers'))
        figD.update_xaxes(title = 'Notas')
        figD.update_layout(font = dict(size=10) ,title={'text':'Distribuição da Quantidade de Alunos por Notas nas Avaliações'})
        figD.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))  
        #
        figB = px.histogram(dataB1[dataB1["Grupos"]== 'Grupo 1'], x='Média', y="Quantidade", barmode='group', color_discrete_sequence=px.colors.qualitative.Set1)

        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_layout(autosize=True)
        figB.update_layout(font = dict(size=10) ,title={
            'text' : 'Composição de Alunos por Notas na Avaliação Checklist'
        })
        figB.update_xaxes(title = 'Intervalo de Notas')
        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_yaxes(title = 'Quantidade Alunos')

        #
        heatmap_data = pd.pivot_table(dataMCF1[dataMCF1["Grupos"]== 'Grupo 1'], values='Quantidade',
                              columns='Semanas')
        
        figMCF = px.imshow(heatmap_data,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                    x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
                    )
        figMCF.update_layout(font = dict(size=10) ,title='Quantidade de Acesso ao Fórum ao Longo dos Meses')
        figMCF.update_xaxes(title = 'Períodos Mensais')
        
        
        return fig,figL,figMCA,figD,figB,figMCF, dataalunos1[dataalunos1["Grupo"]== 'Grupo 1'].to_dict("records")

    ######
    elif input_dropdown == 'graph2' and input_demo_dropdown_grupo == 'Grupo 1':
        #data1 = pd.read_csv('testeagrupamento2.csv',sep=";")
        fig1 = px.area(dataA2[dataA2["Grupos"]== 'Grupo 1'],x='Semanas' ,y='Quantidade', color="Grupos", title="Acesso por dia da semana",color_discrete_sequence=px.colors.qualitative.Set1)

        fig1.update_layout(autosize=True)
        fig1.update_layout(font = dict(size=10) ,title={'text' : 'Comparar a Quantidade de Visualização dos Grupos no Ambiente ao Longo do Tempo'})
        fig1.update_xaxes(title = 'Períodos Mensais')
        fig1.update_yaxes(title = 'Quantidade Visualização')
        #
        figL = px.line(dataL2[dataL2["Grupos"]== 'Grupo 1'], x="Dias da Semana", y="Quantidade", color='Grupos',color_discrete_sequence=px.colors.qualitative.Set1)
        figL.update_xaxes(title = 'Períodos Mensais')
        figL.update_yaxes(title = 'Quantidade Respostas')
        figL.update_layout(autosize=True)
        figL.update_layout(font = dict(size=10) ,title={
                'text' : 'Tendência de Respostas no Fórum ao Longo do Tempo'
        })
        #
        heatmap_data = pd.pivot_table(dataMCA2[dataMCA2["Grupos"]== 'Grupo 1'], values='Quantidade',
                                    index='Grupos',
                                    columns='Semanas')


        figMCA = px.imshow(heatmap_data,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                        x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
                    )
        figMCA.update_layout(font = dict(size=10) , title='Quantidade de Acesso nas Atividades ao Longo do Tempo')
        figMCA.update_xaxes(title = 'Períodos Mensais')   
        #
        figD = px.scatter(dataD2[dataD2["Grupos"]== 'Grupo 1'], x = "Nota", y = "Quantidade de Alunos", color="Grupos", size_max = 80, facet_col = 'Tipo de Avaliação',
                        color_discrete_sequence=px.colors.qualitative.Set1)
        figD.update_traces(marker = dict(size = 10,line = dict(width = 2)),selector = dict(mode = 'markers'))
        figD.update_xaxes(title = 'Notas')
        figD.update_layout(font = dict(size=10) ,title={'text':'Distribuição da Quantidade de Alunos por Notas nas Avaliações'}
        )
        figD.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))     
        #
        figB = px.histogram(dataB2[dataB2["Grupos"]== 'Grupo 1'], x='Média', y="Quantidade",
                    color='Grupos', barmode='group', color_discrete_sequence=px.colors.qualitative.Set1)

        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_layout(autosize=True)
        figB.update_layout(font = dict(size=10) ,title={
            'text' : 'Composição de Alunos por Notas na Avaliação Checklist'
        })
        figB.update_xaxes(title = 'Intervalo de Notas')
        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_yaxes(title = 'Quantidade Alunos')
        #
        heatmap_data = pd.pivot_table(dataMCF2[dataMCF2["Grupos"]== 'Grupo 1'], values='Quantidade',
                              index='Grupos',
                              columns='Semanas')
        
        figMCF = px.imshow(heatmap_data,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                    x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
                    )
        figMCF.update_layout(font = dict(size=10) ,title='Quantidade de Acesso ao Fórum ao Longo dos Meses')
        figMCF.update_xaxes(title = 'Períodos Mensais')
        
        return fig1,figL,figMCA,figD,figB,figMCF, dataalunos2[dataalunos2["Grupo"]== 'Grupo 1'].to_dict("records")
    #############
    elif input_dropdown == 'graph2' and input_demo_dropdown_grupo == 'Grupo 0':
        #data1 = pd.read_csv('testeagrupamento2.csv',sep=";")
        fig1 = px.area(dataA2[dataA2["Grupos"]== 'Grupo 0'],x='Semanas' ,y='Quantidade', color="Grupos", title="Acesso por dia da semana",color_discrete_sequence=px.colors.qualitative.Plotly)

        fig1.update_layout(autosize=True)
        fig1.update_layout(title={'text' : 'Comparar a Quantidade de Visualização dos Grupos no Ambiente ao Longo do Tempo', 'y':0.96,'x': 0.1
        })
        fig1.update_xaxes(title = 'Períodos Mensais')
        fig1.update_yaxes(title = 'Quantidade Visualização')
        #
        figL = px.line(dataL2[dataL2["Grupos"]== 'Grupo 0'], x="Dias da Semana", y="Quantidade", color='Grupos',color_discrete_sequence=px.colors.qualitative.Plotly)
        figL.update_xaxes(title = 'Períodos Mensais')
        figL.update_yaxes(title = 'Quantidade Respostas')
        figL.update_layout(autosize=True)
        figL.update_layout(font = dict(size=10) ,title={
                'text' : 'Tendência de Respostas no Fórum ao Longo do Tempo'
        })
        #
        heatmap_data = pd.pivot_table(dataMCA2[dataMCA2["Grupos"]== 'Grupo 0'], values='Quantidade',
                                    index='Grupos',
                                    columns='Semanas')


        figMCA = px.imshow(heatmap_data,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                        x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
                    )
        figMCA.update_layout(font = dict(size=10) ,title='Quantidade de Acesso nas Atividades ao Longo do Tempo')
        figMCA.update_xaxes(title = 'Períodos Mensais')   
        #
        figD = px.scatter(dataD2[dataD2["Grupos"]== 'Grupo 0'], x = "Nota", y = "Quantidade de Alunos", color="Grupos", size_max = 80, facet_col = 'Tipo de Avaliação',
                        color_discrete_sequence=px.colors.qualitative.Plotly)
        figD.update_traces(marker = dict(size = 10,line = dict(width = 2)),selector = dict(mode = 'markers'))
        figD.update_xaxes(title = 'Notas')
        figD.update_layout(font = dict(size=10) ,title={'text':'Distribuição da Quantidade de Alunos por Notas nas Avaliações'})
        figD.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))     
        #
        figB = px.histogram(dataB2[dataB2["Grupos"]== 'Grupo 0'], x='Média', y="Quantidade",
                    color='Grupos', barmode='group',
                    height=400)

        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_layout(autosize=True)
        figB.update_layout(font = dict(size=10) ,title={
            'text' : 'Composição de Alunos por Notas na Avaliação Checklist'
        })
        figB.update_xaxes(title = 'Intervalo de Notas')
        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_yaxes(title = 'Quantidade Alunos')
        #
        heatmap_data = pd.pivot_table(dataMCF2[dataMCF2["Grupos"]== 'Grupo 0'], values='Quantidade',
                              index='Grupos',
                              columns='Semanas')
        
        figMCF = px.imshow(heatmap_data,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                    x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
                    )
        figMCF.update_layout(font = dict(size=10) ,title='Quantidade de Acesso ao Fórum ao Longo dos Meses')
        figMCF.update_xaxes(title = 'Períodos Mensais')
        
        return fig1,figL,figMCA,figD,figB,figMCF, dataalunos2[dataalunos2["Grupo"]== 'Grupo 0'].to_dict("records")
    ############
    elif input_dropdown == 'graph2' and input_demo_dropdown_grupo == 'Todos':
        #data1 = pd.read_csv('testeagrupamento2.csv',sep=";")
        fig1 = px.area(dataA2,x='Semanas' ,y='Quantidade', color="Grupos", title="Acesso por dia da semana",color_discrete_sequence=px.colors.qualitative.Plotly)

        fig1.update_layout(autosize=True)
        fig1.update_layout(title={'text' : 'Comparar a Quantidade de Visualização dos Grupos no Ambiente ao Longo do Tempo', 'y':0.96,'x': 0.1
        })
        fig1.update_xaxes(title = 'Períodos Mensais')
        fig1.update_yaxes(title = 'Quantidade Visualização')
        #
        figL = px.line(dataL2, x="Dias da Semana", y="Quantidade", color='Grupos',color_discrete_sequence=px.colors.qualitative.Plotly)
        figL.update_xaxes(title = 'Períodos Mensais')
        figL.update_yaxes(title = 'Quantidade Respostas')
        figL.update_layout(autosize=True)
        figL.update_layout(font = dict(size=10) ,title={
                'text' : 'Tendência de Respostas no Fórum ao Longo do Tempo'
        })
        #
        heatmap_data = pd.pivot_table(dataMCA2, values='Quantidade',
                                    index='Grupos',
                                    columns='Semanas')


        figMCA = px.imshow(heatmap_data,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                        x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
                    )
        figMCA.update_layout(
            title='Quantidade de Acesso nas Atividades ao Longo do Tempo',
            xaxis_nticks=36)
        figMCA.update_xaxes(title = 'Períodos Mensais')   
        #
        figD = px.scatter(dataD2, x = "Nota", y = "Quantidade de Alunos", color="Grupos", size_max = 80, facet_col = 'Tipo de Avaliação',
                        color_discrete_sequence=px.colors.qualitative.Plotly)
        figD.update_traces(marker = dict(size = 10,line = dict(width = 2)),selector = dict(mode = 'markers'))
        figD.update_xaxes(title = 'Notas')
        figD.update_layout(font = dict(size=10) ,title={'text':'Distribuição da Quantidade de Alunos por Notas nas Avaliações'}
        )
        figD.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))     
        #
        figB = px.histogram(dataB2, x='Média', y="Quantidade",
                    color='Grupos', barmode='group')

        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_layout(autosize=False,width=900,height=600)
        figB.update_layout(font = dict(size=10) ,title={
            'text' : 'Composição de Alunos por Notas na Avaliação Checklist'
        })
        figB.update_xaxes(title = 'Intervalo de Notas')
        figB.update_xaxes(categoryorder='array', categoryarray= ['0-20', '20-40', '40-60','60-80', '80-100'])
        figB.update_yaxes(title = 'Quantidade Alunos')
        #
        heatmap_data = pd.pivot_table(dataMCF2, values='Quantidade',
                              index='Grupos',
                              columns='Semanas')
        
        figMCF = px.imshow(heatmap_data,
                        labels=dict(x="Semanas", y="Grupos", color="Quantidade"),
                    x=[ '01-07 Agosto', '08-15 Agosto', '16-24 Agosto','25-31 Agosto',
        '01-07 Setembro', '08-15 Setembro', '16-24 Setembro','25-30 Setembro',
        '01-07 Outubro', '08-15 Outubro', '16-24 Outubro','25-31 Outubro',
        '01-07 Novembro', '08-15 Novembro', '16-24 Novembro','25-30 Novembro',
        '01-07 Dezembro', '08-15 Dezembro', '16-24 Dezembro','25-31 Dezembro'],text_auto=True,aspect="auto"
                    )
        figMCF.update_layout(font = dict(size=10) ,
            title='Quantidade de Acesso ao Fórum ao Longo dos Meses')
        figMCF.update_xaxes(title = 'Períodos Mensais')
        
        return fig1,figL,figMCA,figD,figB,figMCF, dataalunos2.to_dict("records")
    else:
        pass
    


#chamada web
if __name__ == '__main__':
    app.run(debug=True)
