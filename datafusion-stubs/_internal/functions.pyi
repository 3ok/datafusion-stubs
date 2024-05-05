from __future__ import annotations

from typing import TYPE_CHECKING

from datafusion._internal.context import SessionContext
from datafusion._internal.expr import Expr
from datafusion._internal.expr.conditional_expr import CaseBuilder
from datafusion._internal.expr.window import WindowFrame

def isnan(expr: Expr) -> Expr: ...
def nullif(expr1: Expr, expr2: Expr) -> Expr: ...
def encode(input1: Expr, encoding: Expr) -> Expr: ...
def decode(input1: Expr, encoding: Expr) -> Expr: ...
def array_to_string(expr: Expr, delim: Expr) -> Expr: ...
def array_join(expr: Expr, delim: Expr) -> Expr: ...
def list_to_string(expr: Expr, delim: Expr) -> Expr: ...
def list_join(expr: Expr, delim: Expr) -> Expr: ...
def in_list(expr: Expr, value: list[Expr], negated: bool) -> Expr: ...
def digest(value: Expr, method: Expr) -> Expr: ...
def concat(*args: Expr) -> Expr: ...
def concat_ws(sep: str, *args: Expr) -> Expr: ...
def order_by(expr: Expr, asc: bool | None, nulls_first: bool | None) -> Expr: ...
def alias(expr: Expr, name: str) -> Expr: ...
def col(name: str) -> Expr: ...
def count_star() -> Expr: ...
def case(expr: Expr) -> CaseBuilder: ...
def window(
    name: str,
    args: list[Expr],
    partition_by: list[Expr] | None,
    order_by: list[Expr] | None,
    window_frame: WindowFrame | None,
    ctx: SessionContext,
) -> Expr: ...

# scalar functions
def abs(*args: Expr) -> Expr:
    """Return the absolute value of a given number.

    Returns
    -------
    Expr
        A new expression representing the absolute value of the input expression.
    """
    ...

def acos(*args: Expr) -> Expr:
    """Return the arc cosine or inverse cosine of a number.

    Returns
    -------
    Expr
        A new expression representing the arc cosine of the input expression.
    """
    ...
    
