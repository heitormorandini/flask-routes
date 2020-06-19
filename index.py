from flask import Flask, render_template
app = Flask(__name__)

prices = [
  [1, 'Refrigerante', 4.50],
  [2, 'Pizza', 2.50],
  [3, 'Suco', 24.90],
  [4, 'Salgado', 5.50],
  [5, 'Lanche', 18.50]
]

@app.route('/')
def index():
  return render_template(
    'listagem.html',
    titulo='Tabela de preços',
    prices=prices
  )

@app.route('/info/<int:index>')
def info(index):
  item = prices[index]
  return render_template(
    'informacoes.html',
    titulo=item[1],
    nome=item[1],
    preco=item[2]
  )

if __name__ == '__main__':
  app.run()