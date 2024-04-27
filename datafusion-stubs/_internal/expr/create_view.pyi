from __future__ import annotations

from datafusion._internal.expr import Expr
from datafusion._internal.sql.logical import LogicalPlan

class CreateView:
    def name(self) -> str: ...
    def input(self) -> list[LogicalPlan]: ...
    def or_replace(self) -> bool: ...
    def definition(self) -> str | None: ...
    def __repr__(self) -> str: ...
    def __name__(self) -> str: ...