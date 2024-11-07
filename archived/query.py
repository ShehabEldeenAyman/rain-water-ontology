from rdflib import Graph

# Create a graph and load RDF data
g = Graph()
g.parse("data.ttl", format="turtle")

# Define the SPARQL query to find all subjects with ex:Storage
query = """
PREFIX ex: <http://example.org#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?subject
WHERE {
    ?subject ex:Has ex:Storage1 .
}
"""

# Execute the query
results = g.query(query)

# Print the results
for row in results:
    print(row[0])
