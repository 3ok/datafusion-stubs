from __future__ import annotations

from datafusion._internal.expr import Expr
from datafusion._internal.sql.logical import LogicalPlan

class ScalarFunction:
    def fun(self) -> BuiltinScalarFunction: ...
    def args(self) -> list[Expr]: ...

class BuiltinScalarFunction: ...
