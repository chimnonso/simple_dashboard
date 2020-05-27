# from project import app
from flask import render_template, Blueprint, redirect, url_for, request
from project import db
from project.data import Articles
from project.forms import AddArticleForm
from project.models import Article
from flask_login import login_required

articles_bp = Blueprint('articles', __name__, template_folder='templates/articles')


@articles_bp.route('/')
def articles():
   articles = Article.query.all()
   return render_template('articles.html', articles=articles)

@articles_bp.route('/<article_id>')
def article(article_id):
   # article_id = article_id
   article = Article.query.get(article_id)
   return render_template('article.html', article=article)

@articles_bp.route('/dashboard')
@login_required
def dashboard():
   articles = Article.query.all()
   # articles = Article.query.order_by(Article.id.desc())
   return render_template('dashboard.html', articles=articles)

@articles_bp.route('/add_article', methods=['GET','POST'])
def add_article():
   form = AddArticleForm()
   # print(form.errors)
   if form.validate_on_submit():
      print(form.title.data, form.body.data)
      article = Article(title=form.title.data, body=form.body.data)
      db.session.add(article)
      db.session.commit()
      return redirect(url_for('articles.dashboard'))
   return render_template('add_article.html', form=form)


