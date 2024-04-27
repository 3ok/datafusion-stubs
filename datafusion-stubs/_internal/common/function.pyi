from __future__ import annotations

from datafusion._internal.common.data_type import DataType

class SqlFunction:
    def __init__(
        self,
        function_name: str,
        input_types: list[DataType],
        return_type: DataType,
        aggregation_bool: bool,
    ) -> None: ...
    def add_type_mapping(
        self, input_types: list[DataType], return_type: DataType
    ) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def return_types(self) -> dict[list[DataType], DataType]: ...
    @property
    def aggregation(self) -> bool: ...
