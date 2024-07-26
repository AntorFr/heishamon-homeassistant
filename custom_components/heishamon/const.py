"""Constant values for HeishaMon integration."""

from enum import Enum

DOMAIN = "heishamon"


class DeviceType(Enum):
    HEATPUMP = 1
    HEISHAMON = 2
