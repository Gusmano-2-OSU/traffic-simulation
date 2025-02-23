import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class fundamentalDiagram(ABC):
    @abstractmethod
    def velocity_at(self, density: np.ndarray) -> np.ndarray:
        pass

    def flowrate_at(self, density: np.ndarray) -> np.ndarray:
        """Hydrodynamic Relationship - true for all fundamental diagrams

        Args:
            density (np.ndarray): Vehicle Density in veh/m

        Returns:
            flowrate: The flowrate for the given densities in veh/s
        """
        flowrate = density * self.velocity_at(density)
        return flowrate

    @abstractmethod
    def plot(self, quantity="flowrate") -> None:
        pass


class Greenshields(fundamentalDiagram):
    def __init__(self, speed_limit=65, jam_density=160):
        self.speed_limit = speed_limit
        self.jam_density = jam_density

    def velocity_at(self, density) -> np.ndarray:
        velocity = self.speed_limit * (
            1 - density / self.jam_density
        )
        return velocity

    def plot(self, quantity="flowrate") -> None:
        densityAxis = np.arange(0, self.jam_density + 1, 1)
        flowrateResponse = self.flowrate_at(densityAxis)

        plt.plot(densityAxis, flowrateResponse)
        plt.xlabel("Density [veh/m]")
        plt.ylabel("Flowrate [veh/s]")
        plt.grid(visible=True, which="both")
        plt.xlim(0, self.jam_density)
        plt.ylim(bottom=0, top=1.1 * max(flowrateResponse))
        plt.show()


class link:
    def __init__(self, speed_limit=10, length=10.2, max_density=160):
        self.speed_limit = speed_limit
        self.length = length
        self.max_density = max_density


class road:
    def __init__(self, name="Road", road_links=link()):
        self.__name__ = name
        self.link = road_links
