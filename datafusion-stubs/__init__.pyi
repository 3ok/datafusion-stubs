from __future__ import annotations

import abc

from typing import Any
from typing import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pyarrow as pa

from datafusion._internal import AggregateUDF as AggregateUDF
from datafusion._internal import Config as Config
from datafusion._internal import DataFrame as DataFrame
from datafusion._internal import SessionContext as SessionContext
from datafusion._internal import SessionConfig as SessionConfig
from datafusion._internal import RuntimeConfig as RuntimeConfig
from datafusion._internal import ScalarUDF as ScalarUDF
from datafusion._internal import SQLOptions as SQLOptions

from datafusion.common import DFField as DFField
from datafusion.common import DFSchema as DFSchema

from datafusion.expr import Expr
from datafusion.expr import Alias as Alias
from datafusion.expr import Analyze as Analyze
from datafusion.expr import Expr as Expr
from datafusion.expr import Filter as Filter
from datafusion.expr import Limit as Limit
from datafusion.expr import Like as Like
from datafusion.expr import ILike as ILike
from datafusion.expr import Projection as Projection
from datafusion.expr import SimilarTo as SimilarTo
from datafusion.expr import ScalarVariable as ScalarVariable
from datafusion.expr import Sort as Sort
from datafusion.expr import TableScan as TableScan
from datafusion.expr import GetIndexedField as GetIndexedField
from datafusion.expr import Not as Not
from datafusion.expr import IsNotNull as IsNotNull
from datafusion.expr import IsTrue as IsTrue
from datafusion.expr import IsFalse as IsFalse
from datafusion.expr import IsUnknown as IsUnknown
from datafusion.expr import IsNotTrue as IsNotTrue
from datafusion.expr import IsNotFalse as IsNotFalse
from datafusion.expr import IsNotUnknown as IsNotUnknown
from datafusion.expr import Negative as Negative
from datafusion.expr import ScalarFunction as ScalarFunction
from datafusion.expr import BuiltinScalarFunction as BuiltinScalarFunction
from datafusion.expr import InList as InList
from datafusion.expr import Exists as Exists
from datafusion.expr import Subquery as Subquery
from datafusion.expr import InSubquery as InSubquery
from datafusion.expr import ScalarSubquery as ScalarSubquery
from datafusion.expr import GroupingSet as GroupingSet
from datafusion.expr import Placeholder as Placeholder
from datafusion.expr import Case as Case
from datafusion.expr import Cast as Cast
from datafusion.expr import TryCast as TryCast
from datafusion.expr import Between as Between
from datafusion.expr import Explain as Explain
from datafusion.expr import CreateMemoryTable as CreateMemoryTable
from datafusion.expr import SubqueryAlias as SubqueryAlias
from datafusion.expr import Extension as Extension
from datafusion.expr import CreateView as CreateView
from datafusion.expr import Distinct as Distinct
from datafusion.expr import DropTable as DropTable
from datafusion.expr import Repartition as Repartition
from datafusion.expr import Partitioning as Partitioning
from datafusion.expr import Window as Window
from datafusion.expr import WindowFrame as WindowFrame


from datafusion._internal import ScalarUDF
from datafusion._internal import AggregateUDF
from datafusion._internal import DataFrame as DataFrame
from datafusion._internal import SessionContext as SessionContext


__version__: str

class Accumulator(abc.ABC):
    @abc.abstractmethod
    def state(self) -> list[pa.Scalar[Any]]: ...
    @abc.abstractmethod
    def update(self, values: pa.Array[Any, Any]) -> None: ...
    @abc.abstractmethod
    def merge(self, states: pa.Array[Any, Any]) -> None: ...
    @abc.abstractmethod
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
