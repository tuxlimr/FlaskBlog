from flask import Flask, render_template, flash, redirect, url_for
app = Flask(__name__)
from forms import RegisterForm,LoginForm
app.config['SECRET_KEY'] = 'affa93da518fea59d1863faf04ecbe1a'


post = [
    {
        'name': "Ajay Sharma",
        'class': "Technical Program Manager"
    },
    {
        'name': "Gitu Sharma",
        'class': "Technical Program Manager"
    }
]


@app.route('/')
def hello():
    return render_template('hello.html', post=post)

@app.route('/about/')
def about():
    return render_template('about.html', title="About")


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('hello'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@hello.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('hello'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
