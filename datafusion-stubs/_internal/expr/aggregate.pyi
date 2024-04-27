from __future__ import annotations

from typing import TYPE_CHECKING

from datafusion._internal.common.df_schema import DFSchema

if TYPE_CHECKING:
    from datafusion._internal.expr import Expr
    from datafusion._internal.sql.logical import LogicalPlan

class Aggregate:
    def group_by_exprs(self) -> list[Expr]: ...
    def aggregate_exprs(self) -> list[Expr]: ...
    def agg_expressions(self) -> list[Expr]: ...
    def agg_func_name(self) -> str: ...
    def aggregation_arguments(self, expr: Expr) -> list[Expr]: ...
    def input(self) -> list[LogicalPlan]: ...
    def schema(self) -> DFSchema: ...
    def __repr__(self) -> str: ...
