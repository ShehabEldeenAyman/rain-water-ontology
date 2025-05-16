# Rainwater Ontology Project

![Rainwater System Diagram](media/image1.png)

A semantic model for rainwater management systems, including collection, storage, treatment, distribution, monitoring, and reuse components.

## Table of Contents
- [Overview](#overview)
- [Ontology Structure](#ontology-structure)
- [Components](#components)
- [Data Generation](#data-generation)
- [Validation](#validation)
- [Usage](#usage)
- [Future Work](#future-work)

## Overview

This project provides:
- A comprehensive **OWL ontology** for rainwater management systems
- **SHACL constraints** for data validation
- A **Python data generator** for synthetic test data
- A **SHACL validator** to ensure data quality

The ontology models all aspects of rainwater systems with particular emphasis on water quality monitoring through various sensor types.

## Ontology Structure

### Core Classes
```mermaid
graph TD
    RainWater --> Collection
    RainWater --> Storage
    RainWater --> Treatment
    RainWater --> Distribution
    RainWater --> Monitoring
    RainWater --> Reuse
    
    Collection --> CatchmentArea
    Collection --> RainBarrel
    Collection --> Gutter
    Collection --> Downspout
    
    Monitoring --> WaterQualitySensor
    WaterQualitySensor --> Salinity
    WaterQualitySensor --> Temperature
    WaterQualitySensor --> DissolvedOxygen
    %% ... other sensor types