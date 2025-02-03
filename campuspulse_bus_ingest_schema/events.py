# Events rough Schema
# https://docs.pydantic.dev/latest/concepts/models/

import datetime

from .common import BaseModel
from typing import List, Dict, Optional
from pydantic import BaseModel, HttpUrl

class ArrivalTime(BaseModel):
    time: str

class Stop(BaseModel):
    stop_id: int
    name: str
    arrival_times: List[ArrivalTime]

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