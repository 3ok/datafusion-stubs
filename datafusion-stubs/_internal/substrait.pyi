from __future__ import annotations

from typing import Any
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datafusion._internal.context import SessionContext
    from datafusion._internal.sql.logical import LogicalPlan

class plan:
    def encode(self) -> Any: ...

class serde:
    @staticmethod
    def serialize(sql: str, ctx: SessionContext, path: str) -> None: ...
    @staticmethod
    def serialize_to_plan(sql: str, ctx: SessionContext) -> plan: ...
    @staticmethod
    def serialize_bytes(sql: str, ctx: SessionContext) -> bytes: ...
    @staticmethod
    def deserialize(path: str) -> plan: ...
    @staticmethod
    def deserialize_bytes(proto_bytes: bytes) -> plan: ...

class producer:
    @staticmethod
    def to_substrait_plan(plan: LogicalPlan, ctx: SessionContext) -> plan: ...

class consumer:
    @staticmethod
    def from_substrait_plan(plan: plan, ctx: SessionContext) -> LogicalPlan: ...
