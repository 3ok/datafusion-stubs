from __future__ import annotations

from typing import Any
from typing import TYPE_CHECKING

from datafusion._internal.common.data_type import DataTypeMap, RexType
from datafusion._internal.expr.bool_expr import Not as Not
from datafusion._internal.expr.filter import Filter as Filter
from datafusion._internal.expr.extension import Extension as Extension
from datafusion._internal.expr.aggregate import Aggregate as Aggregate
from datafusion._internal.expr.aggregate_expr import (
    AggregateFunction as AggregateFunction,
)
from datafusion._internal.expr.alias import Alias as Alias
from datafusion._internal.expr.analyze import Analyze as Analyze
from datafusion._internal.expr.between import Between as Between
from datafusion._internal.expr.binary_expr import BinaryExpr as BinaryExpr
from datafusion._internal.expr.bool_expr import (
    IsFalse as IsFalse,
    IsNotFalse as IsNotFalse,
    IsNotNull as IsNotNull,
    IsNotTrue as IsNotTrue,
    IsNotUnknown as IsNotUnknown,
    IsNull as IsNull,
    IsTrue as IsTrue,
    IsUnknown as IsUnknown,
    Negative as Negative,
)
from datafusion._internal.expr.case import Case as Case
from datafusion._internal.expr.cast import Cast as Cast, TryCast as TryCast
from datafusion._internal.expr.column import Column as Column
from datafusion._internal.expr.create_memory_table import (
    CreateMemoryTable as CreateMemoryTable,
)
from datafusion._internal.expr.create_view import CreateView as CreateView
from datafusion._internal.expr.cross_join import CrossJoin as CrossJoin
from datafusion._internal.expr.distinct import Distinct as Distinct
from datafusion._internal.expr.drop_table import DropTable as DropTable
from datafusion._internal.expr.empty_relation import EmptyRelation as EmptyRelation
from datafusion._internal.expr.exists import Exists as Exists
from datafusion._internal.expr.explain import Explain as Explain
from datafusion._internal.expr.grouping_set import GroupingSet as GroupingSet
from datafusion._internal.expr.in_list import InList as InList
from datafusion._internal.expr.in_subquery import InSubquery as InSubquery
from datafusion._internal.expr.indexed_field import GetIndexedField as GetIndexedField
from datafusion._internal.expr.join import (
    Join as Join,
    JoinConstraint as JoinConstraint,
    JoinType as JoinType,
)
from datafusion._internal.expr.like import (
    ILike as ILike,
    Like as Like,
    SimilarTo as SimilarTo,
)
from datafusion._internal.expr.limit import Limit as Limit
from datafusion._internal.expr.literal import Literal as Literal
from datafusion._internal.expr.placeholder import Placeholder as Placeholder
from datafusion._internal.expr.projection import Projection as Projection
from datafusion._internal.expr.repartition import (
    Partitioning as Partitioning,
    Repartition as Repartition,
)
from datafusion._internal.expr.scalar_function import (
    BuiltinScalarFunction as BuiltinScalarFunction,
    ScalarFunction as ScalarFunction,
)
from datafusion._internal.expr.scalar_subquery import ScalarSubquery as ScalarSubquery
from datafusion._internal.expr.scalar_variable import ScalarVariable as ScalarVariable
from datafusion._internal.expr.sort import Sort as Sort
from datafusion._internal.expr.subquery import Subquery as Subquery
from datafusion._internal.expr.subquery_alias import SubqueryAlias as SubqueryAlias
from datafusion._internal.expr.table_scan import TableScan as TableScan
from datafusion._internal.expr.union import Union as Union
from datafusion._internal.expr.window import (
    Window as Window,
    WindowFrame as WindowFrame,
    WindowFrameBound as WindowFrameBound,
)

if TYPE_CHECKING:
    from datafusion._internal.sql.logical import LogicalPlan
    import pyarrow as pa

class Expr:
    def to_variant(self) -> Any: ...
    def display_name(self) -> str: ...
    def canonical_name(self) -> str: ...
    def variant_name(self) -> str: ...
    def __richcmp__(self, other: Expr, op: int) -> Expr: ...
    def __repr__(self) -> str: ...
    def __add__(self, rhs: Expr) -> Expr: ...
    def __sub__(self, rhs: Expr) -> Expr: ...
    def __truediv__(self, rhs: Expr) -> Expr: ...
    def __mul__(self, rhs: Expr) -> Expr: ...
    def __mod__(self, rhs: Expr) -> Expr: ...
    def __and__(self, rhs: Expr) -> Expr: ...
    def __or__(self, rhs: Expr) -> Expr: ...
    def __invert__(self) -> Expr: ...
    def __getitem__(self, key: str) -> Expr: ...
    @staticmethod
    def literal(value: Any) -> Expr: ...
    @staticmethod
    def column(value: str) -> Expr: ...
    def alias(self, name: str) -> Expr: ...
    def sort(self, ascending: bool = True, nulls_first: bool = True) -> Expr: ...
    def is_null(self) -> Expr: ...
    def cast(self, to: pa.DataType[Any]) -> Expr: ...
    def rex_type(self) -> RexType: ...
    def types(self) -> DataTypeMap: ...
    def python_value(self) -> Any: ...
    def rex_call_operands(self) -> list[Expr]: ...
    def rex_call_operator(self) -> str: ...
    def column_name(self, plan: LogicalPlan) -> str: ...
