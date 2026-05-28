from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([('Rain', 'Traffic')])

cpd_rain = TabularCPD(
    variable='Rain',
    variable_card=2,
    values=[[0.7], [0.3]]
)

cpd_traffic = TabularCPD(
    variable='Traffic',
    variable_card=2,
    values=[
        [0.9, 0.2],
        [0.1, 0.8]
    ],
    evidence=['Rain'],
    evidence_card=[2]
)

model.add_cpds(cpd_rain, cpd_traffic)

model.check_model()

inference = VariableElimination(model)

result = inference.query(
    variables=['Traffic'],
    evidence={'Rain': 1}
)

print(result)
