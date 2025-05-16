from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, XSD, OWL
import random
from datetime import datetime, timedelta
import uuid

# Define namespaces
EX = Namespace("http://example.org#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")

# Create a new RDF graph
g = Graph()

# Bind namespaces
g.bind("ex", EX)
g.bind("rdf", RDF)
g.bind("rdfs", RDFS)
g.bind("owl", OWL)
g.bind("xsd", XSD)

# Helper functions
def random_float(min_val, max_val, decimals=2):
    return round(random.uniform(min_val, max_val), decimals)

def random_date(start_date, end_date):
    time_between = end_date - start_date
    random_days = random.randrange(time_between.days)
    return start_date + timedelta(days=random_days)

# Generate instances
def generate_rainwater_system():
    # Create a rainwater system
    system_id = f"system_{uuid.uuid4().hex[:8]}"
    system_uri = EX[system_id]
    g.add((system_uri, RDF.type, EX.RainWater))
    
    # Generate collection system
    generate_collection_system(system_uri)
    
    # Generate storage system
    generate_storage_system(system_uri)
    
    # Generate treatment system
    generate_treatment_system(system_uri)
    
    # Generate distribution system
    generate_distribution_system(system_uri)
    
    # Generate monitoring system
    generate_monitoring_system(system_uri)
    
    # Generate reuse system
    generate_reuse_system(system_uri)

def generate_collection_system(system_uri):
    # Create catchment area
    catchment_id = f"catchment_{uuid.uuid4().hex[:8]}"
    catchment_uri = EX[catchment_id]
    g.add((catchment_uri, RDF.type, EX.CatchmentArea))
    g.add((catchment_uri, RDFS.comment, Literal("Rooftop catchment area")))
    g.add((system_uri, EX.hasCollection, catchment_uri))
    
    # Create collection components
    components = [
        ("barrel", EX.RainBarrel, "Rain barrel collector"),
        ("gutter", EX.Gutter, "Aluminum gutter system"),
        ("downspout", EX.Downspout, "Vertical downspout")
    ]
    
    for comp_id, comp_type, comp_comment in components:
        comp_uri = EX[f"{comp_id}_{uuid.uuid4().hex[:8]}"]
        g.add((comp_uri, RDF.type, comp_type))
        g.add((comp_uri, RDFS.comment, Literal(comp_comment)))
        g.add((catchment_uri, EX.CollectedBy, comp_uri))

def generate_storage_system(system_uri):
    # Create storage
    storage_id = f"storage_{uuid.uuid4().hex[:8]}"
    storage_uri = EX[storage_id]
    g.add((storage_uri, RDF.type, EX.Storage))
    g.add((system_uri, EX.hasStorage, storage_uri))
    
    # Create storage tank
    tank_id = f"tank_{uuid.uuid4().hex[:8]}"
    tank_uri = EX[tank_id]
    g.add((tank_uri, RDF.type, EX.StorageTank))
    g.add((tank_uri, RDFS.comment, Literal("5000L polyethylene tank")))
    g.add((storage_uri, EX.hasTank, tank_uri))
    
    # Create overflow mechanism
    overflow_id = f"overflow_{uuid.uuid4().hex[:8]}"
    overflow_uri = EX[overflow_id]
    g.add((overflow_uri, RDF.type, EX.OverflowMechanism))
    g.add((overflow_uri, RDFS.comment, Literal("Float valve overflow system")))
    g.add((tank_uri, EX.hasmechanism, overflow_uri))

def generate_treatment_system(system_uri):
    # Create treatment
    treatment_id = f"treatment_{uuid.uuid4().hex[:8]}"
    treatment_uri = EX[treatment_id]
    g.add((treatment_uri, RDF.type, EX.Treatment))
    g.add((system_uri, EX.hasTreatment, treatment_uri))
    
    # Create sedimentation process
    sedimentation_id = f"sedimentation_{uuid.uuid4().hex[:8]}"
    sedimentation_uri = EX[sedimentation_id]
    g.add((sedimentation_uri, RDF.type, EX.Sedimentation))
    g.add((treatment_uri, EX.includes, sedimentation_uri))
    
    # Create sedimentation tank
    sed_tank_id = f"sed_tank_{uuid.uuid4().hex[:8]}"
    sed_tank_uri = EX[sed_tank_id]
    g.add((sed_tank_uri, RDF.type, EX.SedimentationTank))
    g.add((sedimentation_uri, EX.OccursIn, sed_tank_uri))
    
    # Create filtration system
    filtration_id = f"filtration_{uuid.uuid4().hex[:8]}"
    filtration_uri = EX[filtration_id]
    g.add((filtration_uri, RDF.type, EX.FiltrationSystem))
    g.add((filtration_uri, RDFS.comment, Literal("10 micron sediment filter")))
    g.add((treatment_uri, EX.FilteredBy, filtration_uri))
    
    # Create disinfection system
    disinfection_id = f"disinfection_{uuid.uuid4().hex[:8]}"
    disinfection_uri = EX[disinfection_id]
    g.add((disinfection_uri, RDF.type, EX.DisinfectionSystem))
    g.add((disinfection_uri, RDFS.comment, Literal("UV sterilization unit")))
    g.add((treatment_uri, EX.DisinfectedBy, disinfection_uri))

