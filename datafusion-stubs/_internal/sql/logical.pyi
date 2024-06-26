from __future__ import annotations

from typing import Any

class LogicalPlan:
    def to_variant(self) -> Any: ...
    def inputs(self) -> list[LogicalPlan]: ...
    def __repr__(self) -> str: ...
    def display(self) -> str: ...
    def display_indent(self) -> str: ...
    def display_indent_schema(self) -> str: ...
    def display_graphviz(self) -> str: ...
