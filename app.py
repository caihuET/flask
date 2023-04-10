import uuid

import wtf as wtf
from flask import Flask, render_template, request
from wtforms import StringField, PasswordField, SubmitField  # 类型
from flask_wtf import Form, FlaskForm
from wtforms.validators import DataRequired, EqualTo  # 验证数据不能为空，验证两次密码是否相同

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.config.update(SECRE_KEY=app.secret_key)


# 定义表单类型
class Register(FlaskForm):
    user_name = StringField(label="用户名", validators=[DataRequired("用户名不能为空")])
    password = PasswordField(label="密码", validators=[DataRequired("密码不能为空")])
    password2 = PasswordField(label="确认密码", validators=[DataRequired("密码不能为空"), EqualTo("password")])
    submit = SubmitField(label="注册")


@app.route("/register", methods=["GET", "POST"])
def register():
    # 创建表单对象,实例化
    form = Register()
    if request.method == "GET":
        return render_template("register.html", form=form)
    if request.method == "POST":
        password = form.password.data
        password2 = form.password2.data
        if password == password2:
            print(password)
            print(password2)
            return "注册成功!"
            # return render_template("register.html", form=form)
        else:
            return "两次输入的密码不一致"
        # return render_template("register.html", form=form)


if __name__ == '__main__':
    app.run()
