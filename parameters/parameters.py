import os

ENERGY_FILE_NAME = "energydata_complete.csv"
#INSURANCE_FILE_NAME = "insurance.csv"

DATA_FOLDER = "data"
main_path = os.getcwd()

energy_file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), ENERGY_FILE_NAME)
#insurance_file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), INSURANCE_FILE_NAME)

autogluon_params = {
    "save_path": 'artefacts/models_regression',
    "time_limit": 60,
    "label": "Appliances",
    "problem_type": "regression"
}