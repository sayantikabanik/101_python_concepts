# Just required imports to get started
import kagglehub
from kagglehub import KaggleDatasetAdapter


# connect to saya's kagglehub
def kaggle_connect(remote_file_name):
    try:
        df_kaggle_data = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            "sayantikabanik/twilio-stock-price-twlo20162021",
            remote_file_name
        )
        return df_kaggle_data
    except ImportError:
        raise ImportError("Required kagglehub or pandas package not installed")
    except ConnectionError:
        raise ConnectionError("Failed to connect to Kaggle servers. Please check your internet connection.")
    except PermissionError:
        raise PermissionError("Authentication failed. Ensure you have set up your Kaggle API credentials correctly.")
    except FileNotFoundError:
        raise FileNotFoundError(f"Remote file '{remote_file_name}' not found in the specified dataset.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")


# store the dataset locally as stock_market.csv
def store_locally(df, local_file_name):
    df.to_csv(local_file_name, sep='\t')
    return 0


if __name__ == '__main__':
    kaggle_file_path = "TWLO_stock.csv"
    local_file_path = f"local_{kaggle_file_path}"
    df_kaggle_data = kaggle_connect(kaggle_file_path)
    store_locally(df_kaggle_data, local_file_path)
