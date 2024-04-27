from __future__ import annotations

from datafusion._internal.expr.subquery import Subquery

class Exists:
    def subquery(self) -> Subquery: ...
    def negated(self) -> bool: ...
