from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


#Create WildConservation Species List

species_list =[
    {"name": "Elephant","habitat":"Africa"},
    {"name": "Tiger", "habitat": "Asia"},
    {"name": "Giant Panda", "habitat": "China"},
    {"name": "Polar Bear", "habitat": "Arctic"},
    {"name": "Kangaroo", "habitat": "Australia"},
    {"name": "Bald Eagle", "habitat": "North America"},
    {"name": "Emperor Penguin", "habitat": "Antarctica"},
    {"name": "Komodo Dragon", "habitat": "Indonesia"},
    {"name": "Jaguar", "habitat": "South America"},
    {"name": "Red Fox", "habitat": "Europe"}
]

@app.route('/')
def index():
    return render_template('index.html',species_list= species_list)

@app.route('/add_species', methods=['GET','POST'])
def add_species():
    if request.method =='POST':
        name = request.form['name']
        habitat = request.form['habitat']
        species_list.append({"name":name, "habitat": habitat})
        return redirect(url_for('index'))
    return render_template('add_species.html')

if __name__=='__main__':
    app.run(debug=True)