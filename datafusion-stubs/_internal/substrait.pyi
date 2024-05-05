from __future__ import annotations

from typing import Any
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datafusion._internal.context import SessionContext
    from datafusion._internal.sql.logical import LogicalPlan

class plan:
    def encode(self) -> bytes:
        """Encode the plan to bytes.

        Returns
        -------
        bytes
            Encoded plan.
        """
        ...

class serde:
    @staticmethod
    def serialize(sql: str, ctx: SessionContext, path: str) -> None:
        """Serialize a SQL query to a Substrait plan and write it to a file.

        Parameters
        ----------
        sql : str
            SQL query to serialize.
        ctx : SessionContext
            SessionContext to use.
        path : str
            Path to write the Substrait plan to.
        """
        ...

    @staticmethod
    def serialize_to_plan(sql: str, ctx: SessionContext) -> plan:
        """Serialize a SQL query to a Substrait plan.

        Parameters
        ----------
        sql : str
            SQL query to serialize.
        ctx : SessionContext
            SessionContext to use.

        Returns
        -------
        plan
            Substrait plan.
        """
        ...

    @staticmethod
    def serialize_bytes(sql: str, ctx: SessionContext) -> bytes:
        """Serialize a SQL query to a Substrait plan as bytes.

        Parameters
        ----------
        sql : str
            SQL query to serialize.
        ctx : SessionContext
            SessionContext to use.

        Returns
        -------
        bytes
            Substrait plan as bytes.
        """
        ...
        
    @staticmethod
    def deserialize(path: str) -> plan:
        """Deserialize a Substrait plan from a file.

        Parameters
        ----------
        path : str
            Path to read the Substrait plan from.

        Returns
        -------
        plan
            Substrait plan.
        """
        ...
    @staticmethod
    def deserialize_bytes(proto_bytes: bytes) -> plan:
        """Deserialize a Substrait plan from bytes.

        Parameters
        ----------
        proto_bytes : bytes
            Bytes to read the Substrait plan from.

        Returns
        -------
        plan
            Substrait plan.
        """
        ...

class producer:
    @staticmethod
    def to_substrait_plan(plan: LogicalPlan, ctx: SessionContext) -> plan:
        """Convert a DataFusion LogicalPlan to a Substrait plan.

        Parameters
        ----------
        plan : LogicalPlan
            LogicalPlan to convert.
        ctx : SessionContext
            SessionContext to use.

        Returns
        -------
        plan
            Substrait plan.
        """
        ...

class consumer:
    @staticmethod
    def from_substrait_plan(ctx: SessionContext, plan: plan) -> LogicalPlan:
        """Convert a Substrait plan to a DataFusion LogicalPlan.

        Parameters
        ----------
        ctx : SessionContext
            SessionContext to use.
        plan : plan
            Substrait plan to convert.

        Returns
        -------
        LogicalPlan
            LogicalPlan.
        """
        ...
