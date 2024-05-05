from __future__ import annotations

from datafusion._internal.expr import Expr

class BinaryExpr:
    def left(self) -> Expr: ...
    def right(self) -> Expr: ...
    def op(self) -> str: ...
    def __repr__(self) -> str: ...