# app.py
from flask import Flask, render_template, request
from rule_description import RULE_DESCRIPTIONS
from rules import AutomotiveExpertSystem

app = Flask(__name__)

@app.route('/start')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    # Get form data
    ignition = request.form.get('ignition') == 'true'
    engine_crank = request.form.get('engineCrank') == 'true'
    enough_fuel = request.form.get('enoughFuel') == 'true'
    ignition_off = request.form.get('ignitionOff') == 'true'
    engine_not_crank = request.form.get('engineNotCrank') == 'true'
    not_enough_fuel = request.form.get('notEnoughFuel') == 'true'
    temperature = request.form.get('temperature') == 'true'
    liquid_leakage = request.form.get('liquidLeakage') == 'true' 
    ac_blowing_hot_air = request.form.get('acBlowingHotAir') == 'true'
    # additional_input = request.form.get('additionalInput') == 'true'

    # Perform diagnosis using the expert system
    expert_system = AutomotiveExpertSystem()
    result_rules = expert_system.query_fault(**{
        'ignition': ignition,
        'engine_crank': engine_crank,
        'enough_fuel': enough_fuel,
        'ignition_off': ignition_off,
        'engine_not_crank': engine_not_crank,
        'not_enough_fuel': not_enough_fuel,
        'temperature': temperature,
        'liquid_leakage':liquid_leakage,
        'ac_blowing_hot_air': ac_blowing_hot_air
        # 'additional_input': additional_input,
    })
    print ('enginenotcrank:', engine_not_crank)
    print ('resultRules', result_rules)

    # Convert rule numbers to user-friendly descriptions
    recommended_actions = [RULE_DESCRIPTIONS.get(rule, rule) for rule in result_rules.values() if not rule.startswith('rule')]


    return render_template('result.html', recommended_actions=recommended_actions)

if __name__ == "__main__":
    app.run(debug=True)
