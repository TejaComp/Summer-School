import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./libllama2.so')

# Define the Config structure
class Config(ctypes.Structure):
    _fields_ = [
        ("dim", ctypes.c_int),
        ("hidden_dim", ctypes.c_int),
        ("n_layers", ctypes.c_int),
        ("n_heads", ctypes.c_int),
        ("n_kv_heads", ctypes.c_int),
        ("vocab_size", ctypes.c_int),
        ("seq_len", ctypes.c_int)
    ]

# Define the TransformerWeights structure
class TransformerWeights(ctypes.Structure):
    _fields_ = [
        ("token_embedding_table", ctypes.POINTER(ctypes.c_float)),
        ("rms_att_weight", ctypes.POINTER(ctypes.c_float)),
        ("rms_ffn_weight", ctypes.POINTER(ctypes.c_float)),
        ("wq", ctypes.POINTER(ctypes.c_float)),
        ("wk", ctypes.POINTER(ctypes.c_float)),
        ("wv", ctypes.POINTER(ctypes.c_float)),
        ("wo", ctypes.POINTER(ctypes.c_float)),
        ("w1", ctypes.POINTER(ctypes.c_float)),
        ("w2", ctypes.POINTER(ctypes.c_float)),
        ("w3", ctypes.POINTER(ctypes.c_float)),
        ("rms_final_weight", ctypes.POINTER(ctypes.c_float)),
        ("wcls", ctypes.POINTER(ctypes.c_float))
    ]

# Define the RunState structure
class RunState(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.POINTER(ctypes.c_float)),
        ("xb", ctypes.POINTER(ctypes.c_float)),
        ("xb2", ctypes.POINTER(ctypes.c_float)),
        ("hb", ctypes.POINTER(ctypes.c_float)),
        ("hb2", ctypes.POINTER(ctypes.c_float)),
        ("q", ctypes.POINTER(ctypes.c_float)),
        ("k", ctypes.POINTER(ctypes.c_float)),
        ("v", ctypes.POINTER(ctypes.c_float)),
        ("att", ctypes.POINTER(ctypes.c_float)),
        ("logits", ctypes.POINTER(ctypes.c_float)),
        ("key_cache", ctypes.POINTER(ctypes.c_float)),
        ("value_cache", ctypes.POINTER(ctypes.c_float))
    ]

# Define the Transformer structure
class Transformer(ctypes.Structure):
    _fields_ = [
        ("config", Config),
        ("weights", TransformerWeights),
        ("state", RunState),
        ("fd", ctypes.c_int),
        ("data", ctypes.POINTER(ctypes.c_float)),
        ("file_size", ctypes.c_ssize_t)
    ]

# Define the malloc_run_state function
lib.malloc_run_state.argtypes = [ctypes.POINTER(RunState), ctypes.POINTER(Config)]
lib.malloc_run_state.restype = None

def malloc_run_state(state, config):
    lib.malloc_run_state(ctypes.byref(state), ctypes.byref(config))

# Define the free_run_state function
lib.free_run_state.argtypes = [ctypes.POINTER(RunState)]
lib.free_run_state.restype = None

def free_run_state(state):
    lib.free_run_state(ctypes.byref(state))
    
def rmsnorm(o,x,weight,size):
o_ctypes=o.ctypes_data_as(ctypes.POINTER(ctypes.c_float))
x_ctypes=x.ctypes_data_as(ctypes.POINTER(ctypes.c_float))
weight_ctypes=weight.ctypes_data_as(ctypes.POINTER(ctypes.c_float))
size_ctypes=size.ctypes_data_as(ctypes.POINTER(ctypes.c_float))
lib.rmsnorm(o_ctypes, x_ctypes, weight_ctypes, size)

lib.matmul.argtypes = [
    ctypes.POINTER(ctypes.c_float), # xout
    ctypes.POINTER(ctypes.c_float), # x
    ctypes.POINTER(ctypes.c_float), # w
    ctypes.c_int,                   # n
    ctypes.c_int                    # d
]
lib.matmul.restype = None

def matmul(xout, x, w, n, d):
    xout_ctypes = xout.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    x_ctypes = x.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    w_ctypes = w.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    lib.matmul(xout_ctypes, x_ctypes, w_ctypes, n, d)

# Example usage function
def run_model():
    config = Config(dim=512, hidden_dim=2048, n_layers=6, n_heads=8, n_kv_heads=4, vocab_size=256, seq_len=128)

    # Initialize the model
    transformer = Transformer()
    transformer.config = config
    transformer.state = RunState()

    malloc_run_state(transformer.state, transformer.config)

    for i in range(transformer.config.vocab_size):
        transformer.state.logits[i] = i * 0.1  # Example: filling logits with some dummy values

    print("Logits before rmsnorm:")
    for i in range(transformer.config.vocab_size):
        print(f"Index {i}: {transformer.state.logits[i]}")
    free_run_state(transformer.state)
    
#Rmsnorm Function
size=10
x=np.

if __name__ == "__main__":
    run_model()

