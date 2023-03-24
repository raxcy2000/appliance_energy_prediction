# Main Entrypoint
from parameters.parameters import (
    energy_file_path, insurance_file_path, autogluon_params
)
from data_ingestion.ingest import get_data
from model_building.build_model import autogluon_model_build
import time


# Stage 0 - Data Ingestion
print("Starting Data Ingestion")
print("Starting Energy Data...")
start_time = time.time()
appliance_energy_data = get_data(energy_file_path)
end_time = time.time()
print(f"Execution time for Appliance Energy Data Ingestion is {end_time - start_time} seconds")
print(f"Size of Applicance Energy Data is {appliance_energy_data.shape}")
print(appliance_energy_data.head())


# print("Starting Insurance Data...")
# start_time = time.time()
# insurance_data = get_data(insurance_file_path)
# end_time = time.time()
# print(f"Execution time for Insurance Data Ingestion is {end_time - start_time} seconds")
# print(f"Size of Insurance Data is {insurance_data.shape}")
# print(insurance_data.head())

# Stage 1
"""
EDA
"""

# Stage 2 - Model Building
print("Starting Model Builidng...")
start_time = time.time()
train_data, test_data, predictor = (
    autogluon_model_build(appliance_energy_data, autogluon_params)
)
end_time = time.time()
print(f"Execution time for Model Building is {end_time - start_time} seconds")
print(f"Size of Train Data is {train_data.shape}")
print(f"Size of Test Data is {test_data.shape}")

# Stage 3 - Model Evaluation
print("Starting Model Evaluation...")
start_time = time.time()
print(predictor.leaderboard(silent=True))
end_time = time.time()
print(f"Execution time for Model Evaluation (Train) is {end_time - start_time} seconds")
start_time = time.time()
print(predictor.leaderboard(test_data, silent=True))
end_time = time.time()
print(f"Execution time for Model Evaluation (Test) is {end_time - start_time} seconds")