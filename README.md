# Customer Segmentation Model Data/Feature Ingestion Example

## Overview

This project implements a comprehensive customer segmentation and profiling system for educational purposes, demonstrating how a real company might approach ML model data feature ingestion and customer analysis.  

## Components

### 1. Data Ingestion

The `raw_data_ingestor` class in `data_ingestion.py` is responsible for collecting various types of customer data:

- Last 12 months of order data
- Demographic information
- Loyalty program data
- Website browsing data

### 2. Feature Extraction

The `features_generator` classes in `feature_extraction.py` process the raw data to extract meaningful features:

- Product-related features (frequency, monetary value, recency, etc.)
- Channel-related features (device types, brand channels, marketing channels)
- Website behavior features (browsing habits, product types viewed)

### 3. Customer Profiling

The `profiler` classes in `customer_profiling.py` use the extracted features to create comprehensive customer profiles:

- Spending profiles (deciles, channels, statistics)
- Demographic and loyalty information
- Price sensitivity analysis
- Product preferences and shopping patterns

## Usage

To use this system:

1. Ingest raw data using the `raw_data_ingestor` class.
2. Extract features using the appropriate `features_generator` classes.
3. Generate customer profiles using the `profiler` classes.
4. Analyze the results to gain insights into customer behavior and preferences.

## Note

This project is for educational purposes and demonstrates the structure and components of a real-world ML model data feature ingestion system. In a production environment, additional considerations such as data privacy, scalability, and integration with existing systems would be necessary.
