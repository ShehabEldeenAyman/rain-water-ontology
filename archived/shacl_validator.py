from rdflib import Graph
from pyshacl import validate

# Load your RDF data
data_graph = Graph()
data_graph.parse("data_modified.ttl", format="ttl")  # Replace with your data file

# Load your SHACL shapes
shacl_graph = Graph()
shacl_graph.parse("shapes.ttl", format="ttl")  # Replace with your SHACL shapes file

# Validate
conforms, results, report_graph = validate(data_graph, shacl_graph=shacl_graph)

if conforms:
    print("Validation passed.")
else:
    print("Validation failed.")
    print(results)
    print(report_graph)

