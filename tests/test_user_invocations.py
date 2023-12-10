from fhirpathpy.engine.util import get_data,is_number
from fhirpathpy import evaluate

def pow_(ctx, inputs, exp=2):
    return [pow(d, exp) for d in map(get_data, inputs) if is_number(d)]

def user_invocation_test():

    env = {}

    env["userInvocationTable"] = {
        "pow": {
            "fn": pow_, 
            "arity": {0: [], 1: ["Integer"]}
        },
      }
    assert evaluate({"a": [5,6,7]}, "a.pow()", env) == [25, 36, 49]

    assert evaluate({}, "(5 | 6 | 7).pow()", env) == [25, 36, 49]

    assert evaluate({"a": [5,6,7]}, "a.pow(3)", env) == [125, 216, 343]