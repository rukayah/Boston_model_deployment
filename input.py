import numpy as np
import json

def input(data : str):
    body = np.array(json.loads(data)["inputs"])
    return body

