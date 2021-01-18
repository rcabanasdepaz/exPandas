import pandas as pd
import itertools



def cartesian_product(**params):
    return pd.DataFrame(list(itertools.product(*list(params.values()))), columns=params.keys())


def generate_input(params, func_params=None, transformations=None):

    data = cartesian_product(**params)

    fargs = func_params or {}
    for k, v in fargs.items():
        data[k] = data.apply(v, axis=1)

    transformations  = transformations or []

    for t in transformations:
        data = t(data)

    return data



if __name__ == "__main__":

    cartesian_product(a=[1,2,3], b=[10,11])


    params = {"a": [1,2,3,4], "b":[-10,10]}
    func_params={"c": lambda t: t["a"]*t["b"]}
    transformations = [lambda df: df.query("c>0")]

    input_params = generate_input(params, func_params, transformations)

    print(input_params)

