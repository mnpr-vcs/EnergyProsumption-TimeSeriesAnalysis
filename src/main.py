from components import config
from components.utils import (
    get_csv_dataframe
    , adf_test
    , kpss_test
    , get_error_metrics
)
from components.ts_logger import logger



if __name__ == "__main__":

    dataset_path = config.io_paths["DATASET"]
    index_column = "DateTime"
    datetime_format = config.DATETIME_FORMAT

    df = get_csv_dataframe(dataset_path, index_column, datetime_format)
    print(df.tail(3))
    logger.info("logger from main !!")

