import plotly.graph_objects as go

month = ['16 de Fevereiro', '23 de Fevereiro', '1 de Março',
         '8 de Março', '15 de Março', '22 de Março',
         '29 de Março', '5 de Abril', '12 de Abril',
         '19 de Abril', '26 de Abril', '3 de Maio',
         '10 de Maio', '17 de Maio', '24 de Maio',
         '31 de Maio', '7 de Junho', '14 de Junho']
São_Paulo = [+44, +31, +69, +46, +6, -48, -73, -75, -81,
             -81, -82, -82, -82, -81, -79, -76, -73, -70]
Brasília = [+46, +27, +55, +46, +2, -45, -71, -69, -79,
            -76, -76, -75, -76, -80, -77, -74, -70, -71]
Rio_de_Janeiro = [+33, +23, +29, +16, -8, -59, -75, -76, -81,
                  -80, -83, -84, -84, -85, -84, -81, -77, -78]
Belo_Horizonte = [+37, +31, +46, +26, -2, -42, -72, -72, -77,
                  -74, -75, -75, -73, -74, -73, -70, -65, -69]
Goiania = [+58, +47, +67, +44, +13, -34, -63, -62, -74,
           -69, -74, -73, -71, -77, -74, -65, -62, -68]
florianopolis = [+37, +35, +43, +28, +1, -50, -66, -68, -69,
                 -67, -69, -68, -66, -68, -64, -56, -48, -48]
media = [+30, -1, +59, -11, -23, -69, -70, -74, -78,
         -77, -80, -79, -80, -78, -74, -79, -76, -76]


fig = go.Figure()
fig.add_trace(go.Scatter(x=month, y=São_Paulo, name='São Paulo, SP',
                         line=dict(color='royalblue', width=5)))
fig.add_trace(go.Scatter(x=month, y=Rio_de_Janeiro, name='Rio de Janeiro, RJ',
                         line=dict(color='firebrick', width=5)))
fig.add_trace(go.Scatter(x=month, y=Belo_Horizonte, name='Belo Horizonte, MG',
                         line=dict(color='yellow', width=5)))
fig.add_trace(go.Scatter(x=month, y=Brasília, name='Brasília, DF',
                         line=dict(color='green', width=5)))
fig.add_trace(go.Scatter(x=month, y=Goiania, name='Goiânia, GO',
                         line=dict(color='orange', width=5)))
fig.add_trace(go.Scatter(x=month, y=florianopolis, name='Florianópolis, SC',
                         line=dict(color='purple', width=5)))
fig.add_trace(go.Scatter(x=month, y=media, name='Brasil',
                         line=dict(color='black', width=5)))

fig.update_layout(title='Comparação semanal dos principais destinos brasileiros',
                  xaxis_title='Semanas',
                  yaxis_title='Mudanças no interesse pelas buscas de voos (%)')

fig.show()
