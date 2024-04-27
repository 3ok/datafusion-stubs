from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pyarrow as pa

class RecordBatch:
    def to_pyarrow(self) -> pa.RecordBatch: ...

class RecordBatchStream:
    def next(self) -> RecordBatch | None: ...
    def __next__(self) -> RecordBatch | None: ...
    def __iter__(self) -> RecordBatchStream: ...
