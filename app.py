# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:07:35 2025

@author: tamer
"""

from flask import Flask, request, render_template
from rdf_queries import load_rdf, run_sparql_query
from rdflib import URIRef, BNode

app = Flask(__name__)

# RDF dosyasını yükle
g = load_rdf("cloud_family.rdf")

def shorten_uri(term):
    if isinstance(term, URIRef):
        return term.split("#")[-1]  # URI'yi kısalt
    elif isinstance(term, BNode):
        return f"BlankNode:{str(term)}"  # Blank node'ları özel olarak işaretle
    return str(term)  # Diğer durumlarda (literal, vs.) string olarak döndür

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    error_message = None
    if request.method == 'POST':
        query = request.form['query']
        try:
            raw_results = run_sparql_query(g, query)
            results = [{key: shorten_uri(value) for key, value in row.items()} for row in raw_results]
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"

    return render_template('index.html', results=results, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)
