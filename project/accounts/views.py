# from project import app
from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from project.forms import SignUpForm, LoginForm
from project.models import User
from project import db
from flask_login import login_required, login_user, logout_user


accounts_bp = Blueprint('accounts', __name__, template_folder='templates/accounts')

from urllib.parse import urlparse, urljoin

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc



@accounts_bp.route('/logout')
@login_required
def logout():
   logout_user()
   flash("You have been logged out", "success")
   return redirect(url_for('index'))

@accounts_bp.route('/login', methods=['GET','POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
      user = User.query.filter_by(email=form.email.data).first()
      print(user)
      if user.check_password(form.password.data) and user is not None:
         login_user(user)
         flash('Logged Successfully', 'success')
         next = request.args.get('next')
         if not is_safe_url(next):
            return abort(400)
      return redirect(next or url_for('index'))
   return render_template('login.html', form=form)


@accounts_bp.route('/signup', methods=['GET', 'POST'])
def signup():
   form = SignUpForm()
   if form.validate_on_submit():
      user = User(email=form.email.data, username=form.username.data, password=form.password.data)
      db.session.add(user)
      db.session.commit()
      flash('Registration completed successfully', 'success')
      return redirect(url_for('accounts.login'))
   return render_template('signup.html', form=form)


