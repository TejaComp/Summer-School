import ctypes
import numpy as np
import os

lib_path = os.path.join(os.getcwd(), 'libllama2.so')
lib = ctypes.CDLL(lib_path)

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

# Define the Tokenizer structure
class Tokenizer(ctypes.Structure):
    _fields_ = [
        ("vocab", ctypes.POINTER(ctypes.c_char_p)),
        ("vocab_scores", ctypes.POINTER(ctypes.c_float)),
        ("sorted_vocab", ctypes.POINTER(ctypes.c_void_p)),
        ("vocab_size", ctypes.c_int),
        ("max_token_length", ctypes.c_uint),
        ("byte_pieces", ctypes.c_ubyte * 512)
    ]

# Define the Sampler structure
class Sampler(ctypes.Structure):
    _fields_ = [
        ("vocab_size", ctypes.c_int),
        ("temperature", ctypes.c_float),
        ("topp", ctypes.c_float),
        ("rng_seed", ctypes.c_ulonglong)
    ]

try:
    lib = ctypes.CDLL('./libllama2.so')
    print("Library loaded successfully.")
except Exception as e:
    print(f"Error loading library: {e}")

# Define function prototypes
lib.malloc_run_state.argtypes = [ctypes.POINTER(RunState), ctypes.POINTER(Config)]
lib.malloc_run_state.restype = None

lib.free_run_state.argtypes = [ctypes.POINTER(RunState)]
lib.free_run_state.restype = None

lib.memory_map_weights.argtypes = [ctypes.POINTER(TransformerWeights), ctypes.POINTER(Config), ctypes.POINTER(ctypes.c_float), ctypes.c_int]
lib.memory_map_weights.restype = None

lib.read_checkpoint.argtypes = [ctypes.c_char_p, ctypes.POINTER(Config), ctypes.POINTER(TransformerWeights),
                                ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.POINTER(ctypes.c_float)),
                                ctypes.POINTER(ctypes.c_ssize_t)]
lib.read_checkpoint.restype = None

lib.build_transformer.argtypes = [ctypes.POINTER(Transformer), ctypes.c_char_p]
lib.build_transformer.restype = None

lib.free_transformer.argtypes = [ctypes.POINTER(Transformer)]
lib.free_transformer.restype = None

lib.rmsnorm.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float),
                        ctypes.POINTER(ctypes.c_float), ctypes.c_int]
lib.rmsnorm.restype = None

lib.softmax.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
lib.softmax.restype = None

lib.matmul.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float),
                       ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.c_int]
lib.matmul.restype = None

lib.forward.argtypes = [ctypes.POINTER(Transformer), ctypes.c_int, ctypes.c_int]
lib.forward.restype = ctypes.POINTER(ctypes.c_float)

lib.build_tokenizer.argtypes = [ctypes.POINTER(Tokenizer), ctypes.c_char_p, ctypes.c_int]
lib.build_tokenizer.restype = None

lib.free_tokenizer.argtypes = [ctypes.POINTER(Tokenizer)]
lib.free_tokenizer.restype = None

lib.decode.argtypes = [ctypes.POINTER(Tokenizer), ctypes.c_int, ctypes.c_int]
lib.decode.restype = ctypes.c_char_p

