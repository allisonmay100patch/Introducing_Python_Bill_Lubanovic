from  flask import Flask, render_template, request

app = Flask(__name__,static_folder='.',static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('home.j2')

@app.route('/echo/')
def echo():
    thing = request.args.get('thing')
    height = request.args.get('height')
    color = request.args.get('color')
    return render_template('home.j2',thing=thing,height=height,color=color)
app.run(port=5000,debug=True)