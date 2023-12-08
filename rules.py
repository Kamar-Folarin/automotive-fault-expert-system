class AutomotiveExpertSystem:
    def query_fault(self, ignition, engine_crank, enough_fuel, ignition_off, engine_not_crank, not_enough_fuel, temperature, liquid_leakage, ac_blowing_hot_air,**additional_inputs):
        # Check if ignition is On
        if ignition_off:
            return {'message': 'Ignition is not On. Please turn the ignition On and try again.'}

        # Check if the engine is cranking
        if engine_not_crank:
            return {'message': 'Engine is not cranking. Please check the engine and try again.'}

        # Check if there's enough fuel
        if not_enough_fuel:
            return {'message': 'Not enough fuel. Refuel and try again.'}

        result_rules = {}

        # Rule 1
        if ignition and not engine_crank:
            result_rules['rule1'] = 'check_battery_and_terminals'

        # Rule 2
        if 'rule1' in result_rules and not engine_crank:
            result_rules['rule2'] = 'confirm_fuel_gas_level'

        # Rule 3
        if 'rule1' in result_rules and enough_fuel and not engine_crank:
            result_rules['rule3'] = 'check_switching_operation'

        # Rule 4
        if 'rule1' in result_rules and 'rule2' in result_rules and 'rule3' in result_rules and not engine_crank:
            result_rules['rule4'] = 'contact_experienced_personnel'

        # Rule 5
        if 'rule1' in result_rules and 'rule2' in result_rules and not engine_crank:
            result_rules['rule5'] = 'change_fuel_pump'

        # Rule 6
        if 'rule5' in result_rules and not engine_crank:
            result_rules['rule6'] = 'check_and_change_fuel_pump_fuse'

        # Rule 7
        if 'rule6' in result_rules and not engine_crank:
            result_rules['rule7'] = 'replace_slow_running_jet_with_help'

        # Rule 8
        if ignition and not engine_crank and 'rule1' not in result_rules:
            result_rules['rule8'] = 'check_vehicle_battery'

        # Rule 9
        if 'rule8' in result_rules and not engine_crank:
            result_rules['rule9'] = 'charge_battery'

        # Rule 10
        if 'rule8' in result_rules and 'rule9' in result_rules and not engine_crank:
            result_rules['rule10'] = 'check_test_starter'

        # Rule 11
        if 'rule10' in result_rules and not engine_crank:
            result_rules['rule11'] = 'replace_battery'

        # Rule 12
        if 'rule8' in result_rules and 'rule9' in result_rules and 'rule10' in result_rules and not engine_crank:
            result_rules['rule12'] = 'replace_battery_and_starter_with_help'

        # Rule 13
        if engine_crank and 'rule12' not in result_rules:
            result_rules['rule13'] = 'check_spark_plug_and_contact_set'

        # Rule 14
        if 'rule13' in result_rules and engine_crank:
            result_rules['rule14'] = 'contact_experienced_personnel_for_major_fault'

        # Rule 15
        if enough_fuel and engine_crank and 'rule14' not in result_rules:
            result_rules['rule15'] = 'check_overheating_water_level_and_radiator_fan'

        # Rule 16
        if 'rule15' in result_rules and engine_crank:
            result_rules['rule16'] = 'stop_vehicle_cool_engine'

        # Rule 17
        if 'rule15' in result_rules and 'rule16' in result_rules and engine_crank:
            result_rules['rule17'] = 'contact_experienced_personnel_for_major_fault'

        # Rule 18
        if 'rule15' in result_rules and not engine_crank:
            result_rules['rule18'] = 'contact_experienced_personnel_for_major_fault'

        # Rule 19
        if 'rule15' in result_rules and 'rule16' in result_rules and 'rule17' in result_rules and engine_crank:
            result_rules['rule19'] = 'check_engine_oil_leak_from_gasket_seals_and_connections'

        # Rule 20
        if ignition and engine_crank and 'rule19' not in result_rules:
            result_rules['rule20'] = 'check_exhaust_smoke_color'

        # Rule 21
        if 'rule20' in result_rules and engine_crank:
            result_rules['rule21'] = 'seek_assistance_for_black_or_gray_smoke'

        # Rule 22
        if 'rule20' in result_rules and engine_crank:
            result_rules['rule22'] = 'seek_assistance_for_blue_smoke'

        # Rule 23
        if 'rule20' in result_rules and engine_crank:
            result_rules['rule23'] = 'seek_assistance_for_white_smoke'

            # Rule 24
        if 'rule23' in result_rules and engine_crank:
            result_rules['rule24'] = 'seek_assistance_for_engine_backfiring'

        # Rule 25
        if 'rule23' in result_rules and engine_crank:
            result_rules['rule25'] = 'seek_assistance_for_engine_surging'

        # Rule 26
        if ignition and engine_crank and 'rule25' not in result_rules:
            result_rules['rule26'] = 'check_throttle_position_sensor'

        # Rule 27
        if 'rule26' in result_rules and engine_crank:
            result_rules['rule27'] = 'seek_assistance_for_faulty_mass_airflow_sensor'

        # Rule 28
        if 'rule26' in result_rules and engine_crank:
            result_rules['rule28'] = 'seek_assistance_for_faulty_idle_air_control_valve'

        # Rule 29
        if ignition and engine_crank and 'rule28' not in result_rules:
            result_rules['rule29'] = 'check_fuel_pressure'

        # Rule 30
        if 'rule29' in result_rules and engine_crank:
            result_rules['rule30'] = 'seek_assistance_for_faulty_fuel_pump_relay'

        # Rule 31
        if 'rule23' in result_rules and engine_crank:
            result_rules['rule31'] = 'seek_assistance_for_excessive_engine_noise'

        # Rule 32
        if 'rule23' in result_rules and engine_crank:
            result_rules['rule32'] = 'seek_assistance_for_engine_knocking'

        # Rule 33
        if ignition and engine_crank and 'rule32' not in result_rules:
            result_rules['rule33'] = 'check_exhaust_system_for_rattling'

        # Rule 34
        if enough_fuel and engine_crank and 'rule33' not in result_rules:
            result_rules['rule34'] = 'check_air_filter_for_clogging'

        # Rule 35
        if ignition and engine_crank and 'rule34' not in result_rules:
            result_rules['rule35'] = 'inspect_distributor_and_ignition_coil'

        # Rule 36
        if 'rule35' in result_rules and engine_crank:
            result_rules['rule36'] = 'seek_assistance_for_faulty_ignition_module'

        # Rule 37
        if 'rule35' in result_rules and engine_crank:
            result_rules['rule37'] = 'seek_assistance_for_faulty_spark_plug_wires'

        # Rule 38
        if 'rule35' in result_rules and engine_crank:
            result_rules['rule38'] = 'seek_assistance_for_faulty_distributor_cap'

        # Rule 39
        if ignition and engine_crank and 'rule38' not in result_rules:
            result_rules['rule39'] = 'check_engine_timing'

        # Rule 40
        if 'rule39' in result_rules and engine_crank:
            result_rules['rule40'] = 'seek_assistance_for_faulty_crankshaft_position_sensor'

        # Rule 41
        if ignition and engine_crank and 'rule40' not in result_rules:
            result_rules['rule41'] = 'check_exhaust_system_for_hissing'

        # Rule 42
        if 'rule41' in result_rules and engine_crank:
            result_rules['rule42'] = 'seek_assistance_for_exhaust_leaks'

        # Rule 43
        if ignition and engine_crank and 'rule42' not in result_rules:
            result_rules['rule43'] = 'check_fuel_injectors_for_clogging'

        # Rule 44
        if 'rule43' in result_rules and engine_crank:
            result_rules['rule44'] = 'seek_assistance_for_faulty_fuel_pressure_regulator'

        # Rule 45
        if 'rule43' in result_rules and engine_crank:
            result_rules['rule45'] = 'seek_assistance_for_faulty_fuel_injectors'

        # Rule 46
        if ignition and engine_crank and 'rule45' not in result_rules:
            result_rules['rule46'] = 'check_cooling_system_for_leaks'

        # Rule 47
        if 'rule46' in result_rules and engine_crank:
            result_rules['rule47'] = 'seek_assistance_for_faulty_water_pump'

        # Rule 48
        if 'rule46' in result_rules and engine_crank:
            result_rules['rule48'] = 'seek_assistance_for_faulty_thermostat'

        # Rule 49
        if 'rule46' in result_rules and engine_crank:
            result_rules['rule49'] = 'seek_assistance_for_faulty_radiator_cap'

        # Rule 50
        if ignition and engine_crank and 'rule49' not in result_rules:
            result_rules['rule50'] = 'check_engine_oil_level_and_condition'

        # Rule 51
        if temperature > 90 and 'rule50' not in result_rules:
            result_rules['rule51'] = 'check_coolant_level_and_radiator_condition'

        # Rule 52
        if 'rule51' in result_rules and temperature > 100:
            result_rules['rule52'] = 'check_thermostat_operation'

        # Rule 53
        if liquid_leakage and 'rule52' not in result_rules:
            result_rules['rule53'] = 'inspect_underneath_for_fluid_leaks'

        # Rule 54
        if 'rule53' in result_rules and liquid_leakage:
            result_rules['rule54'] = 'check_power_steering_fluid_level'

        # Rule 55
        if ac_blowing_hot_air and 'rule54' not in result_rules:
            result_rules['rule55'] = 'check_ac_refrigerant_level_and_compressor_operation'

        # Rule 56
        if 'rule55' in result_rules and ac_blowing_hot_air:
            result_rules['rule56'] = 'seek_assistance_for_faulty_ac_condenser'

        # Rule 57
        if 'rule55' in result_rules and ac_blowing_hot_air:
            result_rules['rule57'] = 'seek_assistance_for_faulty_ac_blower_motor'

        # Rule 58
        if ignition and engine_crank and 'rule57' not in result_rules:
            result_rules['rule58'] = 'check_dashboard_temperature_indicator'

        # Rule 59
        if 'rule58' in result_rules and temperature > 80:
            result_rules['rule59'] = 'seek_assistance_for_faulty_cabin_temperature_sensor'

        # Rule 60
        if 'rule58' in result_rules and temperature > 80:
            result_rules['rule60'] = 'seek_assistance_for_faulty_heater_core'
  

        return result_rules
