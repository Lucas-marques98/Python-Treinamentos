import PySimpleGUI as sg

layout = [
  [sg.Text('usuario')], 
  [sg.Input(key='usuario')],
  [sg.Text('senha')],
  [sg.Input('senha')],
  [sg.Button('login')],
  [sg.Text('',key='mensagem')]
]

window = sg.Window('login',layout=layout)

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break
  elif event == 'login':
    senha_correta = '123456'
    usuario_correto = 'Lucas'
    usuario = values['usuario']
    senha = values['senha']
    if senha == senha_correta and usuario == usuario_correto:
      window['mensagem'].update('Login feito com sucesso')
    else:
      window['mensagem'].update('Senha ou usuário incorreto')

