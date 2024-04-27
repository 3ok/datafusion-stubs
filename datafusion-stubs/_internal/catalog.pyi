from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pyarrow as pa

class Catalog:
    def names(self) -> list[str]: ...
    def database(self, name: str = "public") -> Database: ...
    def __repr__(self) -> str: ...

class Database:
    def names(self) -> set[str]: ...
    def table(self, name: str) -> Table: ...
    def __repr__(self) -> str: ...

class Table:
    def schema(self) -> pa.Schema: ...
    @property
    def kind(self) -> str: ...
    def __repr__(self) -> str: ...