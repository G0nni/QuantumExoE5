from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble


n=2

# Etape 1

# création des registres
qr = QuantumRegister(n)
cr = ClassicalRegister(n)

# création du circuit
circuit = QuantumCircuit(qr, cr)

# Etape 2
# on applique hadamard sur tous les qubits
for i in range(n):
    circuit.h(i)



# Etape 3

# on répète l'étape 3 en fonction du nombre de steps voulu
steps = 3

for step in range(steps):
    # CNOT sur entre chaque paire de qubits voisins
    for i in range(n-1):
        circuit.cx(i, i+1)


    # application de Rz sur chaque qubit pour simuler
    # le temps qui passe avant la mesure
    t=0.5
    for i in range(n):
        circuit.rz(t, i)


# Etape 4

# mesure chaque qubit
for i in range(n):
    circuit.measure(qr[i], cr[i])

Simulator = AerSimulator()
compiled_circuit = transpile(circuit, Simulator)
qobj = assemble(compiled_circuit)
result = Simulator.run(qobj).result()

# Afficher les résultats
counts = result.get_counts(circuit)
print("Counts:", counts)







