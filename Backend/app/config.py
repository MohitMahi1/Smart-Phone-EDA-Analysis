# app/config.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "smartphone_price_model.pkl"
FEATURE_PATH = BASE_DIR / "model" / "model_features.pkl"

DEFAULT_FEATURES = {
    "ram_capacity": 8,                    # GB
    "internal_memory": 128,               # GB
    "processor_brand": "snapdragon",      # must exist in training data
    "processor_speed": 2.0,               # GHz
    "refresh_rate": 60,                   # Hz
    "primary_camera_rear": 50,            # MP
    "battery_capacity": 5000,             # mAh
    "has_5g": 0,                          # 0 = No, 1 = Yes
    "fast_charging_available": 1,         # 0/1
    "fast_charging": 33,                  # Watts
    "screen_size": 6.5,                   # inches
    "num_rear_cameras": 3,
    "extended_memory_available": 1,       # 0/1
    "rating": 4.2,                        # average rating
    "has_nfc": 0                          # 0/1
}