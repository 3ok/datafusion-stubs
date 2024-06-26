from __future__ import annotations

from datafusion._internal.common.df_schema import DFSchema
from datafusion._internal.expr import Expr
from datafusion._internal.sql.logical import LogicalPlan

class JoinType:
    def is_outer(self) -> bool: ...
    def __repr__(self) -> str: ...

class JoinConstraint:
    def __repr__(self) -> str: ...

class Join:
    def left(self) -> LogicalPlan: ...
    def right(self) -> LogicalPlan: ...
    def on(self) -> list[tuple[Expr, Expr]]: ...
    def filter(self) -> Expr | None: ...
    def join_type(self) -> JoinType: ...
    def join_constraint(self) -> JoinConstraint: ...
    def schema(self) -> DFSchema: ...
    def null_equals_null(self) -> bool: ...
    def __repr__(self) -> str: ...
    def __name__(self) -> str: ...