def generate_distribution_system(system_uri):
    # Create distribution
    distribution_id = f"distribution_{uuid.uuid4().hex[:8]}"
    distribution_uri = EX[distribution_id]
    g.add((distribution_uri, RDF.type, EX.Distribution))
    g.add((system_uri, EX.hasDistribution, distribution_uri))
    
    # Create distribution pipe
    pipe_id = f"pipe_{uuid.uuid4().hex[:8]}"
    pipe_uri = EX[pipe_id]
    g.add((pipe_uri, RDF.type, EX.DistributionPipe))
    g.add((pipe_uri, RDFS.comment, Literal("50mm PVC distribution pipe")))
    g.add((distribution_uri, EX.hasPipe, pipe_uri))
    
    # Create pump system
    pump_id = f"pump_{uuid.uuid4().hex[:8]}"
    pump_uri = EX[pump_id]
    g.add((pump_uri, RDF.type, EX.PumpSystem))
    g.add((pump_uri, RDFS.comment, Literal("12V DC diaphragm pump")))
    g.add((distribution_uri, EX.hasPump, pump_uri))
    
    # Create control valve
    valve_id = f"valve_{uuid.uuid4().hex[:8]}"
    valve_uri = EX[valve_id]
    g.add((valve_uri, RDF.type, EX.ControlValve))
    g.add((valve_uri, RDFS.comment, Literal("Solenoid control valve")))
    g.add((distribution_uri, EX.hasValve, valve_uri))

def generate_monitoring_system(system_uri):
    # Create monitoring
    monitoring_id = f"monitoring_{uuid.uuid4().hex[:8]}"
    monitoring_uri = EX[monitoring_id]
    g.add((monitoring_uri, RDF.type, EX.Monitoring))
    g.add((system_uri, EX.hasMonitoring, monitoring_uri))
    
    # Create sensor types with random readings
    sensor_types = [
        (EX.Salinity, "Salinity sensor", 0.5, 35.0),  # Practical salinity units
        (EX.Temperature, "Water temperature sensor", 5.0, 30.0),  # °C
        (EX.Transparency, "Water transparency sensor", 0.1, 10.0),  # Secchi depth in meters
        (EX.DissolvedOxygen, "DO sensor", 0.0, 15.0),  # mg/L
        (EX.Ammonium, "Ammonium sensor", 0.0, 2.0),  # mg/L
        (EX.NitrateNitrite, "Nitrate sensor", 0.0, 10.0),  # mg/L
        (EX.Phosphate, "Phosphate sensor", 0.0, 1.0)  # mg/L
    ]
    
    for sensor_class, comment, min_val, max_val in sensor_types:
        sensor_id = f"sensor_{uuid.uuid4().hex[:8]}"
        sensor_uri = EX[sensor_id]
        g.add((sensor_uri, RDF.type, sensor_class))
        g.add((sensor_uri, RDFS.comment, Literal(comment)))
        g.add((monitoring_uri, EX.hasSensor, sensor_uri))
        
        # Add sensor properties
        g.add((sensor_uri, EX.hasID, Literal(str(uuid.uuid4()))))
        g.add((sensor_uri, EX.hasModel, Literal("Model-X200")))
        
        # Create location
        loc_id = f"loc_{uuid.uuid4().hex[:8]}"
        loc_uri = EX[loc_id]
        g.add((loc_uri, RDF.type, EX.Location))
        g.add((loc_uri, EX.hasLat, Literal(random_float(-90, 90), datatype=XSD.float)))
        g.add((loc_uri, EX.hasLang, Literal(random_float(-180, 180), datatype=XSD.float)))
        g.add((sensor_uri, EX.hasLocation, loc_uri))
        
        # Generate 5 random readings for each sensor
        for _ in range(5):
            reading_id = f"reading_{uuid.uuid4().hex[:8]}"
            reading_uri = EX[reading_id]
            g.add((reading_uri, RDF.type, EX.SensorReading))
            g.add((reading_uri, EX.hasUnit, Literal("mg/L" if "Oxygen" in comment else "PSU" if "Salinity" in comment else "°C" if "Temperature" in comment else "m" if "Transparency" in comment else "mg/L")))
            
            # Add timestamp
            timestamp = random_date(datetime(2023, 1, 1), datetime(2023, 12, 31))
            g.add((sensor_uri, EX.hasTime, Literal(timestamp.isoformat(), datatype=XSD.dateTime)))
            
            # Add reading value
            reading_value = random_float(min_val, max_val)
            g.add((sensor_uri, EX.hasReading, Literal(reading_value, datatype=XSD.float)))

def generate_reuse_system(system_uri):
    # Create reuse
    reuse_id = f"reuse_{uuid.uuid4().hex[:8]}"
    reuse_uri = EX[reuse_id]
    g.add((reuse_uri, RDF.type, EX.Reuse))
    g.add((system_uri, EX.hasReuse, reuse_uri))
    
    # Create irrigation use
    irrigation_id = f"irrigation_{uuid.uuid4().hex[:8]}"
    irrigation_uri = EX[irrigation_id]
    g.add((irrigation_uri, RDF.type, EX.Irrigation))
    g.add((reuse_uri, EX.UsedFor, irrigation_uri))
    
    # Create non-potable use
    nonpotable_id = f"nonpotable_{uuid.uuid4().hex[:8]}"
    nonpotable_uri = EX[nonpotable_id]
    g.add((nonpotable_uri, RDF.type, EX.NonPottable))
    g.add((reuse_uri, EX.DesignatedFor, nonpotable_uri))

# Generate data for 3 complete rainwater systems
for _ in range(3):
    generate_rainwater_system()

# Serialize the graph to Turtle format
output = g.serialize(format="turtle", encoding="utf-8").decode("utf-8")

# Save to file
with open("rainwater_system_data.ttl", "w") as f:
    f.write(output)

print("Generated data saved to rainwater_system_data.ttl")