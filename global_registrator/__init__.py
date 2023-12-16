from abc import ABC, abstractmethod
from typing import Any

from environment import Environment


class GlobalRegistrator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_gvar(self, var: str, env: Environment):
        pass

    @abstractmethod
    def register_gvar(self, var: str, value: Any, env: Environment):
        pass