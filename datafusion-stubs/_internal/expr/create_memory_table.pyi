from __future__ import annotations

from datafusion._internal.expr import Expr
from datafusion._internal.sql.logical import LogicalPlan

class CreateMemoryTable:
    def name(self) -> str: ...
    def input(self) -> list[LogicalPlan]: ...
    def if_not_exists(self) -> bool: ...
    def or_replace(self) -> bool: ...
    def __repr__(self) -> str: ...
    def __name__(self) -> str: ...