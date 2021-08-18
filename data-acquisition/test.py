import nidaqmx

def main():
    system = nidaqmx.system.System.local()
    print(system.driver_version)  # DriverVersion(major_version=20, minor_version=0, update_version=0)

if __name__ == '__main__':
    main()