def acosh(*args: Expr) -> Expr: ...
def ascii(*args: Expr) -> Expr: ...
def asin(*args: Expr) -> Expr: ...
def asinh(*args: Expr) -> Expr: ...
def atan(*args: Expr) -> Expr: ...
def atanh(*args: Expr) -> Expr: ...
def atan2(*args: Expr) -> Expr: ...
def bit_length(*args: Expr) -> Expr: ...
def btrim(*args: Expr) -> Expr: ...
def cbrt(*args: Expr) -> Expr: ...
def ceil(*args: Expr) -> Expr: ...
def character_length(*args: Expr) -> Expr: ...
def length(*args: Expr) -> Expr: ...
def char_length(*args: Expr) -> Expr: ...
def chr(*args: Expr) -> Expr: ...
def coalesce(*args: Expr) -> Expr: ...
def cos(*args: Expr) -> Expr: ...
def cosh(*args: Expr) -> Expr: ...
def degrees(*args: Expr) -> Expr: ...
def exp(*args: Expr) -> Expr: ...
def factorial(*args: Expr) -> Expr: ...
def floor(*args: Expr) -> Expr: ...
def gcd(*args: Expr) -> Expr: ...
def initcap(*args: Expr) -> Expr: ...
def iszero(*args: Expr) -> Expr: ...
def lcm(*args: Expr) -> Expr: ...
def left(*args: Expr) -> Expr: ...
def ln(*args: Expr) -> Expr: ...
def log(*args: Expr) -> Expr: ...
def log10(*args: Expr) -> Expr: ...
def log2(*args: Expr) -> Expr: ...
def lower(*args: Expr) -> Expr: ...
def lpad(*args: Expr) -> Expr: ...
def ltrim(*args: Expr) -> Expr: ...
def md5(*args: Expr) -> Expr: ...
def nanvl(*args: Expr) -> Expr: ...
def octet_length(*args: Expr) -> Expr: ...
def pi(*args: Expr) -> Expr: ...
def power(*args: Expr) -> Expr: ...
def pow(*args: Expr) -> Expr: ...
def radians(*args: Expr) -> Expr: ...
def regexp_match(*args: Expr) -> Expr: ...
def regexp_replace(*args: Expr) -> Expr: ...
def repeat(*args: Expr) -> Expr: ...
def replace(*args: Expr) -> Expr: ...
def reverse(*args: Expr) -> Expr: ...
def right(*args: Expr) -> Expr: ...
def round(*args: Expr) -> Expr: ...
def rpad(*args: Expr) -> Expr: ...
def rtrim(*args: Expr) -> Expr: ...
def sha224(*args: Expr) -> Expr: ...
def sha256(*args: Expr) -> Expr: ...
def sha384(*args: Expr) -> Expr: ...
def sha512(*args: Expr) -> Expr: ...
def signum(*args: Expr) -> Expr: ...
def sin(*args: Expr) -> Expr: ...
def sinh(*args: Expr) -> Expr: ...
def split_part(*args: Expr) -> Expr: ...
def sqrt(*args: Expr) -> Expr: ...
def starts_with(*args: Expr) -> Expr: ...
def strpos(*args: Expr) -> Expr: ...
def substr(*args: Expr) -> Expr: ...
def tan(*args: Expr) -> Expr: ...
def tanh(*args: Expr) -> Expr: ...
def to_hex(*args: Expr) -> Expr: ...
def now(*args: Expr) -> Expr: ...
def to_timestamp(*args: Expr) -> Expr: ...
def to_timestamp_millis(*args: Expr) -> Expr: ...
def to_timestamp_micros(*args: Expr) -> Expr: ...
def to_timestamp_seconds(*args: Expr) -> Expr: ...
def current_date(*args: Expr) -> Expr: ...
def current_time(*args: Expr) -> Expr: ...
def datepart(*args: Expr) -> Expr: ...
def date_part(*args: Expr) -> Expr: ...
def date_trunc(*args: Expr) -> Expr: ...
def datetrunc(*args: Expr) -> Expr: ...
def date_bin(*args: Expr) -> Expr: ...
def translate(*args: Expr) -> Expr: ...
def trim(*args: Expr) -> Expr: ...
def trunc(*args: Expr) -> Expr: ...
def upper(*args: Expr) -> Expr: ...
def make_array(*args: Expr) -> Expr: ...
def array(*args: Expr) -> Expr: ...
def range(*args: Expr) -> Expr: ...
def uuid(*args: Expr) -> Expr: ...
def struct(*args: Expr) -> Expr: ...
def from_unixtime(*args: Expr) -> Expr: ...
def arrow_typeof(*args: Expr) -> Expr: ...
def random(*args: Expr) -> Expr: ...
def array_append(*args: Expr) -> Expr: ...
def array_push_back(*args: Expr) -> Expr: ...
def list_append(*args: Expr) -> Expr: ...
def list_push_back(*args: Expr) -> Expr: ...
def array_concat(*args: Expr) -> Expr: ...
def array_cat(*args: Expr) -> Expr: ...
def array_dims(*args: Expr) -> Expr: ...
def array_distinct(*args: Expr) -> Expr: ...
def list_distinct(*args: Expr) -> Expr: ...
def list_dims(*args: Expr) -> Expr: ...
def array_element(*args: Expr) -> Expr: ...
def array_extract(*args: Expr) -> Expr: ...
def list_element(*args: Expr) -> Expr: ...
def list_extract(*args: Expr) -> Expr: ...
def array_length(*args: Expr) -> Expr: ...
def list_length(*args: Expr) -> Expr: ...
def array_has(*args: Expr) -> Expr: ...
def array_has_all(*args: Expr) -> Expr: ...
def array_has_any(*args: Expr) -> Expr: ...
def array_position(*args: Expr) -> Expr: ...
def array_indexof(*args: Expr) -> Expr: ...
def list_position(*args: Expr) -> Expr: ...
def list_indexof(*args: Expr) -> Expr: ...
def array_positions(*args: Expr) -> Expr: ...
def list_positions(*args: Expr) -> Expr: ...
def array_ndims(*args: Expr) -> Expr: ...
def list_ndims(*args: Expr) -> Expr: ...
def array_prepend(*args: Expr) -> Expr: ...
def array_push_front(*args: Expr) -> Expr: ...
def list_prepend(*args: Expr) -> Expr: ...
def list_push_front(*args: Expr) -> Expr: ...
def array_pop_back(*args: Expr) -> Expr: ...
def array_pop_front(*args: Expr) -> Expr: ...
def array_remove(*args: Expr) -> Expr: ...
def list_remove(*args: Expr) -> Expr: ...
def array_remove_n(*args: Expr) -> Expr: ...
def list_remove_n(*args: Expr) -> Expr: ...
def array_remove_all(*args: Expr) -> Expr: ...
def list_remove_all(*args: Expr) -> Expr: ...
def array_repeat(*args: Expr) -> Expr: ...
def array_replace(*args: Expr) -> Expr: ...
def list_replace(*args: Expr) -> Expr: ...
def array_replace_n(*args: Expr) -> Expr: ...
def list_replace_n(*args: Expr) -> Expr: ...
def array_replace_all(*args: Expr) -> Expr: ...
def list_replace_all(*args: Expr) -> Expr: ...
def array_slice(*args: Expr) -> Expr: ...
def list_slice(*args: Expr) -> Expr: ...
def array_intersect(*args: Expr) -> Expr: ...
def list_intersect(*args: Expr) -> Expr: ...
def array_union(*args: Expr) -> Expr: ...
def list_union(*args: Expr) -> Expr: ...
def array_except(*args: Expr) -> Expr: ...
def list_except(*args: Expr) -> Expr: ...
def array_resize(*args: Expr) -> Expr: ...
def list_resize(*args: Expr) -> Expr: ...
def flatten(*args: Expr) -> Expr: ...

