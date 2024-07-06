import json
import random
import math

# Task-1 Read JSON File as list of list and convert to matrix
with open("/Users/tejaswinisubramanian/Downloads/training_sample.json", "r") as file:
    data = json.load(file)

def create_matrix(data):
    rows = []
    for i in data:
        col = [
            float(i["propertyAge"]),
            i["balconies"],
            float(i["swimmingPool"]),
            i["propertySize"],
            float(i["furnishingStatus"]),
            i["rent"]
        ]
        rows.append(col)
    return rows

Train_data = create_matrix(data)

# Task-2 Create model
def create_weight(m, n):    
    return [[random.uniform(0, 1) for _ in range(n)] for _ in range(m)]

def create_zeromatrix(m, n):    
    return [[0.0 for _ in range(n)] for _ in range(m)]

def multimodel(sample, Weight):
    R1 = len(sample)
    C1 = len(sample[0])
    R2 = len(Weight)
    C2 = len(Weight[0])
    
    print(f"Sample dimensions: {R1}x{C1}")
    print(f"Weight dimensions: {R2}x{C2}")
    
    if C1 != R2:
        print("Cannot multiply the matrices. Invalid dimensions.")
        return None

    result = create_zeromatrix(R1, C2)
    for i in range(R1):
        for j in range(C2):
            for k in range(R2):
                result[i][j] += sample[i][k] * Weight[k][j]

    print(f"Result dimensions: {R1}x{C2}")

    return result

Weight = create_weight(5, 1)

def relu(x):
    return max(0, x)

def apply_relu(matrix):
    return [[relu(element) for element in row] for row in matrix]

result = multimodel(Train_data, Weight)

if result is not None:
    result = apply_relu(result)
    print(result)
else:
    print("Matrix multiplication failed due to incompatible dimensions.")

model = []
for iter in Train_data:
    sample = [iter[:5]]
    Out_model = multimodel(sample, Weight)
    if Out_model is not None:
        model.append(Out_model[0])

Model = [item for sublist in model for item in sublist]

rent = [row[5] for row in Train_data]

def error(predicted, rent):
    estimate = sum((pred - actual) ** 2 for pred, actual in zip(predicted, rent))
    return math.sqrt(estimate / len(predicted))

error_value = error(Model, rent)
print(error_value)


