lib.encode.argtypes = [ctypes.POINTER(Tokenizer), ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
lib.encode.restype = None

lib.build_sampler.argtypes = [ctypes.POINTER(Sampler), ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_ulonglong]
lib.build_sampler.restype = None

lib.generate.argtypes = [ctypes.POINTER(Transformer), ctypes.POINTER(Tokenizer), ctypes.POINTER(Sampler), ctypes.c_char_p, ctypes.c_int]
lib.generate.restype = None

lib.chat.argtypes = [ctypes.POINTER(Transformer), ctypes.POINTER(Tokenizer), ctypes.POINTER(Sampler), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
lib.chat.restype = None

lib.free_sampler.argtypes = [ctypes.POINTER(Sampler)]
lib.free_sampler.restype = None

lib.free_transformer.argtypes = [ctypes.POINTER(Transformer)]
lib.free_transformer.restype = None

lib.forward.argtypes = [ctypes.POINTER(Transformer), ctypes.c_int, ctypes.c_int]
lib.forward.restype = ctypes.POINTER(ctypes.c_float)

# Initialize the variables
data_ptr = ctypes.POINTER(ctypes.c_void_p)()
fd = ctypes.c_int()
file_size = ctypes.c_size_t()
n = 0  # Placeholder for token
d = 0  # Placeholder for position

# Helper function to initialize a Tokenizer
def create_tokenizer(tokenizer_path, vocab_size):
    tokenizer = Tokenizer()
    lib.build_tokenizer(ctypes.byref(tokenizer), tokenizer_path.encode('utf-8'), vocab_size)
    return tokenizer

# Helper function to free a Tokenizer
def destroy_tokenizer(tokenizer):
    lib.free_tokenizer(ctypes.byref(tokenizer))

# Helper function for decoding
def decode(tokenizer, prev_token, token):
    result = lib.decode(ctypes.byref(tokenizer), prev_token, token)
    return ctypes.string_at(result).decode('utf-8')

# Helper function for encoding
def encode(tokenizer, text, bos, eos):
    tokens = np.zeros(len(text), dtype=np.int32)
    n_tokens = ctypes.c_int(0)
    lib.encode(ctypes.byref(tokenizer), text.encode('utf-8'), bos, eos, tokens.ctypes.data_as(ctypes.POINTER(ctypes.c_int)), ctypes.byref(n_tokens))
    return tokens[:n_tokens.value]

def rmsnorm(o, x, weight):
    o = np.ascontiguousarray(o, dtype=np.float32)
    x = np.ascontiguousarray(x, dtype=np.float32)
    weight = np.ascontiguousarray(weight, dtype=np.float32)
    size = ctypes.c_int(len(x))

    o_ptr = o.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    weight_ptr = weight.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

    lib.rmsnorm(o_ptr, x_ptr, weight_ptr, size)

def softmax(x):
    x = np.ascontiguousarray(x, dtype=np.float32)
    size = ctypes.c_int(len(x))

    x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

    lib.softmax(x_ptr, size)

def matmul(xout, x, w, n, d):
    xout = np.ascontiguousarray(xout, dtype=np.float32)
    x = np.ascontiguousarray(x, dtype=np.float32)
    w = np.ascontiguousarray(w, dtype=np.float32)

    xout_ptr = xout.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
    w_ptr = w.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

    lib.matmul(xout_ptr, x_ptr, w_ptr, n, d)

def allocate_run_state():
    try:
        print("Calling malloc_run_state...")
        lib.malloc_run_state(ctypes.byref(run_state), ctypes.byref(config))
        print("Malloc run_state successful.")
    except Exception as e:
        print(f"Error in malloc_run_state: {e}")

def free_run_state():
    try:
        print("Calling free_run_state...")
        lib.free_run_state(ctypes.byref(run_state))
        print("Free run_state successful.")
    except Exception as e:
        print(f"Error in free_run_state: {e}")

def memory_map_weights():
    try:
        print("Calling memory_map_weights...")
        lib.memory_map_weights(ctypes.byref(transformer.weights), ctypes.byref(config), data_ptr, fd)
        print("Memory mapping weights successful.")
    except Exception as e:
        print(f"Error in memory_map_weights: {e}")

def read_checkpoint():
    try:
        print("Calling read_checkpoint...")
        lib.read_checkpoint(file_path, ctypes.byref(config), ctypes.byref(transformer.weights), ctypes.byref(fd), ctypes.byref(data_ptr), ctypes.byref(file_size))
        print("Checkpoint read successfully.")
    except Exception as e:
        print(f"Error in read_checkpoint: {e}")

def build_transformer():
    try:
        print("Calling build_transformer...")
        lib.build_transformer(ctypes.byref(transformer), file_path.encode('utf-8'))
        print("Transformer built successfully.")
    except Exception as e:
        print(f"Error in build_transformer: {e}")

def free_transformer():
    try:
        print("Calling free_transformer...")
        lib.free_transformer(ctypes.byref(transformer))
        print("Free transformer successful.")
    except Exception as e:
        print(f"Error in free_transformer: {e}")

def forward_pass(token, pos):
    try:
        print("Calling forward...")
        output = lib.forward(ctypes.byref(transformer), token, pos)
        print("Forward pass successful.")
        return output
    except Exception as e:
        print(f"Error in forward pass: {e}")
        return None

# Example usage
if __name__ == "__main__":
    file_path = "/Users/tejaswinisubramanian/llama2.c/stories15M.bin"
    config = Config()
    transformer = Transformer()
    run_state = RunState()
    tokenizer = create_tokenizer("/Users/tejaswinisubramanian/llama2.c/tokenizer.bin", 32000)
    sampler = Sampler(vocab_size=32000, temperature=1.0, topp=0.9, rng_seed=42)

    build_transformer()
    allocate_run_state()
    memory_map_weights()
    read_checkpoint()

    text = "Hello, world!"
    tokens = encode(tokenizer, text, bos=1, eos=2)
    print("Tokens:", tokens)

    token = tokens[0]
    pos = 0  # Initial position
    output = forward_pass(token, pos)
    print("Output:", output)

    decoded_text = decode(tokenizer, 1, token)
    print("Decoded text:", decoded_text)

    free_run_state()
    free_transformer()
    destroy_tokenizer(tokenizer)

