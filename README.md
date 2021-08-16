# SEG-D Reconstructor
#### Reconstruction script for SEG-D files from header block, traces headers and traces data
***
### Usage 

* Create instance of `SegDCreator(segdproto_path='...')`, where `segdproto_path` is path to 
  [pickle](https://docs.python.org/3/library/pickle.html) - dumped file with `.segdproto` extension. 
  This file should contain pickle-serialized list of length 3:

  | Index   | 0      |   1    |   2    |
  | :----:  | :----: | :----: | :----: |
  | Content | Header block <br />(GenHeaders + ChanSets <br /> + ExtdHdr+ ExtrlHdr) | Traces headers <br /> Trhdr + TrExtHdr #1-7 | Traces Data      |   
  | Type    | bytearray | List of bytearrays <br /> with `len(num_of_traces)`       | `np.array` with <br /> `shape=(num_of_traces, num_of_samples)` |

* Run `.reconstruct()` and read or save with `save_segd()` result

* Example can be found in `run.py`