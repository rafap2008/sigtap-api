from flask import render_template

def getRotasApi(app):
    links = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and rule.rule != '/' and rule.endpoint != 'static' and rule.endpoint.startswith('get_'):
            links.append(rule.rule)

    return links

def getHome(app):
    return render_template("home.html", rotas=getRotasApi(app))

def toBool(valor):
    return str(valor).upper() in ['1', 'S', 'SIM', 'TRUE', 'T']