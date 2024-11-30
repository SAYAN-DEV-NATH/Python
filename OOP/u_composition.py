class Engine:
    def __init__(self, capacity) -> None:
        self.capacity = capacity

    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")


class Car(Engine):
    def __init__(self, name, capacity) -> None:
        self.name = name
        self.engine = Engine(capacity)

    def run(self):
        self.start()
        print("Car is running")
        self.stop()


c1 = Car("BMW", 2000)
c1.run()
