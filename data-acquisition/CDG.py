import nidaqmx
from nidaqmx.constants import BridgeConfiguration, BridgeElectricalUnits, BridgePhysicalUnits, BridgeUnits, ExcitationSource, ForceUnits
import statistics

cell_offsets = [17.20, -6.53, -11.02, 31.16]

def main():
    system = nidaqmx.system.System.local()
    ni_9219 = system.devices['cDAQ9188Mod7']
    
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_force_bridge_two_point_lin_chan(physical_channel="cDAQ9188Mod7/ai0", 
                                                                name_to_assign_to_channel="cell_no_1", 
                                                                min_val=-1000, 
                                                                max_val=1000, 
                                                                units=ForceUnits.POUNDS, 
                                                                bridge_config=BridgeConfiguration.FULL_BRIDGE, 
                                                                voltage_excit_source=ExcitationSource.INTERNAL, 
                                                                voltage_excit_val=2.5, 
                                                                nominal_bridge_resistance=350, 
                                                                first_electrical_val=0, 
                                                                second_electrical_val=3, 
                                                                electrical_units=BridgeElectricalUnits.M_VOLTS_PER_VOLT, 
                                                                first_physical_val=0, 
                                                                second_physical_val=1000, 
                                                                physical_units=BridgePhysicalUnits.POUNDS, 
                                                                custom_scale_name="")

        task.ai_channels.add_ai_force_bridge_two_point_lin_chan(physical_channel="cDAQ9188Mod7/ai1", 
                                                                name_to_assign_to_channel="cell_no_2", 
                                                                min_val=-1000, 
                                                                max_val=1000, 
                                                                units=ForceUnits.POUNDS, 
                                                                bridge_config=BridgeConfiguration.FULL_BRIDGE, 
                                                                voltage_excit_source=ExcitationSource.INTERNAL, 
                                                                voltage_excit_val=2.5, 
                                                                nominal_bridge_resistance=350, 
                                                                first_electrical_val=0, 
                                                                second_electrical_val=3, 
                                                                electrical_units=BridgeElectricalUnits.M_VOLTS_PER_VOLT, 
                                                                first_physical_val=0, 
                                                                second_physical_val=1000, 
                                                                physical_units=BridgePhysicalUnits.POUNDS, 
                                                                custom_scale_name="")

        task.ai_channels.add_ai_force_bridge_two_point_lin_chan(physical_channel="cDAQ9188Mod7/ai2", 
                                                                name_to_assign_to_channel="cell_no_3", 
                                                                min_val=-1000, 
                                                                max_val=1000, 
                                                                units=ForceUnits.POUNDS, 
                                                                bridge_config=BridgeConfiguration.FULL_BRIDGE, 
                                                                voltage_excit_source=ExcitationSource.INTERNAL, 
                                                                voltage_excit_val=2.5, 
                                                                nominal_bridge_resistance=350, 
                                                                first_electrical_val=0, 
                                                                second_electrical_val=3, 
                                                                electrical_units=BridgeElectricalUnits.M_VOLTS_PER_VOLT, 
                                                                first_physical_val=0, 
                                                                second_physical_val=1000, 
                                                                physical_units=BridgePhysicalUnits.POUNDS, 
                                                                custom_scale_name="")

        task.ai_channels.add_ai_force_bridge_two_point_lin_chan(physical_channel="cDAQ9188Mod7/ai3", 
                                                                name_to_assign_to_channel="cell_no_4", 
                                                                min_val=-1000, 
                                                                max_val=1000, 
                                                                units=ForceUnits.POUNDS, 
                                                                bridge_config=BridgeConfiguration.FULL_BRIDGE, 
                                                                voltage_excit_source=ExcitationSource.INTERNAL, 
                                                                voltage_excit_val=2.5, 
                                                                nominal_bridge_resistance=350, 
                                                                first_electrical_val=0, 
                                                                second_electrical_val=3, 
                                                                electrical_units=BridgeElectricalUnits.M_VOLTS_PER_VOLT, 
                                                                first_physical_val=0, 
                                                                second_physical_val=1000, 
                                                                physical_units=BridgePhysicalUnits.POUNDS, 
                                                                custom_scale_name="")

        # Run the following to get the offset.
        # data = task.read(number_of_samples_per_channel=4)
        # cell_offsets = [statistics.mean(data[0]),
        #                 statistics.mean(data[1]),
        #                 statistics.mean(data[2]),
        #                 statistics.mean(data[3])]
        # print(data)
        # print(cell_offsets)

        data = task.read(number_of_samples_per_channel=4)
        data = [statistics.mean(data[0]),
                        statistics.mean(data[1]),
                        statistics.mean(data[2]),
                        statistics.mean(data[3])]

        data = [round(elem, 2) for elem in data]
        data = [data[0] - cell_offsets[0],
                data[1] - cell_offsets[1],
                data[2] - cell_offsets[2],
                data[3] - cell_offsets[3]
                ]
        print(data)

        print(f"Peso celda No. 1 - Báscula No. 1: {round((data[0]) * 0.454, 2)} kg.")
        print(f"Peso celda No. 2 - Báscula No. 1: {round((data[1]) * 0.454, 2)} kg.")
        print(f"Peso celda No. 3 - Báscula No. 2: {round((data[2]) * 0.454, 2)} kg.")
        print(f"Peso celda No. 4 - Báscula No. 2: {round((data[3]) * 0.454, 2)} kg.")
        print(f"Peso báscula No. 1: {round((data[0] + data[1]) * 0.454, 2)} kg.")
        print(f"Peso báscula No. 2: {round((data[2] + data[3]) * 0.454, 2)} kg.")
        print(f"Peso total del sistema: {round((data[0] + data[1] + data[2] + data[3]) * 0.454, 2)} kg.")


if __name__ == '__main__':
    main()
