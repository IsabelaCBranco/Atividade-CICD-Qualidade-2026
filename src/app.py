from flask import Flask, request, render_template_string
from calculadora import juros_compostos
app = Flask(__name__)
PAGINA = """
<form method="get" action="/calcular">
    <input name="principal" id="principal" value="1000">
    <input name="taxa" id="taxa" value="0.05">
    <input name="periodos" id="periodos" value="12">
    <button type="submit" id="calcular">Calcular</button>
</form>
{% if resultado is not none %}<p id="resultado">Montante: {{ resultado }}</p>{% endif %}
"""
@app.route("/")
def index(): return render_template_string(PAGINA, resultado=None)
@app.route("/calcular")
def calcular():
    r = juros_compostos(float(request.args["principal"]),
                        float(request.args["taxa"]),
                        int(request.args["periodos"]))
    return render_template_string(PAGINA, resultado=r)

if __name__ == "__main__":
    import os
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
    