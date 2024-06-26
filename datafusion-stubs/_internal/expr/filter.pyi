from __future__ import annotations

from datafusion._internal.common.df_schema import DFSchema
from datafusion._internal.expr import Expr
from datafusion._internal.sql.logical import LogicalPlan

class Filter:
    def predicate(self) -> Expr: ...
    def input(self) -> list[LogicalPlan]: ...
    def schema(self) -> DFSchema: ...
    def __repr__(self) -> str: ...
