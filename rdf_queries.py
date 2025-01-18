# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:02:10 2025

@author: tamer
"""

# rdf_queries.py
from rdflib.plugins.sparql import prepareQuery
from rdflib import Graph

def load_rdf(file_path):
    g = Graph()
    g.parse(file_path, format="xml")
    return g

def run_sparql_query(graph, query):
    prepared_query = prepareQuery(query)
    results = graph.query(prepared_query)
    # Sonuçları uygun formata dönüştür
    formatted_results = []
    for row in results:
        formatted_row = {}
        for key in row.labels:
            formatted_row[key] = row[key]
        formatted_results.append(formatted_row)
    return formatted_results