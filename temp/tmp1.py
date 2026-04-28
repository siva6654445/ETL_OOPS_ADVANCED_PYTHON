import pandas as pd
import time

_source_path = r"C:\Users\ACER\Documents\vs_code\coding\spark\sample1.csv"

def etl_monitor(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Running: {func.__name__}")
        print(f"Start Time: {time.strftime('%H:%M:%S')}")

        try:
            result = func(*args, **kwargs)

            end = time.time()
            print(f"End Time: {time.strftime('%H:%M:%S')}")
            print(f"Execution Time: {end - start:.2f} sec")

            # Bonus: row count logging
            if isinstance(result, pd.DataFrame):
                print(f"Rows processed: {len(result)}")

            return result

        except Exception as e:
            print(f"[ERROR] {func.__name__}: {e}")

    return wrapper


@etl_monitor
def load_data(path):
    df = pd.read_csv(path)

    if len(df) < 50:
        print("Warning: Low data volume")
    return df


df = load_data(_source_path)