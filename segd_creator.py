import os
from pathlib import Path

import numpy as np
import pickle

class SegDCreator:
    def __init__(self, segdproto_path: str):
        decompressed_list = pickle.load(open(segdproto_path, 'rb'))
        self._filename = os.path.basename(segdproto_path).split('.')[0]
        self._extension = '.reconstructed.segd'
        self._dirname = os.path.dirname(segdproto_path)
        self._hdr_block = bytearray(decompressed_list[0])
        self._traces_hdr = decompressed_list[1]
        self._traces_data = np.array(decompressed_list[2]).astype(np.float32)
        self.reconstructed_segd = bytearray(b'')
    
    def reconstruct(self):
        self.reconstructed_segd.extend(self._hdr_block)

        for trace_hdr, trace_data in zip(self._traces_hdr, self._traces_data):
            self.reconstructed_segd.extend(bytearray(trace_hdr))
            trace_data_buf = trace_data.byteswap().tobytes()
            self.reconstructed_segd.extend(trace_data_buf)
        print(f'Successfully reconstructed {self._filename}.segd')
        return self.reconstructed_segd

    def save_segd(self, save_dir: str = None):
        if save_dir is None or save_dir == '':
            save_dir = os.path.join(self._dirname, 'reconstructed')
            Path(save_dir).mkdir(parents=True, exist_ok=True)

        save_path = os.path.join(save_dir, self._filename + self._extension)
        with open(save_path, 'wb') as f:
            f.write(self.reconstructed_segd)
            print(f'Saved {self._filename + self._extension} in {save_dir}')
