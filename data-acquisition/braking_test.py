# Project: Braking test data acquisition program.
# Author: Pablo Torres | @pablot30
# Date: 2020-04-24
# Version: 1.0
# Description: This program is used to acquire sensors data from the braking test.
#              by using own sensors, and a data acquisition system cRIO, as well as
#              reading the car CAN interfaces. Moreover it uploads the data to a 
#              cloud database in GCP.
#
# Variables to measure:
#  Own sensors.
#   - Velocity:
#       - RPM and kmh using an inductive sensor on the fifth wheel.
#       - RPM and kmh using a pitot tube.
#   - Braking force:
#       - Force on the brake pedal using a load cell.
#   - Temperature:
#       - Temperature on each vehicle wheel using infrared sensors.
#   - Position:
#       - Longitude, latitude and height using a GPS.
#  - Acceleration:
#       - Acceleration in x, y and z axis using an accelerometer.
#
# Car sensors through the CAN interface using the OBD2 to Bluetooth connector.
#   - RPM.
#
# Notes:
#   - Please find project documentation in the following link:
#       https://drive.google.com/drive/folders/1JkUUfGPfUcidrIRiiRFg3Pv5doAyZ5X9?usp=sharing
#  - Please find project connection diagram in the following link:
#       https://drive.google.com/drive/folders/1JkUUfGPfUcidrIRiiRFg3Pv5doAyZ5X9?usp=sharing


import re
import nidaqmx
import math
import nidaqmx.constants as nic
import numpy as np
import obd
from time import time
import serial
import time
import csv
import multiprocessing as mp
from datetime import datetime


def connect_to_car():
    # create car_connection with ELM327 Bluetooth Dongle.
    # https://python-obd.readthedocs.io/en/latest/
    # https://github.com/brendan-w/python-OBD
    ports = obd.scan_serial()      # return list of valid USB or RF ports
    car_connection = obd.OBD(portstr=ports[0],
                        baudrate=None,
                        protocol=None,
                        fast=False,  # True by default.
                        timeout=1,  # 0.1 by default.
                        check_voltage=False)  # True by default.
    if car_connection.is_connected():
        print("Connected to car.")
        return car_connection
    else:
        print("Could not connect to car.")
    return None


def disconnect_from_car(car_connection):
    car_connection.close()
    print("Disconnected from car.")

