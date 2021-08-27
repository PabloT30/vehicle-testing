from logging import log
import os
import can
import time
import csv
import sys

def get_moment():
    return time.strftime("%Y-%b-%d__%H_%M_%S", time.localtime())


def open_can_port():
    os.system('sudo ip link set can0 type can bitrate 500000')
    os.system('sudo ifconfig can0 up')
    can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native
    return can0


def close_can_port():
    os.system('sudo ifconfig can0 down')


def get_raw_can_message(can_socket, timeout):
    msg = can_socket.recv(10.0)
    if msg is not None:
        return msg
    else:
        print('Timeout occurred, no message.')
        return -1


def create_log_file(moment):
    headers = ["timestamp", "arbitration_id", "is_extended_id", "is_remote_frame",
                "is_error_frame", "channel", "dlc", "data", "is_fd", "bitrate_switch"]
    file_name = "raw_can_log_(" + moment + ").csv"
    log_file_write(file_name, headers)
    return file_name


def log_file_write(file_name, content):
    with open(file_name, 'a', newline='') as log_file:
        log_file_writer = csv.writer(log_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        log_file_writer.writerow(content)


def log_can_message(file_name, raw_can_message):
    msg = [raw_can_message.timestamp, raw_can_message.arbitration_id, raw_can_message.is_extended_id,
            raw_can_message.is_remote_frame, raw_can_message.is_error_frame, raw_can_message.channel,
            raw_can_message.dlc, raw_can_message.data, raw_can_message.is_fd, raw_can_message.bitrate_switch]
    log_file_write(file_name, msg)


def main():
    can_socket = open_can_port()
    moment = get_moment()
    file_name = create_log_file(moment)
    while(True):
        moment = get_moment()
        if moment[-5:-3] == "59":
            break
        raw_can_message = get_raw_can_message(can_socket, 10)
        if raw_can_message != -1:
            log_can_message(file_name, raw_can_message)
        else:
            break
    close_can_port()
    sys.exit(0)


if __name__ == '__main__':
    main()
