from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np

def prepare_arbitrary_state(a, b):
    """
    Prépare un qubit dans l'état a|0> + b|1>.
    a et b doivent être des nombres complexes.
    """
    qc = QuantumCircuit(1)
    # Normaliser les coefficients
    norm = np.sqrt(np.abs(a)**2 + np.abs(b)**2)
    a = a / norm
    b = b / norm
    # Calcul des angles de rotation
    theta = 2 * np.arccos(np.abs(a))
    phi = np.angle(b) - np.angle(a)
    # Application des rotations nécessaires
    qc.ry(theta, 0)
    qc.rz(phi, 0)
    return qc

# Etape 1

# création des registres
qr = QuantumRegister(1)

# création du circuit
circuit = QuantumCircuit(qr)

# Etape 2

# Préparation de l'état arbitraire
a = 1
b = 1j
qc = prepare_arbitrary_state(a, b)

# Etape 3

def Visualise_bloch(circuit, gate_name):
    state = Statevector.from_instruction(circuit)
    plot_bloch_multivector(state)
    plt.title(gate_name)
    plt.show()

Visualise_bloch(qc, "État arbitraire")

# appliquer les portes sur le circuit
gates = ['h','x','y','z']
for gate in gates:
    if gate == 'h':
        circuit.h(0)
    elif gate == 'x':
        circuit.x(0)
    elif gate == 'y':
        circuit.y(0)
    elif gate == 'z':
        circuit.z(0)
    Visualise_bloch(circuit, gate)