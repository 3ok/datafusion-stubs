from __future__ import annotations

from typing import Any
from typing import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pyarrow as pa

from datafusion.expr import Expr
from datafusion._internal import ScalarUDF
from datafusion._internal import AggregateUDF
from datafusion._internal import DataFrame as DataFrame
from datafusion._internal import SessionContext as SessionContext

class Accumulator:
    def state(self) -> list[pa.Scalar[Any]]: ...
    def update(self, values: pa.Array[Any, Any]) -> None: ...
    def merge(self, states: pa.Array[Any, Any]) -> None: ...
    def evaluate(self) -> pa.Scalar[Any]: ...

def column(value: str) -> Expr: ...
def col(value: str) -> Expr: ...
def literal(value: Any) -> Expr: ...
def lit(value: Any) -> Expr: ...
def udf(
    func: Callable[[Any], Any],
    input_types: list[pa.DataType[Any]],
    return_type: pa.DataType[Any],
    volatility: str,
    name: str | None = None,
) -> ScalarUDF: ...
def udaf(
    accum: Accumulator,
    input_type: list[pa.DataType[Any]],
    return_type: pa.DataType[Any],
    state_type: list[pa.DataType[Any]],
    volatility: str,
    name: str | None = None,
) -> AggregateUDF: ...
