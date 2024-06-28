from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Etape 1

# création des registres
qr = QuantumRegister(2)
cr = ClassicalRegister(2)

# création du circuit
circuit = QuantumCircuit(qr, cr)

# Etape 2

# porte de Hadamard et porte CNOT pour intrication
circuit.h(qr[0])
circuit.cx(qr[0], qr[1])

# Etape 3

bits = input("Quels bits voulez-vous envoyer? (00, 01, 10, 11): ")

print("Bits à envoyer: ", bits)

if bits == "01":
    circuit.z(qr[0])

if bits == "10":
    circuit.x(qr[0])

if bits == "11":
    circuit.x(qr[0])
    circuit.z(qr[0])

# Etape 4

circuit.cx(qr[0], qr[1])
circuit.h(qr[0])

#mesure
circuit.measure(qr, cr)


# Etape 5
simulator = AerSimulator()
compiled_circuit = transpile(circuit, simulator)

qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()

# Afficher les résultats
counts = result.get_counts(circuit)
print("Counts:", counts)