import binascii
from array import array

import numpy as np
import os
import pickle
from segd_creator import SegDCreator

if __name__ == '__main__':
    segdproto_path = os.path.join('.', '00015208.segdproto')

    segd_creator = SegDCreator(segdproto_path)
    segd = segd_creator.reconstruct()
    # print(len(segd))

    save_dir = ''
    segd_creator.save_segd(save_dir)