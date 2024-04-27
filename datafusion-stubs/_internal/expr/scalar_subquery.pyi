from __future__ import annotations

from datafusion._internal.expr import Expr
from datafusion._internal.expr.subquery import Subquery
from datafusion._internal.sql.logical import LogicalPlan

class ScalarSubquery:
    def subquery(self) -> Subquery: ...
