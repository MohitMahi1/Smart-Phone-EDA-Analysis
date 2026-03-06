# app/models.py

from pydantic import BaseModel
from typing import Optional


class SmartphoneInput(BaseModel):
    ram_capacity: Optional[int] = None
    internal_memory: Optional[int] = None
    processor_brand: Optional[str] = None
    processor_speed: Optional[float] = None
    refresh_rate: Optional[int] = None
    primary_camera_rear: Optional[int] = None
    battery_capacity: Optional[int] = None
    has_5g: Optional[int] = None
    fast_charging_available: Optional[int] = None
    fast_charging: Optional[int] = None
    screen_size: Optional[float] = None
    num_rear_cameras: Optional[int] = None
    extended_memory_available: Optional[int] = None
    rating: Optional[float] = None
    has_nfc: Optional[int] = None