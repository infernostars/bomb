from typing import Any, Optional

from exceptions import BombIllegalDefinitionException
from global_registrator import GlobalRegistrator


class Environment:
    """
    An Environment is a class which stores variable data, as well as any other important configuration.
    """
    def __init__(self, parent: Optional["Environment"], global_registrator: Optional[GlobalRegistrator]): # We use quotes in the parent optional tag so that it can refer to itself without being init'd
        self.parent = parent
        self.gregistrator = global_registrator
        if self.gregistrator is None:
            self.gregistrator = parent.gregistrator
        self.variables = {}

    def register_var(self, var: str, value: Any):
        if not var.startswith("__"):
            self.variables[var] = value
            return var
        raise BombIllegalDefinitionException(f"The value {var} starts with a double underscore and can only be defined by the runtime!")

    def get_var(self, var: str):
        return self.variables[var]

    def register_gvar(self, var: str, value: Any):
        self.gregistrator.register_gvar(var, value, self)

    def get_gvar(self, var: str):
        return self.gregistrator.get_gvar(var, self)