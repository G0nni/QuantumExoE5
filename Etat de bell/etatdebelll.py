from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Etape 1

# création des registres
qr = QuantumRegister(2)
cr = ClassicalRegister(2)

# création du circuit
circuit = QuantumCircuit(qr, cr)

# initialisation
circuit.h(qr[0])
circuit.cx(qr[0], qr[1])


EtatSouhaite = input("Quel est l'état souhaité? (phi+, phi-, psi+, psi-): ")

print("Etat souhaité: ", EtatSouhaite)

if EtatSouhaite == "phi-":
    circuit.z(qr[0])

if EtatSouhaite == "psi+":
    circuit.x(qr[1])

if EtatSouhaite == "psi-":
    circuit.z(qr[0])
    circuit.x(qr[1])

# mesure
circuit.measure(qr, cr)

# execution du circuit
simulator = AerSimulator()
compiled_circuit = transpile(circuit, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()

# Afficher les résultats
counts = result.get_counts(circuit)
print("Counts:", counts)


# Afficher le circuit
print(circuit.draw(output='text'))