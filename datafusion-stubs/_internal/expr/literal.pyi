from __future__ import annotations

from typing import Any

from datafusion._internal.expr import Expr
from datafusion._internal.sql.logical import LogicalPlan

class Literal:
    def data_type(self) -> str: ...
    def value_f32(self) -> float: ...
    def value_f64(self) -> float: ...
    def value_decimal128(self) -> tuple[int, int, int]: ...
    def value_i8(self) -> int: ...
    def value_i16(self) -> int: ...
    def value_i32(self) -> int: ...
    def value_i64(self) -> int: ...
    def value_u8(self) -> int: ...
    def value_u16(self) -> int: ...
    def value_u32(self) -> int: ...
    def value_u64(self) -> int: ...
    def value_date32(self) -> int: ...
    def value_date64(self) -> int: ...
    def value_time32(self) -> int: ...
    def value_timestamp(self) -> tuple[int, str]: ...
    def value_bool(self) -> bool: ...
    def value_string(self) -> str: ...
    def value_interval_day_time(self) -> tuple[int, int]: ...
    def into_type(self) -> Any: ...
    def __repr__(self) -> str: ...
