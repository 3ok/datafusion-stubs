from __future__ import annotations

from typing import Any
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pyarrow as pa

    from datafusion._internal.expr import Expr

class AggregateUDF:
    def __init__(
        self,
        name: str,
        accumulator: Any,
        input_type: list[pa.DataType[Any]],
        return_type: pa.DataType[Any],
        state_type: list[pa.DataType[Any]],
        volatility: str,
    ) -> None: ...
    def __call__(self, *args: Expr) -> Expr: ...
    def __repr__(self) -> str: ...
