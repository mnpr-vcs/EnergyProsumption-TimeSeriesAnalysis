from matplotlib import rcParams
import seaborn as sns

# visualization settings
rcParams["figure.figsize"] = 25, 10
rcParams["timezone"] = "UTC"
sns.set_style("whitegrid")

# data I/O paths and filenames
io_paths = {
    "DATASET": "./datasets/electricityConsumptionAndProduction.csv",
    "DATASET_TEMP_AIR_17": "./datasets/energy_charts/energy-charts_Air_temperature_in_Germany_in_2017.csv",
    "DATASET_TEMP_AIR_18": "./datasets/energy_charts/energy-charts_Air_temperature_in_Germany_in_2018.csv",
    "DATASET_TEMP_AIR_19": "./datasets/energy_charts/energy-charts_Air_temperature_in_Germany_in_2019.csv",
    "DATASET_EC_LOAD_17": "./datasets/energy_charts/energy-charts_Public_net_electricity_generation_in_Germany_in_2017.csv",
    "DATASET_EC_LOAD_18": "./datasets/energy_charts/energy-charts_Public_net_electricity_generation_in_Germany_in_2018.csv",
    "DATASET_EC_LOAD_19": "./datasets/energy_charts/energy-charts_Public_net_electricity_generation_in_Germany_in_2019.csv",
    "DATA_EC_LOAD_MAIN": "./datasets/stationary/load_ec.csv",
    "VIZ_OUTPUT_1": "./output/dataset1/",
    "VIZ_OUTPUT_2": "./output/dataset2/",
}

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"