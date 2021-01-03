class Neuron():
    neural_complexity = 0
    __protected_attr = "защищенный атрибут"

    def transmit(self, impulse):
        return impulse

    def __init__(self):
        self.neural_complexity += 1
        print("на один нейорн больше")

    def activate(self, power):
        neural_activity = 0
        neural_activity += power
        print("neuron activated")

    def __protected_method(self):
        print("защищенная херня")

class Axon(Neuron):
    neural_complexity = 2
    def __init__(self):
        print("Axxon init")
        self.neural_complexity +=2


    def activate(self, power, complexity):
        print(f"Axxon with {power} and {complexity}")

neur1 = Neuron()

print(neur1.neural_complexity)

neur1._Neuron__protected_method()

print(neur1._Neuron__protected_attr)

axx1 = Axon()

print(axx1.neural_complexity)

axx1.activate(4, 6)
c =1
print(neur1.neural_complexity)