# Nissan Tida 2010.
def read_car(car_connection, parameter):
    if parameter == "RPM":
        return car_connection.query(obd.commands.RPM).value.magnitude
    elif parameter == "SPEED":
        return car_connection.query(obd.commands.SPEED).value.magnitude
    elif parameter == "FUEL_STATUS":
        return car_connection.query(obd.commands.FUEL_STATUS).value.magnitude
    elif parameter == "ENGINE_LOAD":
        return car_connection.query(obd.commands.ENGINE_LOAD).value.magnitude
    elif parameter == "COOLANT_TEMP":
        return car_connection.query(obd.commands.COOLANT_TEMP).value.magnitude
    elif parameter == "FUEL_PRESSURE":
        return car_connection.query(obd.commands.FUEL_PRESSURE).value.magnitude
    elif parameter == "INTAKE_PRESSURE":
        return car_connection.query(obd.commands.INTAKE_PRESSURE).value.magnitude
    elif parameter == "MAF":
        return car_connection.query(obd.commands.MAF).value.magnitude
    elif parameter == "THROTTLE_POS":
        return car_connection.query(obd.commands.THROTTLE_POS).value.magnitude
    elif parameter == "AIR_STATUS":
        return car_connection.query(obd.commands.AIR_STATUS).value.magnitude
    elif parameter == "O2_SENSORS":
        return car_connection.query(obd.commands.O2_SENSORS).value.magnitude
    elif parameter == "RUN_TIME":
        return car_connection.query(obd.commands.RUN_TIME).value.magnitude
    elif parameter == "ABSOLUTE_LOAD":
        return car_connection.query(obd.commands.ABSOLUTE_LOAD).value.magnitude
    elif parameter == "RELATIVE_THROTTLE_POS":
        return car_connection.query(obd.commands.RELATIVE_THROTTLE_POS).value.magnitude
    elif parameter == "AMBIANT_AIR_TEMP":
        return car_connection.query(obd.commands.AMBIANT_AIR_TEMP).value.magnitude
    elif parameter == "THROTTLE_POS_B":
        return car_connection.query(obd.commands.THROTTLE_POS_B).value.magnitude
    elif parameter == "THROTTLE_POS_C":
        return car_connection.query(obd.commands.THROTTLE_POS_B).value.magnitude
    elif parameter == "ACCELERATOR_POS_D":
        return car_connection.query(obd.commands.ACCELERATOR_POS_D).value.magnitude
    elif parameter == "ACCELERATOR_POS_E":
        return car_connection.query(obd.commands.ACCELERATOR_POS_E).value.magnitude
    elif parameter == "ACCELERATOR_POS_F":
        return car_connection.query(obd.commands.ACCELERATOR_POS_F).value.magnitude
    elif parameter == "THROTTLE_ACTUATOR":
        return car_connection.query(obd.commands.THROTTLE_ACTUATOR).value.magnitude
    elif parameter == "FUEL_TYPE":
        return car_connection.query(obd.commands.FUEL_TYPE).value.magnitude
    elif parameter == "HYBRID_BATTERY_REMAINING":
        return car_connection.query(obd.commands.HYBRID_BATTERY_REMAINING).value.magnitude
    elif parameter == "OIL_TEMP":
        return car_connection.query(obd.commands.OIL_TEMP).value.magnitude


