# Imports das bibliotecas do Flask e as defs do models.py
from flask import Blueprint, request, redirect, url_for, render_template, flash
from .models import insert_user, get_user_by_email

# Crio o módulo main para as rotas da aplicação
main_bp = Blueprint('main', __name__)

# Rota inicial
@main_bp.route('/')
def home():
  return render_template('home.html')

# Rota de Login com requisição GET ou POST usando a def do banco
@main_bp.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
        
    user = get_user_by_email(email)
    if user and user['password'] == password:
      flash('Login bem-sucedido!')
      return redirect(url_for('main.home'))
    else:
      flash('Email ou senha incorretos!')
      return redirect(url_for('main.login'))

  # Retornando o GET
  return render_template('login.html')

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
        
    if get_user_by_email(email):
      flash('Email já cadastrado!')
      return redirect(url_for('main.register'))
        
    insert_user(username, email, password)
    flash('Registrado com sucesso!')
    return redirect(url_for('main.login'))

  return render_template('register.html')
