from __future__ import annotations

from datafusion._internal.common.df_schema import DFSchema
from datafusion._internal.expr import Expr
from datafusion._internal.sql.logical import LogicalPlan

class Sort:
    def sort_exprs(self) -> list[Expr]: ...
    def get_fetch_val(self) -> int | None: ...
    def input(self) -> list[LogicalPlan]: ...
    def schema(self) -> DFSchema: ...
    def __repr__(self) -> str: ...
