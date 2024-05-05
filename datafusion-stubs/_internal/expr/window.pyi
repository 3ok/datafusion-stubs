from __future__ import annotations

from datafusion._internal.common.df_schema import DFSchema
from datafusion._internal.expr import Expr
from datafusion._internal.sql.logical import LogicalPlan

class Window:
    def schema(self) -> DFSchema: ...
    def get_window_expr(self) -> list[Expr]: ...
    def get_sort_exprs(self) -> list[Expr]: ...
    def get_partition_exprs(self, expr: Expr) -> list[Expr]: ...
    def get_args(self, epr: Expr) -> list[Expr]: ...
    def window_func_name(self, expr: Expr) -> str: ...
    def get_frame(self, expr: Expr) -> WindowFrame | None: ...

class WindowFrame:
    def __init__(
        self, unit: str, start_bound: int | None, end_bound: int | None
    ) -> None: ...
    def get_frame_units(self) -> str: ...
    def get_lower_bound(self) -> WindowFrameBound: ...
    def get_upper_bound(self) -> WindowFrameBound: ...
    def __repr__(self) -> str: ...

class WindowFrameBound:
    def is_current_row(self) -> bool: ...
    def is_preceding(self) -> bool: ...
    def is_following(self) -> bool: ...
    def get_offset(self) -> int | None: ...
    def is_bounded(self) -> bool: ...