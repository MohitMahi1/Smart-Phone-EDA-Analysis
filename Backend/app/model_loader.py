# app/model_loader.py

import joblib
import pandas as pd

from app.config import MODEL_PATH, FEATURE_PATH, DEFAULT_FEATURES


# Load trained model
model = joblib.load(MODEL_PATH)

# Load feature column order
feature_columns = joblib.load(FEATURE_PATH)


def prepare_input(user_input: dict) -> pd.DataFrame:
    """
    Merge user input with default values
    and return properly ordered DataFrame
    """

    final_input = DEFAULT_FEATURES.copy()

    for key, value in user_input.items():
        if value is not None:
            final_input[key] = value

    ordered_input = {col: final_input[col] for col in feature_columns}

    return pd.DataFrame([ordered_input])


def predict_price(user_input: dict) -> float:

    df_input = prepare_input(user_input)

    prediction = model.predict(df_input)[0]

    return round(float(prediction), 2)