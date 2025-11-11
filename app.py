from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tools')
def tools():
    return render_template('tools.html')


@app.route('/biology/main')
def biology_main():
    return render_template('biology/main.html')

@app.route('/biology/extra')
def biology_extra():
    return render_template('biology/extra.html')

@app.route('/biology/nmt')
def biology_nmt():
    return render_template('biology/nmt.html')


@app.route('/chemistry/main')
def chemistry_main():
    return render_template('chemistry/main.html')

@app.route('/chemistry/extra')
def chemistry_extra():
    return render_template('chemistry/extra.html')

@app.route('/chemistry/nmt')
def chemistry_nmt():
    return render_template('chemistry/nmt.html')

@app.route('/physics/main')
def physics_main():
    return render_template('physics/main.html')

@app.route('/physics/extra')
def physics_extra():
    return render_template('physics/extra.html')

@app.route('/physics/nmt')
def physics_nmt():
    return render_template('physics/nmt.html')

@app.route('/geography/main')
def geography_main():
    return render_template('geography/main.html')

@app.route('/geography/extra')
def geography_extra():
    return render_template('geography/extra.html')

    return render_template('geography/nmt.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
