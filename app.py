from flask import Flask, jsonify, request

app = Flask(__name__)

# Page d'accueil avec HTML inline
@app.route("/")
def home():
    return """
    <h1>Bienvenue sur mon app Flask 🚀</h1>
    <p><a href='/api/products'>Voir les produits en JSON</a></p>
    <p><a href='/form'>Tester le formulaire</a></p>
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
        <input type="submit" value="Envoyer">
    </form>
    """

# Gestion des erreurs
@app.errorhandler(404)
def not_found(e):
    return """
    <h1>404 - Page non trouvée 😢</h1>
    <p><a href='/'>Retour à l'accueil</a></p>
    """, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

