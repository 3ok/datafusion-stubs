from __future__ import annotations

class DFSchema:
    @staticmethod
    def empty() -> DFSchema: ...
    def field_names(self) -> list[str]: ...