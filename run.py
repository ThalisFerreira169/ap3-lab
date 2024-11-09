# Import do Flask e bibliotecas e iniciando a aplicação
from flask import Flask, render_template;
app = Flask(__name__);


# Rota Home
@app.route('/')
def home():
  return render_template('index.html');

# Inicializando a aplicação
if __name__ == '__main__':
  app.run(debug=True);