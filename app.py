# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:07:35 2025

@author: tamer
"""

from flask import Flask, request, render_template_string
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

    return render_template_string('''
        <h1>SPARQL Query Interface</h1>
        <form method="post">
            <textarea name="query" rows="10" cols="50"></textarea><br>
            <input type="submit" value="Run Query">
        </form>
        {% if error_message %}
            <p style="color: red;">{{ error_message }}</p>
        {% endif %}
        <h2>Results:</h2>
        {% if results %}
            <table border="1">
                <tr>
                    {% for key in results[0].keys() %}
                        <th>{{ key }}</th>
                    {% endfor %}
                </tr>
                {% for row in results %}
                    <tr>
                        {% for value in row.values() %}
                            <td>{{ value }}</td>
                        {% endfor %}
                    </tr>
                {% endfor %}
            </table>
        {% else %}
            <p>No results found.</p>
        {% endif %}
        <div id="pagination">
            <button onclick="prevPage()">Previous</button>
            <span id="pageInfo"></span>
            <button onclick="nextPage()">Next</button>
        </div>
        <script>
            let currentPage = 1;
            const rowsPerPage = 10;

            function showPage(page) {
                const rows = document.querySelectorAll('table tr');
                rows.forEach((row, index) => {
                    if (index === 0 || (index > (page - 1) * rowsPerPage && index <= page * rowsPerPage)) {
                        row.style.display = '';
                    } else {
                        row.style.display = 'none';
                    }
                });
                document.getElementById('pageInfo').innerText = `Page ${page}`;
            }

            function prevPage() {
                if (currentPage > 1) {
                    currentPage--;
                    showPage(currentPage);
                }
            }

            function nextPage() {
                const rows = document.querySelectorAll('table tr').length - 1;
                if (currentPage < Math.ceil(rows / rowsPerPage)) {
                    currentPage++;
                    showPage(currentPage);
                }
            }

            showPage(currentPage);
        </script>
    ''', results=results, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)