def daq_task_init():
    task = nidaqmx.Task()
    # TODO configure task measurements.

    # Configure wheel temperature measurements.
    # NI-9201 channel 0.
    task.ai_channels.add_ai_voltage_chan(physical_channel="cDAQ9188Mod1/ai0", 
                                        name_to_assign_to_channel="front_left_wheel_temperature", 
                                        terminal_config=nic.TerminalConfiguration.DEFAULT, 
                                        min_val=0.0, 
                                        max_val=5.0, 
                                        units=nic.VoltageUnits.VOLTS, 
                                        custom_scale_name='')
    
    # NI-9201 channel 1.
    task.ai_channels.add_ai_voltage_chan(physical_channel="cDAQ9188Mod1/ai1", 
                                        name_to_assign_to_channel="rear_right_wheel_temperature", 
                                        terminal_config=nic.TerminalConfiguration.DEFAULT, 
                                        min_val=0.0, 
                                        max_val=5.0, 
                                        units=nic.VoltageUnits.VOLTS, 
                                        custom_scale_name='')
    
    # NI-9201 channel 2.
    task.ai_channels.add_ai_voltage_chan(physical_channel="cDAQ9188Mod1/ai2", 
                                        name_to_assign_to_channel="front_left_wheel_temperature", 
                                        terminal_config=nic.TerminalConfiguration.DEFAULT, 
                                        min_val=0.0, 
                                        max_val=5.0, 
                                        units=nic.VoltageUnits.VOLTS, 
                                        custom_scale_name='')
    
    # NI-9201 channel 3.
    task.ai_channels.add_ai_voltage_chan(physical_channel="cDAQ9188Mod1/ai3", 
                                        name_to_assign_to_channel="rear_right_wheel_temperature", 
                                        terminal_config=nic.TerminalConfiguration.DEFAULT, 
                                        min_val=0.0, 
                                        max_val=5.0, 
                                        units=nic.VoltageUnits.VOLTS, 
                                        custom_scale_name='')
    
    # TODO Configure fifth wheel speed measurements.
    # NI-9201 Nr. 2 channel 0.
    task.ai_channels.add_ai_voltage_chan(physical_channel="cDAQ9188Mod2/ai0", 
                                        name_to_assign_to_channel="fifth_wheel_velocity", 
                                        terminal_config=nic.TerminalConfiguration.DEFAULT, 
                                        min_val=0.0, 
                                        max_val=5.0, 
                                        units=nic.VoltageUnits.VOLTS, 
                                        custom_scale_name='')

    # TODO scale brake pedal load cell measurements to kgf.
    # NI-9219 channel 0.
    # Note: connect to external supply.
    task.ai_channels.add_ai_voltage_chan(physical_channel="cDAQ9188Mod3/ai0", 
                                    name_to_assign_to_channel="brake_pedal_load_cell_force", 
                                    terminal_config=nic.TerminalConfiguration.DEFAULT, 
                                    min_val=-1.0, 
                                    max_val=1.0, 
                                    units=nic.VoltageUnits.VOLTS, 
                                    custom_scale_name='')

    # TODO configure acceleration sensor measurements.
    # NI-9230 channel 0  for X axis.
    task.ai_channels.add_ai_voltage_chan(physical_channel="cDAQ9188Mod4/ai0", 
                                    name_to_assign_to_channel="brake_pedal_load_cell_force_x_axis", 
                                    terminal_config=nic.TerminalConfiguration.DEFAULT, 
                                    min_val=-1.0, 
                                    max_val=1.0, 
                                    units=nic.VoltageUnits.VOLTS, 
                                    custom_scale_name='')

    # NI-9230 channel 1  for Y axis.
    task.ai_channels.add_ai_voltage_chan(physical_channel="cDAQ9188Mod4/ai1", 
                                name_to_assign_to_channel="brake_pedal_load_cell_force_y_axis", 
                                terminal_config=nic.TerminalConfiguration.DEFAULT, 
                                min_val=-1.0, 
                                max_val=1.0, 
                                units=nic.VoltageUnits.VOLTS, 
                                custom_scale_name='')

    # NI-9230 channel 2  for Z axis.
    task.ai_channels.add_ai_voltage_chan(physical_channel="cDAQ9188Mod4/ai1", 
                                name_to_assign_to_channel="brake_pedal_load_cell_force_y_axis", 
                                terminal_config=nic.TerminalConfiguration.DEFAULT, 
                                min_val=-1.0, 
                                max_val=1.0, 
                                units=nic.VoltageUnits.VOLTS, 
                                custom_scale_name='')


    # TODO Configure sampling rate.
    # Requirements:
    # Temperature sensor Texense IRN-2-V-500-5. Response time: 50 ms | 20 Hz.
    # Brake pedal load cell Futek LTH 300. Response time: N/A ¿?. TODO define response time.
    # Fifth wheel speed sensor NI-9201. Response time: S ¿?. TODO define response time.
    # S = (V * n) / (2 * pi * R) where V is vehicle speed im kmh, n is the number of trigger wheel holes, and R is the wheel radius.
    # 
    task.timing.cfg_samp_clk_timing(10, 
                                    source="", 
                                    active_edge=nic.Edge.RISING, 
                                    sample_mode=nic.AcquisitionType.FINITE, 
                                    samps_per_chan=50)

    return task


def read_gps():
    '''Return data from gps in format: 
    ['time_stamp', 'latitude', 'north/south', 'longitude', 
    'east/west', 'speed_kmh', 'true_course', 'date_stamp', 
    'variation', 'east/west']'''
    
    with serial.Serial("/dev/ttyUSB0", baudrate=4800) as ser:
        line = str(ser.readline())  # read a '\n' terminated line.
        data = line.split(',')
        if data[0] == "b'$GPRMC":
            if data[2] == 'A':
                return data


def main():
    car_connection = connect_to_car()
    daq_task = daq_task_init()
    
    gps_data = read_gps()
    car_data = read_car(car_connection)
    data = daq_task.read(number_of_samples_per_channel=50)


    # TODO parallalize measurements from OBD2, DAQ and GPS using multiprocessing module.


if __name__ == "__main__":
    main()
