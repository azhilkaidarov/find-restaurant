import json
import os
import pandas as pd


def read_json(file_path: str) -> dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_result(df: pd.DataFrame, output_path: str):
    df.to_csv(output_path, index=False)
    print(f"Результаты сохранены в: {output_path}")
