# Document and file reading:
import os
import pandas as pd


def extract_bring_options(filepath: str) -> tuple[str, ...]:
    
    # Creating dataframe and extracting lines from table:
    dataframe = pd.read_excel(filepath)
    bingo_options = tuple(dataframe["Bingo"].dropna().astype(str).tolist())
    
    # Returning:
    return bingo_options

