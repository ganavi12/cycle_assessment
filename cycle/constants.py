from enum import Enum


class Frame(Enum):
    CANTILEVER = "CANTILEVER"
    DIAMOND = "DIAMOND"
    ORDINARY = "ORDINARY"


class HandleType(Enum):
    DROP = "DROP"
    ORDINARY = "ORDINARY"


class SeatType(Enum):
    COMFORT = "COMFORT"
    ORDINARY = "ORDINARY"


class Wheel(Enum):
    TUBLESS = "TUBLESS"
    WIHTTUBE = "WIHTTUBE"
