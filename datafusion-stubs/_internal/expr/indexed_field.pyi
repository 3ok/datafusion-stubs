from __future__ import annotations

from datafusion._internal.expr import Expr
from datafusion._internal.expr.literal import Literal
from datafusion._internal.sql.logical import LogicalPlan

class GetIndexedField:
    def expr(self) -> Expr: ...
    def key(self) -> Literal: ...
    def __repr__(self) -> str: ...
