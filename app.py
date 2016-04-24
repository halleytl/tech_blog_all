from flask import Flask, render_template, redirect
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect("/blog/meituan")

@app.route('/menu')
def menu():
    return ["meituan", "taobao"]

@app.route('/blog/<blog_type>')
def hello_world2(blog_type="meituan"):
    filename = "store/%s_items.json" % blog_type
    return render_template('index.html', datas = json.loads(open(filename).read()))

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
