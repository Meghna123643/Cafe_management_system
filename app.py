from flask import Flask, render_template, request

app = Flask(__name__)

menu = {
    'Pizza': 80,
    'Momos': 60,
    'Egg': 50,
    'Pav Bhaji': 90,
    'Chai': 10,
    'Coffee': 30,
    'Panipuri': 50,
    'Biscuit': 10
}

@app.route('/', methods=['GET', 'POST'])
def index():
    total = 0
    ordered_items = []
    if request.method == 'POST':
        items = request.form.getlist('items')
        for item in items:
            total += menu[item]
            ordered_items.append((item, menu[item]))
        return render_template('index.html', menu=menu, ordered_items=ordered_items, total=total)
    return render_template('index.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
