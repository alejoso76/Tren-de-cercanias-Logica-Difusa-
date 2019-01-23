import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

velocidad = ctrl.Antecedent(np.arange(0, 80, 1), 'v')
distancia = ctrl.Antecedent(np.arange(0, 100, 1), 'x')
aceleracion = ctrl.Antecedent(np.arange(-10, 10, 1), 'a')
aceleracionf = ctrl.Consequent(np.arange(-10, 10, 1), 'af')
velocidad_final = ctrl.Consequent(np.arange(0, 80, 1), 'vf')

velocidad.automf(5,'quant')
distancia.automf(5,'quant')
aceleracion.automf(3,'quant')

"""
'lower',
'low',
'average',
'high',
'higher',
"""

velocidad.view()
distancia.view()
plt.show()

aceleracionf['low'] = fuzz.trimf(aceleracionf.universe, [-10, -10, 0])
aceleracionf['medium'] = fuzz.trimf(aceleracionf.universe, [-10, 0, 10])
aceleracionf['high'] = fuzz.trimf(aceleracionf.universe, [0, 10, 10])

aceleracionf.view()
plt.show()

velocidad_final['lower'] = fuzz.trimf(velocidad_final.universe, [0, 0, 20])
velocidad_final['low'] = fuzz.trimf(velocidad_final.universe, [0, 20, 40])
velocidad_final['average'] = fuzz.trimf(velocidad_final.universe, [20, 40, 60])
velocidad_final['high'] = fuzz.trimf(velocidad_final.universe, [40, 60, 80])
velocidad_final['higher'] = fuzz.trimf(velocidad_final.universe, [60, 80, 80])

velocidad_final.view()
plt.show()

#-------reglas aceleracionf
rule1 = ctrl.Rule(velocidad['higher'] & distancia['lower'], aceleracionf['low'])
rule2 = ctrl.Rule(velocidad['high'] & distancia['lower'], aceleracionf['low'])
rule3 = ctrl.Rule(velocidad['average'] & distancia['lower'], aceleracionf['low'])
rule4 = ctrl.Rule(velocidad['low'] & distancia['lower'], aceleracionf['low'])
rule5 = ctrl.Rule(velocidad['lower'] & distancia['lower'], aceleracionf['medium'])

rule6 = ctrl.Rule(velocidad['higher'] & distancia['low'], aceleracionf['low'])
rule7 = ctrl.Rule(velocidad['high'] & distancia['low'], aceleracionf['low'])
rule8 = ctrl.Rule(velocidad['average'] & distancia['low'], aceleracionf['low'])
rule9 = ctrl.Rule(velocidad['low'] & distancia['low'], aceleracionf['medium'])
rule10 = ctrl.Rule(velocidad['lower'] & distancia['low'], aceleracionf['high'])

rule11 = ctrl.Rule(velocidad['higher'] & distancia['average'], aceleracionf['low'])
rule12 = ctrl.Rule(velocidad['high'] & distancia['average'], aceleracionf['low'])
rule13 = ctrl.Rule(velocidad['average'] & distancia['average'], aceleracionf['medium'])
rule14 = ctrl.Rule(velocidad['low'] & distancia['average'], aceleracionf['high'])
rule15 = ctrl.Rule(velocidad['lower'] & distancia['average'], aceleracionf['high'])

rule16 = ctrl.Rule(velocidad['higher'] & distancia['high'], aceleracionf['low'])
rule17 = ctrl.Rule(velocidad['high'] & distancia['high'], aceleracionf['medium'])
rule18 = ctrl.Rule(velocidad['average'] & distancia['high'], aceleracionf['high'])
rule19 = ctrl.Rule(velocidad['low'] & distancia['high'], aceleracionf['high'])
rule20 = ctrl.Rule(velocidad['lower'] & distancia['high'], aceleracionf['high'])

rule21 = ctrl.Rule(velocidad['higher'] & distancia['high'], aceleracionf['low'])
rule22 = ctrl.Rule(velocidad['high'] & distancia['high'], aceleracionf['medium'])
rule23 = ctrl.Rule(velocidad['average'] & distancia['high'], aceleracionf['high'])
rule24 = ctrl.Rule(velocidad['low'] & distancia['high'], aceleracionf['high'])
rule25 = ctrl.Rule(velocidad['lower'] & distancia['high'], aceleracionf['high'])

rule26 = ctrl.Rule(velocidad['higher'] & distancia['higher'], aceleracionf['medium'])
rule27 = ctrl.Rule(velocidad['high'] & distancia['higher'], aceleracionf['high'])
rule28 = ctrl.Rule(velocidad['average'] & distancia['higher'], aceleracionf['high'])
rule29 = ctrl.Rule(velocidad['low'] & distancia['higher'], aceleracionf['high'])
rule30 = ctrl.Rule(velocidad['lower'] & distancia['higher'], aceleracionf['high'])


#----------------reglas velocidad
rule31 = ctrl.Rule(velocidad['higher'] & aceleracion['low'], velocidad_final['high'])
rule32 = ctrl.Rule(velocidad['high'] & aceleracion['low'], velocidad_final['average'])
rule33 = ctrl.Rule(velocidad['average'] & aceleracion['low'], velocidad_final['low'])
rule34 = ctrl.Rule(velocidad['low'] & aceleracion['low'], velocidad_final['lower'])
rule44 = ctrl.Rule(velocidad['lower'] & aceleracion['low'], velocidad_final['lower'])

rule35 = ctrl.Rule(velocidad['higher'] & aceleracion['average'], velocidad_final['higher'])
rule36 = ctrl.Rule(velocidad['high'] & aceleracion['average'], velocidad_final['high'])
rule37 = ctrl.Rule(velocidad['average'] & aceleracion['average'], velocidad_final['average'])
rule38 = ctrl.Rule(velocidad['low'] & aceleracion['average'], velocidad_final['low'])
rule39 = ctrl.Rule(velocidad['lower'] & aceleracion['average'], velocidad_final['lower'])

rule45 = ctrl.Rule(velocidad['higher'] & aceleracion['high'], velocidad_final['higher'])
rule40 = ctrl.Rule(velocidad['high'] & aceleracion['high'], velocidad_final['higher'])
rule41 = ctrl.Rule(velocidad['average'] & aceleracion['high'], velocidad_final['high'])
rule42 = ctrl.Rule(velocidad['low'] & aceleracion['high'], velocidad_final['average'])
rule43 = ctrl.Rule(velocidad['lower'] & aceleracion['high'], velocidad_final['low'])

acc_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
                                rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
                                rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30])
acc = ctrl.ControlSystemSimulation(acc_ctrl)

vf_ctrl = ctrl.ControlSystem([rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40,rule41, rule42, rule43, rule44, rule45])
vf = ctrl.ControlSystemSimulation(vf_ctrl)

acc.input['x'] = 20
acc.input['v'] = 50

acc.compute()
vf.input['a']=acc.output['af']
vf.compute()
print(vf.output['vf'])