# diagnosis_rules.py

import json


class DiagnosisEngine:
    def __init__(self, user_info, symptoms):
        print('dataInRules', user_info, symptoms)
        self.user_info = user_info
        self.symptoms = symptoms
        self.diagnosis = []
        self.symptoms_diagnosis = []  # Added array to store specific symptom diagnosis

    def check_starting_problems(self):
        starting_problems = self.symptoms.get('starting_problems', [])
        if 'will_not_crank' in starting_problems:
            self.diagnosis.append("Check the battery, starter motor, and ignition switch.")
            self.symptoms_diagnosis.append("Possible issues: Bad battery, faulty starter motor, or problematic ignition switch.")
        if 'cranks_but_will_not_start' in starting_problems:
            self.diagnosis.append("Check for fuel delivery, ignition system function, and engine compression.")
            self.symptoms_diagnosis.append("Possible issues: Fuel delivery problem, ignition system malfunction, or low engine compression.")
        if 'starts_then_dies' in starting_problems:
            self.diagnosis.append("Inspect idle control system and potential vacuum leaks.")
            self.symptoms_diagnosis.append("Possible issues: Idle control system failure or vacuum leaks.")

    def check_engine_behavior(self):
        engine_behavior = self.symptoms.get('engine_behavior', [])
        if 'engine_misfires' in engine_behavior:
            self.diagnosis.append("Inspect spark plugs, ignition wires, and coil packs.")
            self.symptoms_diagnosis.append("Possible issues: Worn-out spark plugs, faulty ignition wires, or malfunctioning coil packs.")
        if 'engine_knocks_under_load' in engine_behavior:
            self.diagnosis.append("Inspect for incorrect fuel octane, carbon deposits, or faulty spark plugs.")
            self.symptoms_diagnosis.append("Possible issues: Wrong fuel octane, carbon buildup, or defective spark plugs.")
        if 'overheating_engine' in engine_behavior:
            self.diagnosis.append("Check for coolant level, thermostat operation, and radiator condition.")
            self.symptoms_diagnosis.append("Possible issues: Low coolant level, thermostat malfunction, or radiator issues.")

    def check_transmission_problems(self):
        transmission_problems = self.symptoms.get('transmission_problems', [])
        if 'slipping_transmission' in transmission_problems:
            self.diagnosis.append("Check transmission fluid level and condition, consider a fluid change or filter replacement.")
            self.symptoms_diagnosis.append("Possible issues: Low transmission fluid, dirty fluid, or worn-out transmission filter.")
        if 'hard_shifts' in transmission_problems:
            self.diagnosis.append("Inspect transmission mounts, fluid level, and shift solenoids.")
            self.symptoms_diagnosis.append("Possible issues: Damaged transmission mounts, low fluid level, or faulty shift solenoids.")

    def check_idling_conditions(self):
        idling_conditions = self.symptoms.get('idling_conditions', [])
        if 'rough_idle' in idling_conditions:
            self.diagnosis.append("Check for vacuum leaks, faulty spark plugs, or dirty fuel injectors.")
            self.symptoms_diagnosis.append("Possible issues: Vacuum leaks, worn-out spark plugs, or clogged fuel injectors.")
        if 'fluctuating_idle' in idling_conditions:
            self.diagnosis.append("Inspect the throttle body and idle air control valve.")
            self.symptoms_diagnosis.append("Possible issues: Dirty throttle body or malfunctioning idle air control valve.")

    def check_running_conditions(self):
        running_conditions = self.symptoms.get('running_conditions', [])
        if 'lacks_power' in running_conditions:
            self.diagnosis.append("Check the exhaust system for blockages and the fuel system for proper pressure.")
            self.symptoms_diagnosis.append("Possible issues: Exhaust system blockage or fuel system pressure problems.")
        if 'engine_hesitation' in running_conditions:
            self.diagnosis.append("Check for dirty fuel injectors, faulty ignition components, or clogged air filters.")
            self.symptoms_diagnosis.append("Possible issues: Dirty fuel injectors, defective ignition components, or clogged air filters.")

    def check_electrical_system(self):
        electrical_system = self.symptoms.get('electrical_system', [])
        if 'battery_drains_quickly' in electrical_system:
            self.diagnosis.append("Perform an electrical system test, including the battery and alternator.")
            self.symptoms_diagnosis.append("Possible issues: Battery or alternator issues leading to quick drainage.")
        if 'headlights_dim' in electrical_system:
            self.diagnosis.append("Inspect the charging system and battery health.")
            self.symptoms_diagnosis.append("Possible issues: Charging system problems or deteriorating battery health.")

    def check_braking_system(self):
        braking_system = self.symptoms.get('braking_system', [])
        if 'squealing_brakes' in braking_system:
            self.diagnosis.append("Check brake pads for wear and rotor surface for unevenness.")
            self.symptoms_diagnosis.append("Possible issues: Worn-out brake pads or uneven rotor surface.")
        if 'brake_pedal_soft' in braking_system:
            self.diagnosis.append("Inspect for brake fluid leaks and brake line condition.")
            self.symptoms_diagnosis.append("Possible issues: Brake fluid leaks or compromised brake lines.")

    def check_steering_suspension(self):
        steering_suspension = self.symptoms.get('steering_suspension', [])
        if 'car_pulls_to_one_side' in steering_suspension:
            self.diagnosis.append("Check wheel alignment and tire pressure.")
            self.symptoms_diagnosis.append("Possible issues: Wheel misalignment or incorrect tire pressure.")
        if 'steering_wheel_vibration' in steering_suspension:
            self.diagnosis.append("Inspect wheel balance, alignment, and suspension components.")
            self.symptoms_diagnosis.append("Possible issues: Imbalanced wheels, misalignment, or faulty suspension components.")

    def check_exhaust_system(self):
        exhaust_system = self.symptoms.get('exhaust_system', [])
        if 'exhaust_smoke' in exhaust_system:
            self.diagnosis.append("Check engine oil level, head gasket integrity, and turbocharger operation.")
            self.symptoms_diagnosis.append("Possible issues: Low engine oil, damaged head gasket, or malfunctioning turbocharger.")
        if 'loud_exhaust_noise' in exhaust_system:
            self.diagnosis.append("Inspect for holes or disconnections in the exhaust piping.")
            self.symptoms_diagnosis.append("Possible issues: Exhaust system leaks, holes, or disconnections.")

    def check_fuel_system(self):
        fuel_system = self.symptoms.get('fuel_system', [])
        if 'poor_fuel_economy' in fuel_system:
            self.diagnosis.append("Check for clogged fuel injectors, fuel filter, or oxygen sensor.")
            self.symptoms_diagnosis.append("Possible issues: Clogged fuel injectors, dirty fuel filter, or malfunctioning oxygen sensor.")
        if 'fuel_smell' in fuel_system:
            self.diagnosis.append("Inspect the fuel lines and connections for leaks.")
            self.symptoms_diagnosis.append("Possible issues: Fuel lines or connections leaking.")

    def check_cooling_system(self):
        cooling_system = self.symptoms.get('cooling_system', [])
        if 'coolant_leak' in cooling_system:
            self.diagnosis.append("Inspect the radiator, hoses, and water pump for leaks.")
            self.symptoms_diagnosis.append("Possible issues: Radiator, hoses, or water pump leaks.")
        if 'high_temperature' in cooling_system:
            self.diagnosis.append("Check for low coolant level, faulty thermostat, or a malfunctioning cooling fan.")
            self.symptoms_diagnosis.append("Possible issues: Low coolant level, thermostat malfunction, or cooling fan issues.")

    def check_air_conditioning(self):
        air_conditioning = self.symptoms.get('air_conditioning', [])
        if 'ac_not_cooling' in air_conditioning:
            self.diagnosis.append("Inspect refrigerant level, compressor operation, and cooling system components.")
            self.symptoms_diagnosis.append("Possible issues: Low refrigerant level, compressor malfunction, or issues with cooling system components.")
        if 'ac_blowing_hot_air' in air_conditioning:
            self.diagnosis.append("Check for low refrigerant, compressor issues, or a malfunctioning blend door.")
            self.symptoms_diagnosis.append("Possible issues: Low refrigerant, compressor problems, or malfunctioning blend door.")

    def run_diagnosis(self):
        self.check_starting_problems()
        self.check_engine_behavior()
        self.check_transmission_problems()
        self.check_idling_conditions()
        self.check_running_conditions()
        self.check_electrical_system()
        self.check_braking_system()
        self.check_steering_suspension()
        self.check_exhaust_system()
        self.check_fuel_system()
        self.check_cooling_system()
        self.check_air_conditioning()

        if not self.diagnosis:
            self.diagnosis.append("No issues detected based on the symptoms provided.")
        return {'user_info': self.user_info, 'diagnosis': self.diagnosis, 'symptoms_diagnosis': self.symptoms_diagnosis}

def diagnose(user_info, symptoms):
    # If symptoms is already a dictionary, use it directly
    if isinstance(symptoms, dict):
        symptoms_dict = symptoms
    else:
        # Assuming symptoms is a JSON string, parse it
        try:
            symptoms_dict = json.loads(symptoms)
        except json.JSONDecodeError as e:
            print(f"Error decoding symptoms JSON: {e}")
            return {"error": "Error decoding symptoms JSON"}

    engine = DiagnosisEngine(user_info=user_info, symptoms=symptoms_dict)
    return engine.run_diagnosis()
