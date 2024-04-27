from __future__ import annotations

from datafusion._internal.expr import Expr
from datafusion._internal.expr.subquery import Subquery
from datafusion._internal.sql.logical import LogicalPlan

class InSubquery:
    def expr(self) -> Expr: ...
    def subquery(self) -> Subquery: ...
    def negated(self) -> bool: ...
