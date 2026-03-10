import numpy
from utils import utils

def load_data(file_path):
    data_list = []
    label_list = []
    if file_path:
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    attrs = line.split(',')[0:-1]
                    attrs = utils.vcol(numpy.array([float(i) for i in attrs]))
                    label = line.split(',')[-1].strip()
                    data_list.append(attrs)
                    label_list.append(label)
                except:
                    print('Error in loading data')
    return numpy.hstack(data_list), numpy.array(label_list, dtype=numpy.int32)