"""def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
    return wrapper


@handle_errors
def load_data():
    x = 10 / 0  # error


load_data()"""



"""
import pandas as pd
_source_path = r"C:\Users\ACER\Documents\vs_code\coding\spark\sample1.csv"
_target_path = r"C:\Users\ACER\Documents\vs_code\coding\spark\target.csv"

def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in panads dataframe")
    return wrapper
    

@handle_errors
def load_data():
    df = pd.read_csv(_source_path)
    print(df.head())
    return df
df = load_data()"""



import pandas as pd
_source_path = r"C:\Users\ACER\Documents\vs_code\coding\spark\sample1.csv"
_target_path = r"C:\Users\ACER\Documents\vs_code\coding\spark\target.csv"
def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except Exception as e:
            print(f"Error in panads dataframe")
    return wrapper


@handle_errors
def load_data():
    try:
        pd.read_csv(_source_path)
        return pd.count()
        if pd.count < 50:
            print(f"today there is no data")
    except Exception as e:
        print(f"failed to get data from path which is {_source_path}")


df = load_data()
    
        


