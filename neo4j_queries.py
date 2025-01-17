# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:02:46 2025

@author: tamer
"""

# neo4j_queries.py
from neo4j import GraphDatabase

def connect_to_neo4j(uri, username, password):
    driver = GraphDatabase.driver(uri, auth=(username, password))
    return driver

def run_cypher_query(driver, query):
    with driver.session() as session:
        result = session.run(query)
        return [record for record in result]