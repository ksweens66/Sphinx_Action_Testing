"""
This program is used to proof-of-concept test a few ideas
1) Can we use enumerations as function inputs
2) Does the bit-shift logic in get_status_bit properly parse the status
"""
from enum import IntEnum

# Define the locations of the status bit
class LASER_STATUS_BITS(IntEnum):
    SPARE_15 = 15
    SPARE_14 = 14
    HIGH_POWER_MODE = 13
    LOW_POWER_MODE = 12
    READY_TO_FIRE = 11
    READ_TO_ENABLE = 10
    POWER_FAILURE = 9
    ELECTRICAL_OVERTEMP = 8
    RESONATOR_OVERTEMP = 7
    EXTERNAL_INTERLOCK = 6
    RESERVED_5 = 5
    RESERVED_4 = 4
    DIODE_EXTERNAL_TRIGGER = 3
    RESERVED_2 = 2
    LASER_ACTIVE = 1
    LASER_ENABLED = 0

# The magic "everything is fine" code
dummy_status = 3075


def get_status(dummy_status):
    """Gets the status response of the laser"""
    raw_status = dummy_status
    return raw_status

def get_status_bit(raw_status, offset):
    """
    Gets specific bits from the laser status response.
    Pass it the response from the laser for status_response, and LASER_STATUS_BITS.whatever for the offset

    """
    status_bit_value = (raw_status >> offset & 1)
    return status_bit_value

# Report dummy_status
status = get_status(dummy_status)
print(f"dummy_status decimal is: {status}")
print(f"dummy_status binary is: {format(status, '#018b')}")

# Report bit w/0 using Enums
laser_enabled_bit = get_status_bit(status, 0)
print(f"checking the laser_enable_bit w/o using IntEnum {laser_enabled_bit}")

# Report bit using Enums
laser_enabled_bit = get_status_bit(status, LASER_STATUS_BITS.LASER_ENABLED)
print(f"checking the laser_enable_bit w/o using IntEnum {laser_enabled_bit}")

# Check if the Enums line up with proper bits
print("lets check all of the enum shifts")
for data in LASER_STATUS_BITS:
    laser_enabled_bit = get_status_bit(status, data.value)
    print('{:24} = {:2}. Bit value = {}'.format(data.name, data.value, laser_enabled_bit))
