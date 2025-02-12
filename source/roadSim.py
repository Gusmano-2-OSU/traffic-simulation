import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class fundamentalDiagram(ABC):
    parameters: dict = {}

    @abstractmethod
    def calculate_flowrate(self, density: np.ndarray) -> int:
        pass


class Greenshields(fundamentalDiagram):
    parameters: dict = {"speedLimit": 10, "jamDensity": 160}

    def __init__(self, speedLimit=65, jamDensity=160):
        self.parameters["speedLimit"] = speedLimit
        self.parameters["jamDensity"] = jamDensity

    def calculate_flowrate(self, density) -> int:
        flowrate = (
            density
            * self.parameters["speedLimit"]
            * (1 - density / self.parameters["jamDensity"])
        )
        return flowrate

    def plot(
        self,
        quantity="flowrate",
    ) -> None:
        densityAxis = np.arange(0, self.parameters["jamDensity"] + 1, 1)
        flowrateResponse = self.calculate_flowrate(densityAxis)

        plt.plot(densityAxis, flowrateResponse)
        plt.xlabel("Density [veh/m]")
        plt.ylabel("Flowrate [veh/s]")
        plt.grid(visible=True, which="both")
        plt.xlim(0, self.parameters["jamDensity"])
        plt.ylim(bottom=0, top=1.1 * max(flowrateResponse))
        plt.show()


class link:
    speedLimit: int = 10
    length: int = 10.2
    maxDensity: int = 160

    def __init__(self, speedLimit=10, length=10.2):
        self.speedLimit = speedLimit
        self.length = length


class road:
    __name__: str = "Road"
    link_instance: link = link()

    def __init__(self, name="Road", link_instance=link()):
        self.__name__ = name
        self.link_instance = link


fd = Greenshields()
fd.plot()
