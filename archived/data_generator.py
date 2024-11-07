# Python script to generate 100 Turtle instances for various sensors

# Define sensor types and their starting reading values
sensor_types = [
    ("Salinity", 35.0),         # Starting reading for each sensor type
    ("Temperature", 22.0),
    ("Transparency", 4.0),
    ("DissolvedOxygen", 7.5),
    ("Ammonium", 0.4),
    ("NitrateNitrite", 0.1),
    ("TotalNitrogen", 2.0),
    ("Phosphate", 0.05),
    ("TotalPhosphorus", 0.03),
    ("DissolvedSilica", 1.1),
    ("TotalOrganicCarbon", 10.0),
    ("ParticulateOrganicCarbon", 3.0)
]

num_instances = 100
instances_per_sensor = num_instances // len(sensor_types)
increment_value = 0.1  # Increment to make each reading unique

# Generate Turtle format output
turtle_output = ""

for sensor, start_value in sensor_types:
    for i in range(1, instances_per_sensor + 1):
        instance_name = f"ex:{sensor}Sensor{i}"
        reading_value = start_value + (i * increment_value)
        
        # Add instance with a unique reading
        turtle_output += f"{instance_name} a ex:{sensor} ;\n"
        turtle_output += f'    rdfs:label "{sensor} Sensor Instance {i}" ;\n'
        turtle_output += f'    ex:hasReading "{reading_value:.2f}"^^xsd:float .\n\n'

# Save to file or print
with open("sensor_instances.ttl", "w") as f:
    f.write(turtle_output)

print("100 sensor instances generated and saved to 'sensor_instances.ttl'")
