from flask import Flask, jsonify, request

app = Flask(__name__)

# Page d'accueil avec HTML inline
@app.route("/")
def home():
    return """
    <h1>Bienvenue sur mon app Flask 🚀</h1>
    <p><a href='/api/products'>Voir les produits en JSON</a></p>
    <p><a href='/form'>Tester le formulaire</a></p>
    <p><a href='/about'>À propos</a></p>
    """

# API JSON avec données simulées
@app.route("/api/products")
def products():
    data = [
        {"id": 1, "name": "Laptop", "price": 1200},
        {"id": 2, "name": "Smartphone", "price": 800},
        {"id": 3, "name": "Casque Audio", "price": 150}
    ]
    return jsonify({"status": "success", "products": data})

# Formulaire GET + POST (tout inline)
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return f"""
        <h2>Bienvenue {name} 🎉</h2>
        <p>Ton email : {email}</p>
        <p><a href='/'>Retour à l'accueil</a></p>
        """
    return """
    <h1>Formulaire d'inscription</h1>
    <form method="POST">
        <label>Nom :</label>
        <input type="text" name="name"><br>
        <label>Email :</label>
        <input type="email" name="email"><br>
        <button type="submit">Envoyer</button>
    </form>
    """

# Nouvelle page "À propos"
@app.route("/about")
def about():
    return """
    <h1>À propos</h1>
    <p>Cette petite app Flask est une démo avec :</p>
    <ul>
        <li>Une page d'accueil</li>
        <li>Une API JSON simulée</li>
        <li>Un formulaire GET/POST</li>
    </ul>
    <p>Code prêt à être poussé sur GitHub 🚀</p>
    <p><a href='/'>Retour à l'accueil</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True)

