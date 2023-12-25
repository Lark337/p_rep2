from flask import Flask,request, render_template, redirect,url_for , make_response

app = Flask(__name__)

def cookie(key:str,value:str):
    res = make_response()
    res.set_cookie(key, value)
    return res

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        login = request.form.get("username")
        email = request.form.get("email")
        response = make_response(redirect(url_for("success", name=login)))
        response.set_cookie("login", login)
        response.set_cookie("email", email)
        return response
    else:
        return render_template("login.html")


@app.route("/success/<name>")
def success(name: str):
    return render_template("success.html", name1 = request.cookies.get("login"))


@app.route("/exit/")
def exit():
    res = make_response(redirect("/"))
    res.set_cookie("login", '', max_age=0)
    res.set_cookie("email", '', max_age=0)
    return res


if __name__ == "__main__":
    app.run(debug=True)