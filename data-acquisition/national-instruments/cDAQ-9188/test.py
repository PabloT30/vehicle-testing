import nidaqmx

# https://www.ni.com/es-co/support/downloads/drivers/download.ni-linux-device-drivers.html#350003
# https://www.ni.com/es-co/support/documentation/supplemental/18/downloading-and-installing-ni-driver-software-on-linux-desktop.html
# https://www.ni.com/pdf/manuals/378353d.html
# https://www.ni.com/pdf/manuals/378353a.html
# https://nidaqmx-python.readthedocs.io/en/latest/
# https://github.com/ni/nidaqmx-python

# https://www.ni.com/es-co/support/documentation/supplemental/06/getting-started-with-ni-daqmx--main-page.html
# https://www.ni.com/es-co/support/documentation/supplemental/06/learn-10-functions-in-ni-daqmx-and-handle-80-percent-of-your-dat.html
# https://knowledge.ni.com/KnowledgeArticleDetails?id=kA03q000000x0QHCAY&l=es-CO
# https://documentation.help/NI-DAQmx/
# https://nidaqmx-python.readthedocs.io/en/latest/
# https://www.ni.com/getting-started/labview-basics/esa/
# https://www.ni.com/getting-started/labview-basics/esa/debug
# https://www.ni.com/getting-started/esa/begin-application.htm
# http://www.learnni.com/
# https://univalle.electude.com/

def main():
    system = nidaqmx.system.System.local()
    print(system.driver_version)  # DriverVersion(major_version=20, minor_version=0, update_version=0)

if __name__ == '__main__':
    main()
