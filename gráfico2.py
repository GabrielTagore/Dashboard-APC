import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__)

df = pd.read_csv('Gráfico2(01.11).csv', encoding='UTF-8', sep=';')


app.layout = html.Div([
    html.Div([
        html.H1(
            children='As tendências de buscas de viagens durante a pandemia do COVID19'),
        html.Label(['Escolha as cidades para comparar:'],
                   style={'font-weight': 'bold'}),
        dcc.Dropdown(id='cidades',
                     options=[{'label': x, 'value': x}
                              for x in df['CIDADE'].unique()],
                     value=['Brasil'],
                     multi=True,
                     disabled=False,
                     clearable=False,
                     searchable=True,
                     placeholder='Escolha a cidade...'),
    ]),
    html.Div([dcc.Graph(id='grafico')]),
])


@ app.callback(
    Output(component_id='grafico', component_property='figure'),
    [Input(component_id='cidades', component_property='value')]
)
def update_graph(cidades):
    dff = df.loc[df['CIDADE'].isin(cidades)]
    fig = px.line(data_frame=dff, x='DIA', y='PCTG',
                  color='CIDADE')
    fig.update_layout(title={'text': 'Comparação semanal dos principais destinos brasileiros:',
                             'font': {'size': 20}, 'x': 0.5, 'xanchor': 'center'},
                      xaxis_title='<b>Semanas de 2020<b>',
                      yaxis_title='<b>Mudanças no interesse pelas buscas de voos (%)<b>')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
