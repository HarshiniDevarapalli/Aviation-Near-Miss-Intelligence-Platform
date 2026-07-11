from src.data_loader import DataLoader

loader = DataLoader(
    "data/processed/asrs_clean_final.csv"
)

df = loader.load_data()

print(df.head())