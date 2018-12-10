import sys
from adafruit_blinka.agnostic import board_id


if board_id == "raspi_2" or board_id == "raspi_3":
    from adafruit_blinka.microcontroller.bcm283x.pulseio.PulseIn import PulseIn as PulseIn
