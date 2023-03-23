import pandas as pd
from parameters.parameters import energy_file_path

appliance_energy_data = pd.read_csv(energy_file_path)