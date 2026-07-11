import pandas as pd


class DataLoader:
    """
    Loads and prepares the cleaned ASRS dataset.
    """

    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def load_data(self) -> pd.DataFrame:
        """
        Load the cleaned CSV into a DataFrame.
        """
        df = pd.read_csv(self.csv_path)

        print(f"Loaded {len(df)} incidents.")

        return df

    def prepare_documents(self, df):

        df = df.copy()

        if "length" in df.columns:
            df = df.drop(columns=["length"])

        documents = (
            df["Synopsis"].fillna("") +
            "\n\n" +
            df["full_narrative"].fillna("")
        ).tolist()

        return documents
    def prepare_metadata(self, df):

        metadata = []

        for _, row in df.iterrows():

            metadata.append({
                "acn": str(row["ACN"]),
                "date": str(row["Date"]),
                "primary_problem": str(row["Primary Problem"]),
                "result": str(row["Result"]),
                "contributing_factors": str(row["Contributing Factors / Situations"])
            })

        return metadata