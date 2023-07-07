"""Deprecated import location for schema"""

import warnings

from .load import ImportMatchAction, ImportSourceLocation  # noqa: F401
from .location import (  # noqa: F401
    Access,
    Address,
    Availability,
    Contact,
    LatLng,
    Link,
    NormalizedLocation,
    OpenDate,
    OpenHour,
    Organization,
    Source,
    Vaccine,
)

"""
DEPRECATION NOTICE
rit_housing_data_schema/schema.py is DEPRECATED. Instead of using this file,
import the file that you care about:

from rit_housing_data_schema import location
~or~
from rit_housing_data_schema import load

This may be removed in a future major version bump.
"""
warnings.warn(
    "rit_housing_data_schema.schema is deprecated. "
    + "Use rit_housing_data_schema.location or rit_housing_data_schema.load instead",
    DeprecationWarning,
    stacklevel=2,
)
