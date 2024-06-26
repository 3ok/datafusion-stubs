from __future__ import annotations

from datafusion._internal.common.df_schema import DFSchema
from datafusion._internal.expr import Expr
from datafusion._internal.sql.logical import LogicalPlan

class Union:
    def input(self) -> list[LogicalPlan]: ...
    def schema(self) -> DFSchema: ...
    def __repr__(self) -> str: ...
    def __name__(self) -> str: ...
