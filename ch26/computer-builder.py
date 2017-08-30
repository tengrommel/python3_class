class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = ('Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)

class ComputerBuilder:

    def __init__(self):self.computer = Computer('AG23385193')
    def configure_memory(self, memory):self.computer.memory = memory
    def configure_hdd(self, hdd):self.computer.hdd = hdd
    def configure_gpu(self, gpu_model):self.computer.gpu = gpu_model

class HardwareEngineer:
    def __init__(self):self.builder = None
    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory),
                           self.builder.configure_gpu(gpu),
                           self.builder.configure_hdd(hdd))]
    @property
    def computer(self):return self.builder.computer

def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
    computer = engineer.computer
    print(computer)

if __name__ == '__main__':
    main()