# Events rough Schema
# https://docs.pydantic.dev/latest/concepts/models/

import datetime

from .common import BaseModel
from typing import List, Dict, Optional
from pydantic import BaseModel, HttpUrl

class Time(BaseModel):
    arrival: str
    departure: Optional[str] # departure time. if not present, it is up to the implementor to make a guess. recommendations: either use the same arrival time, or arrival time + 59 seconds, or some other predefined interval based on how long the busses wait at each stop

class Stop(BaseModel):
    stop_id: int
    name: str
    times: List[Time]

class Route(BaseModel):
    route_id: str
    name: str
    stops: List[Stop]
    source_url: HttpUrl

class ServiceAlert(BaseModel):
    alert_id: str
    description: str
    severity: str  # e.g., 'low', 'medium', 'high'

class BusSchedule(BaseModel):
    source_url: HttpUrl
    service_alerts: List[ServiceAlert]
    routes: List[Route]