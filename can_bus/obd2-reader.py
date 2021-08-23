# https://python-obd.readthedocs.io/en/latest/
# https://github.com/brendan-w/python-OBD
import obd  # 

# print(obd.OBD)            # main OBD connection class
# print(obd.Async)          # asynchronous OBD connection class
# print(obd.commands)       # command tables
# print(obd.Unit)           # unit tables (a Pint UnitRegistry)
# print(obd.OBDStatus)      # enum for connection status
# print(obd.scan_serial)    # util function for manually scanning for OBD adapters
# print(obd.OBDCommand)     # class for making your own OBD Commands
# print(obd.ECU)            # enum for marking which ECU a command should listen to
# print(obd.logger)        # the OBD module's root logger (for debug)

# create connection with ELM327 Bluetooth Dongle.
ports = obd.scan_serial()      # return list of valid USB or RF ports
print(ports)                    # ['/dev/rfcomm0']
connection = obd.OBD(portstr=ports[0],
                    baudrate=None,
                    protocol=None,
                    fast=False,  # True by default.
                    timeout=1,  # 0.1 by default.
                    check_voltage=False)  # True by default.

# cmd = obd.commands.SPEED # select an OBD command (sensor)
cmd = obd.commands.ELM_VERSION # select an OBD command (sensor)
response = connection.query(cmd) # send the command, and parse the response

print(response.value) # returns unit-bearing values thanks to Pint
# print(response.value.to("mph")) # user-friendly unit conversions

print(connection.status())
print(connection.port_name())
print(connection.protocol_name())

# with obd.OBD() as connection:
#     print("...")
#     print(obd.OBDStatus.NOT_CONNECTED)
#     print(obd.OBDStatus.ELM_CONNECTED)
#     print(obd.OBDStatus.OBD_CONNECTED)
#     print(obd.OBDStatus.CAR_CONNECTED)
#     print("...")
#     print(connection.status())
