import nidaqmx


def main():
    system = nidaqmx.system.System.local()
    print(system.driver_version)  # DriverVersion(major_version=20, minor_version=0, update_version=0)
    for device in system.devices:
        print(device)
    # Device(name=cDAQ9188)
    # Device(name=cDAQ9188Mod1)
    # Device(name=cDAQ9188Mod2)
    # Device(name=cDAQ9188Mod3)
    # Device(name=cDAQ9188Mod4)
    # Device(name=cDAQ9188Mod5)
    # Device(name=cDAQ9188Mod6)
    # Device(name=cDAQ9188Mod7)
    # Device(name=cDAQ9188Mod8)

    # help(system)
    ni_9219 = system.devices['cDAQ9188Mod8']
    # help(ni_9219)
    print(ni_9219.ai_meas_types)  # [<UsageTypeAI.CURRENT: 10134>, <UsageTypeAI.RESISTANCE: 10278>,
    # <UsageTypeAI.STRAIN_STRAIN_GAGE: 10300>, <UsageTypeAI.TEMPERATURE_RTD: 10301>,
    # <UsageTypeAI.TEMPERATURE_THERMOCOUPLE: 10303>, <UsageTypeAI.TEMPERATURE_BUILT_IN_SENSOR: 10311>,
    # <UsageTypeAI.VOLTAGE: 10322>, <UsageTypeAI.VOLTAGE_CUSTOM_WITH_EXCITATION: 10323>, <UsageTypeAI.FORCE_BRIDGE:
    # 15899>, <UsageTypeAI.PRESSURE_BRIDGE: 15902>, <UsageTypeAI.TORQUE_BRIDGE: 15905>, <UsageTypeAI.BRIDGE: 15908>,
    # <UsageTypeAI.ROSETTE_STRAIN_GAGE: 15980>]
    for phy_channel in ni_9219.ai_physical_chans:
        print(phy_channel)
    # PhysicalChannel(name=cDAQ9188Mod8/ai0)
    # PhysicalChannel(name=cDAQ9188Mod8/ai1)
    # PhysicalChannel(name=cDAQ9188Mod8/ai2)
    # PhysicalChannel(name=cDAQ9188Mod8/ai3)
    print(ni_9219.ai_bridge_rngs)  # [-0.0078125, 0.0078125, -0.0625, 0.0625, -0.5, 0.5]
    print(ni_9219.ai_samp_modes)  # [<AcquisitionType.FINITE: 10178>, <AcquisitionType.CONTINUOUS: 10123>]
    print(ni_9219.ai_simultaneous_sampling_supported)  # True
    print(ni_9219.ai_voltage_int_excit_discrete_vals)  # [0.0, 2.5, 5.0]
    print(ni_9219.compact_daq_chassis_device)  # Device(name=cDAQ9188)
    print(ni_9219.compact_daq_slot_num)  # 8
    print(ni_9219.dev_serial_num)  # 27056357
    print(ni_9219.product_category)  # ProductCategory.C_SERIES_MODULE
    print(ni_9219.product_num)  # 29386
    print(ni_9219.product_type)  # NI_9219
    print(ni_9219.self_test_device())

    with nidaqmx.Task() as task:
        # task.ai_channels.add_ai_voltage_chan("cDAQ9188Mod8/ai3")
        # data = task.read(number_of_samples_per_channel=4)
        # print(data)

        task.ai_channels.add_ai_force_bridge_two_point_lin_chan(physical_channel="cDAQ9188Mod8/ai3",
                                                                min_val=0,
                                                                max_val=1000,
                                                                first_electrical_val=0.0,
                                                                second_electrical_val=3.0,
                                                                first_physical_val=0.0,
                                                                second_physical_val=1000.0)
        # data = task.read(number_of_samples_per_channel=4)
        data = task.read()
        print(data)


if __name__ == '__main__':
    main()
