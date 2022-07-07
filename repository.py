from Graph import *


class Repository:
    def create(self, file):
        with open(f'graphics/{file}') as f:
            lines = f.read().splitlines()
            x_name, y_name, x_err, y_err, log, err = [k.strip() for k in lines[0].split(',')]
            x_value = []
            y_value = []
            x_value_err = []
            y_value_err = []
            for line in lines[1:]:
                val = line.split()
                x, y, x_e, y_e = val
                x_value.append(float(x))
                y_value.append(float(y))
                x_value_err.append(x_e)
                y_value_err.append(y_e)
            if err == 'True':
                graph = Graph_not_err(file, x_value, y_value, log, err)
            elif x_err != 'None' and y_err != 'None':
                graph = Graph_global_err(file, x_value, y_value, log, err, float(x_err), float(y_err))
            else:
                graph = Graph_local_err(file, x_value, y_value,  log, err, x_value_err, y_value_err)
            return graph




