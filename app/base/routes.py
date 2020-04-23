from flask import Blueprint, render_template, request, redirect, url_for
from app.base.forms import LoginForm
from app.base.models import User
from flask_login import current_user, login_required, login_user, logout_user

blueprint = Blueprint(
    'base_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)

@blueprint.route('/')
def index():
    return render_template('index.html')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if 'login' in request.form:
        admin = User.query.filter_by(email=request.form['email']).first()
        if admin:
            if admin.check_password(request.form['password']):
                login_user(admin)
                return redirect(url_for('base_blueprint.index'))
            else:
                status = 'Неверный пароль'
        else:
            status = "Пользователь не найден"

        return render_template('login.html', form=form, status=status)
    if current_user.is_authenticated:
        redirect(url_for('base_blueprint.index'))
    return render_template('login.html', form=form, status='')


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('base_blueprint.login'))