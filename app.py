import string
import hashlib
from flask import Flask, render_template, Blueprint, jsonify, flash, request, redirect, url_for, session
from flask_ngrok import run_with_ngrok

from utils.nos_lat_long import nos as nos_lat_long
from utils.busca_amplitude import busca_amplitude
from utils.busca import busca
from utils.nos import nos

app = Flask(__name__)
# run_with_ngrok(app)

# ---------------------------------------
# Chave da Aplicação FLask
# ---------------------------------------

app.secret_key = 'sas'
sol = busca()
sol_amplitude = busca_amplitude()

# ---------------------------------------
# Verificar
# ---------------------------------------

@app.route('/', methods=['GET', 'POST'])
def index():
  data          = ""
  custo         = ""
  caminho_final = ""
  lat_long      = ""

  if request.method == 'POST':
    algoritmo       = request.form['algoritmo']

    if algoritmo == "amplitude" or algoritmo == "profundidade" or algoritmo == "profundidade_limitada" or algoritmo == "profundidade_limitada_3" or algoritmo == "profundidade_limitada_4" or algoritmo == "aprofundamento_iterativo":
      destino = request.form['destino_1']
      a  = request.form['origem_1']
      b = request.form['origem_2']
      origem = [a, b] 
    else:
      destino = request.form['destino']
      origem  = request.form['origem']

    # Ínicio da Verificação
    if destino == "":
      flash("Destino é obrigatório para a verificação", "warning")      

    if origem == "":
      flash("Origem é obrigatório para a verificação", "warning")      

    if algoritmo == "":
      flash("Algoritmo é obrigatório para a verificação", "warning")      
    # Final da Verificação

    # Se foi selecionado o método Custo Uniforme 
    if algoritmo == 'custo-uniforme':
      caminho    = []
      lat_long   = []
      data       = "custo-uniforme"
      caminho, custo = sol.custo_uniforme(origem,destino)
      caminho_final  = caminho[::-1]
      # Ínicio da obtenção do valor das coordenadas (latitude e longitude)
      for a in nos_lat_long:
        for b in caminho_final:
          if a['nome'] == b:
            lat_long.append(a)
      # Final da obtenção do valor das coordenadas (latitude e longitude)

    elif algoritmo == 'greedy': # Se foi selecionado o método Greedy 
      caminho      = []
      lat_long     = []
      data         = "greedy"
      caminho, custo = sol.greedy(origem,destino)
      caminho_final = caminho[::-1]
      # Ínicio da obtenção do valor das coordenadas (latitude e longitude)
      for a in nos_lat_long:
        for b in caminho_final:
          if a['nome'] == b:
            lat_long.append(a)
      # Final da obtenção do valor das coordenadas (latitude e longitude)

    elif algoritmo == 'a-estrela': # Se foi selecionado o método A estrela
      caminho   = []
      caminho_final = []
      lat_long  = []
      data      = "a-estrela"
      caminho, custo = sol.a_estrela(origem,destino)
      caminho_final = caminho[::-1]
      # Ínicio da obtenção do valor das coordenadas (latitude e longitude)
      for a in nos_lat_long:
        for b in caminho_final:
          if a['nome'] == b:
            lat_long.append(a)
      # Final da obtenção do valor das coordenadas (latitude e longitude)

    elif algoritmo == 'bidirecional': # Se foi selecionado o método bidirecional
      caminho   = []
      caminho_final = []
      lat_long  = []
      data      = "bidirecional"
      caminho_final = sol_amplitude.bidirecional(destino, origem)
      print("\n\n\nCaminho Final => ", caminho_final)
      # Ínicio da obtenção do valor das coordenadas (latitude e longitude)
      for a in nos_lat_long:
        for b in caminho_final:
          if a['nome'] == b:
            lat_long.append(a)
      # Final da obtenção do valor das coordenadas (latitude e longitude)

    elif algoritmo == 'amplitude': # Se foi selecionado o método Amplitude
      caminho   = []
      caminho_final = []
      lat_long  = []
      data      = "amplitude"
      caminho_final = sol_amplitude.amplitude(destino, origem)
      print("\n\n\nCaminho Final => ", caminho_final)
      # Ínicio da obtenção do valor das coordenadas (latitude e longitude)
      for a in nos_lat_long:
        for b in caminho_final:
          if a['nome'] == b:
            lat_long.append(a)
      # Final da obtenção do valor das coordenadas (latitude e longitude)


    elif algoritmo == 'profundidade': # Se foi selecionado o método profundidade
      caminho   = []
      caminho_final = []
      lat_long  = []
      data      = "profundidade"
      caminho_final = sol_amplitude.profundidade(destino,origem)
      print("\n\n\nCaminho Final => ", caminho_final)
      # Ínicio da obtenção do valor das coordenadas (latitude e longitude)
      for a in nos_lat_long:
        for b in caminho_final:
          if a['nome'] == b:
            lat_long.append(a)
      # Final da obtenção do valor das coordenadas (latitude e longitude)

    elif algoritmo == 'profundidade_limitada': # Se foi selecionado o método profundidade
      caminho   = []
      caminho_final = []
      lat_long  = []
      data      = "profundidade"
      caminho_final = sol_amplitude.prof_limitada(destino, origem, 5)
      print("\n\n\nCaminho Final => ", caminho_final)
      # Ínicio da obtenção do valor das coordenadas (latitude e longitude)
      for a in nos_lat_long:
        for b in caminho_final:
          if a['nome'] == b:
            lat_long.append(a)
      # Final da obtenção do valor das coordenadas (latitude e longitude)


    elif algoritmo == 'profundidade_limitada_3': # Se foi selecionado o método profundidade_limitada_3
      caminho   = []
      caminho_final = []
      lat_long  = []
      data      = "profundidade_limitada_3"
      caminho_final = sol_amplitude.profundidade_limitada( origem, destino,3)
      print("\n\n\nCaminho Final => ", caminho_final)
      # Ínicio da obtenção do valor das coordenadas (latitude e longitude)
      for a in nos_lat_long:
        for b in caminho_final:
          if a['nome'] == b:
            lat_long.append(a)
      # Final da obtenção do valor das coordenadas (latitude e longitude)

    elif algoritmo == 'profundidade_limitada_4': # Se foi selecionado o método profundidade_limitada_4
      caminho   = []
      caminho_final = []
      lat_long  = []
      data      = "profundidade_limitada_4"
      caminho_final = sol_amplitude.profundidade_limitada( origem, destino,4)
      print("\n\n\nCaminho Final => ", caminho_final)
      # Ínicio da obtenção do valor das coordenadas (latitude e longitude)
      for a in nos_lat_long:
        for b in caminho_final:
          if a['nome'] == b:
            lat_long.append(a)
      # Final da obtenção do valor das coordenadas (latitude e longitude)


    elif algoritmo == 'aprofundamento_iterativo': # Se foi selecionado o método aprofundamento_iterativo
      caminho   = []
      caminho_final = []
      lat_long  = []
      data      = "aprofundamento_iterativo"
      caminho_final = sol_amplitude.aprofundamento_iterativo(destino, origem, 10)
      print("\n\n\nCaminho Final => ", caminho_final)
      # Ínicio da obtenção do valor das coordenadas (latitude e longitude)
      for a in nos_lat_long:
        for b in caminho_final:
          if a['nome'] == b:
            lat_long.append(a)
      # Final da obtenção do valor das coordenadas (latitude e longitude)
  return render_template('index.jinja2', data=data, caminho=caminho_final, custo=custo, todo_caminho=lat_long, array_nos=nos)

# ---------------------------------------
# Tela de erro
# ---------------------------------------

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Ocorreu um erro na página ' + request.url,
        'status': 404
    }

    response = jsonify(message)
    response.status_code = 404
    return response

# ---------------------------------------
# Inicializando aplicação
# ---------------------------------------

if __name__ == '__main__':
  # app.run()
  app.run(host='0.0.0.0', debug=True, port=8080)