# aggregate functions
def approx_distinct(*args: Expr, distinct: bool = False) -> Expr: ...
def approx_median(*args: Expr, distinct: bool = False) -> Expr: ...
def approx_percentile_cont(*args: Expr, distinct: bool = False) -> Expr: ...
def approx_percentile_cont_with_weight(*args: Expr, distinct: bool = False) -> Expr: ...
def array_agg(*args: Expr, distinct: bool = False) -> Expr: ...
def avg(*args: Expr, distinct: bool = False) -> Expr: ...
def corr(*args: Expr, distinct: bool = False) -> Expr: ...
def count(*args: Expr, distinct: bool = False) -> Expr: ...
def covar(*args: Expr, distinct: bool = False) -> Expr: ...
def covar_pop(*args: Expr, distinct: bool = False) -> Expr: ...
def covar_samp(*args: Expr, distinct: bool = False) -> Expr: ...
def grouping(*args: Expr, distinct: bool = False) -> Expr: ...
def max(*args: Expr, distinct: bool = False) -> Expr: ...
def mean(*args: Expr, distinct: bool = False) -> Expr: ...
def median(*args: Expr, distinct: bool = False) -> Expr: ...
def min(*args: Expr, distinct: bool = False) -> Expr: ...
def sum(*args: Expr, distinct: bool = False) -> Expr: ...
def stddev(*args: Expr, distinct: bool = False) -> Expr: ...
def stddev_pop(*args: Expr, distinct: bool = False) -> Expr: ...
def stddev_samp(*args: Expr, distinct: bool = False) -> Expr: ...
def var(*args: Expr, distinct: bool = False) -> Expr: ...
def var_pop(*args: Expr, distinct: bool = False) -> Expr: ...
def var_samp(*args: Expr, distinct: bool = False) -> Expr: ...
def regr_avgx(*args: Expr, distinct: bool = False) -> Expr: ...
def regr_avgy(*args: Expr, distinct: bool = False) -> Expr: ...
def regr_count(*args: Expr, distinct: bool = False) -> Expr: ...
def regr_intercept(*args: Expr, distinct: bool = False) -> Expr: ...
def regr_r2(*args: Expr, distinct: bool = False) -> Expr: ...
def regr_slope(*args: Expr, distinct: bool = False) -> Expr: ...
def regr_sxx(*args: Expr, distinct: bool = False) -> Expr: ...
def regr_sxy(*args: Expr, distinct: bool = False) -> Expr: ...
def regr_syy(*args: Expr, distinct: bool = False) -> Expr: ...
def first_value(*args: Expr, distinct: bool = False) -> Expr: ...
def last_value(*args: Expr, distinct: bool = False) -> Expr: ...
def bit_and(*args: Expr, distinct: bool = False) -> Expr: ...
def bit_or(*args: Expr, distinct: bool = False) -> Expr: ...
def bit_xor(*args: Expr, distinct: bool = False) -> Expr: ...
def bool_and(*args: Expr, distinct: bool = False) -> Expr: ...
def bool_or(*args: Expr, distinct: bool = False) -> Expr: ...