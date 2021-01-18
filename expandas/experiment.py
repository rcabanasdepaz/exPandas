from expandas.input import generate_input


class Experiment(object):

    def __init__(self, functions, verbose=0, logfolder="."):
        self.__verbose__ = verbose
        self.__logfolder__ = logfolder
        self.__functions = functions



    def __is_evaluable__(self, params):
        return True

    def __run_iteration(self, params):
        for f in self.__functions:
            if isinstance(params, dict):
                params = f(**params)
            elif isinstance(params, list):
                params = f(*params)
            else:
                params = f(params)

        return params

    def run(self, inputs):
        return [self.__run_iteration(i) for i in inputs.to_dict(orient='records')]




