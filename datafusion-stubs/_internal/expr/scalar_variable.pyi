from __future__ import annotations

from datafusion._internal.common.data_type import DataType
from datafusion._internal.expr import Expr
from datafusion._internal.sql.logical import LogicalPlan

class ScalarVariable:
    def data_type(self) -> DataType: ...
    def variables(self) -> list[str]: ...
    def __repr__(self) -> str: ...
