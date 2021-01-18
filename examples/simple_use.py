import expandas as expd


params = {"a": [1, 2, 3, 4], "b": [-10, 10]}
func_params = {"c": lambda t: t["a"] * t["b"]}
transformations = [lambda df: df.query("c>0")]

inputs = generate_input(params, func_params, transformations)
i = inputs.to_dict(orient='records')[0]


def f1(a, b, c):
  return [2 * a, 2 * b, 2 * c]


exp = Experiment(functions=[f1, f1])
exp.run(inputs)
