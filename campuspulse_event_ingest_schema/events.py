# Events rough Schema
# https://docs.pydantic.dev/latest/concepts/models/

import datetime
from pydantic import BaseModel, Field, datetime_parse
from typing import List, Optional

class StringDatetime(datetime.datetime):

    @classmethod
    def from_iso(cls, iso: str):
        """Parse ISO string to datetime"""
        dt = datetime_parse.parse_datetime(iso) 
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

# test it 
# dt = StringDatetime.from_iso("2024-01-01T07:15:00.000")
# print(dt)
    
class StringDate(datetime.datetime):
    @classmethod
    def from_iso(cls, iso: str):
        """Parse ISO string to date"""
        dt = datetime_parse.parse_datetime(iso) 
        return dt.date()
        
# test it 
# dt = StringDate.from_iso("2024-01-01T07:15:00.000")
# print(dt)

class StringTime(datetime.datetime):
    @classmethod
    def from_iso(cls, iso: str):
        """Parse ISO string to time"""
        dt = datetime_parse.parse_datetime(iso) 
        return dt.time()
        
# test it 
# dt = StringTime.from_iso("2024-01-01T07:15:00.000")
# print(dt)


class Location(BaseModel):
        """
        {
            "street": str,
            "city": str,
            "state": str,
            "zip": str,
            "building": str,
            "room-number": int
       
        }
        """
        street: Optional[str]
        city: Optional[str]
        state: Optional[str]
        zip: Optional[str]
        building: Optional[str]
        room_number: Optional[int]
        

class Event(BaseModel):
    """ name: str,
        event_id: int,   
        location: Location, 
        date: int,
        isAllDay: bool,
        time_start: int, 
        time_end: int, 
        duration: int, 
        description: str, 
        host: str
    """

    name: Optional[str]
    event_id: Optional[int]
    location: Optional[Location]
    date: Optional[StringDate]
    isAllDay: Optional[bool]
    time_start: Optional[StringTime]
    time_end: Optional[StringTime]
    duration: Optional[StringTime]
    description: Optional[str]
    host: Optional[str]

        

class EventMetadata:
    def __init__(self, event: Event, tags, is_public, source_id, source_link, submitter):
        self.event = event
        self.tags = tags
        self.is_public = is_public 
        self.source_id = source_id 
        self.source_link = source_link
        self.submitter = submitter

class Freebies:
    def __init__(self, event, freebies):
        self.event = event
        self.freebies = freebies