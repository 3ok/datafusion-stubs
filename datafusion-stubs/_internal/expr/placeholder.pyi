from __future__ import annotations

from datafusion._internal.common.data_type import DataType

class Placeholder:
    def id(self) -> str: ...
    def data_type(self) -> DataType: ...
