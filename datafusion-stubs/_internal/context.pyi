from __future__ import annotations

from typing import Any
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pyarrow as pa
    import pandas as pd
    import polars as pl  # type: ignore [import-not-found]

    from pyarrow import dataset

    from datafusion._internal.physical_plan import ExecutionPlan
    from datafusion._internal.record_batch import RecordBatchStream
    from datafusion._internal.sql.logical import LogicalPlan
    from datafusion._internal.dataframe import DataFrame
    from datafusion._internal.expr import Expr
    from datafusion._internal.udf import ScalarUDF
    from datafusion._internal.udaf import AggregateUDF
    from datafusion._internal.catalog import Catalog
    from datafusion._internal.catalog import Table

class SessionConfig:
    def __init__(self, config_options: dict[str, str]) -> None: ...
    def with_create_default_catalog_and_schema(
        self, enabled: bool
    ) -> SessionConfig: ...
    def with_default_catalog_and_schema(
        self, catalog: str, schema: str
    ) -> SessionConfig: ...
    def with_information_schema(self, enabled: bool) -> SessionConfig: ...
    def with_batch_size(self, batch_size: int) -> SessionConfig: ...
    def with_target_partitions(self, target_partitions: int) -> SessionConfig: ...
    def with_repartition_aggregations(self, enabled: bool) -> SessionConfig: ...
    def with_repartition_joins(self, enabled: bool) -> SessionConfig: ...
    def with_repartition_windows(self, enabled: bool) -> SessionConfig: ...
    def with_repartition_sorts(self, enabled: bool) -> SessionConfig: ...
    def with_repartition_file_scans(self, enabled: bool) -> SessionConfig: ...
    def with_repartition_file_min_size(self, size: int) -> SessionConfig: ...
    def with_parquet_pruning(self, enabled: bool) -> SessionConfig: ...
    def set(self, key: str, value: str) -> SessionConfig: ...

class RuntimeConfig:
    def __init__(self) -> None: ...
    def with_disk_manager_disabled(self) -> RuntimeConfig: ...
    def with_disk_manager_os(self) -> RuntimeConfig: ...
    def with_disk_manager_specified(self, paths: list[str]) -> RuntimeConfig: ...
    def with_unbounded_memory_pool(self) -> RuntimeConfig: ...
    def with_fair_spill_pool(self, size: int) -> RuntimeConfig: ...
    def with_greedy_memory_pool(self, size: int) -> RuntimeConfig: ...
    def with_temp_file_path(self, path: str) -> RuntimeConfig: ...

class SQLOptions:
    def __init__(self) -> None: ...
    def with_allow_ddl(self, allow: bool) -> SQLOptions: ...
    def with_allow_dml(self, allow: bool) -> SQLOptions: ...
    def with_allow_statements(self, allow: bool) -> SQLOptions: ...

class SessionContext:
    def __init__(
        self, config: SessionConfig | None = None, runtime: RuntimeConfig | None = None
    ) -> None:
        """Main interface for executing queries with DataFusion.

        Maintains the state of the connection between a user and an instance
        of the connection between a user and an instance of the DataFusion
        engine.

        Examples
        --------
        The following example demostrates how to use the context to execute
        a query against a CSV data source using the `DataFrame` API:

        ```python
        from datafusion import SessionContext

        ctx = SessionContext()
        df = ctx.read_csv("data.csv")
        ```

        Parameters
        ----------
        config : SessionConfig | None
            Session configuration options.
        runtime : RuntimeConfig | None
            Runtime configuration options.
        """
        ...

    def register_object_store(
        self, scheme: str, store: Any, host: str | None
    ) -> None: ...
    def register_listing_table(
        self,
        name: str,
        path: str,
        table_partition_cols: list[tuple[str, str]] = ...,
        file_extension: str = ".parquet",
        schema: pa.Schema | None = None,
        file_sort_order: list[list[Expr]] | None = None,
    ) -> None: ...
    def sql(self, query: str) -> DataFrame: ...
    def sql_with_options(self, query: str, options: SQLOptions) -> DataFrame: ...
    def create_dataframe(
        self,
        partitions: list[list[pa.RecordBatch]],
        name: str | None,
        schema: pa.Schema | None,
    ) -> DataFrame: ...
    def creat_dataframe_from_logical_plan(self, plan: LogicalPlan) -> DataFrame: ...
    def from_pylist(
        self, data: list[dict[str, Any]], name: str | None
    ) -> DataFrame: ...
    def from_pydict(
        self, data: dict[str, list[Any]], name: str | None
    ) -> DataFrame: ...
    def from_arrow_table(self, data: pa.Table, name: str | None) -> DataFrame: ...
    def from_pandas(self, data: pd.DataFrame, name: str | None) -> DataFrame: ...
    def from_polars(self, data: pl.DataFrame, name: str | None) -> DataFrame: ...
    def register_table(self, name: str, table: pa.Table) -> None: ...
    def deregister_table(self, name: str) -> None: ...
    def register_record_batches(
        self, name: str, partitions: list[list[pa.RecordBatch]]
    ) -> None: ...
    def register_parquet(
        self,
        name: str,
        path: str,
        table_partition_cols: list[tuple[str, str]] = ...,
        parquet_pruning: bool = True,
        file_extension: str = ".parquet",
        skip_metadata: bool = True,
        schema: pa.Schema | None = None,
        file_sort_order: list[list[Expr]] | None = None,
    ) -> None: ...
    def register_csv(
        self,
        name: str,
        path: str,
        schema: pa.Schema | None = None,
        has_header: bool = True,
        delimiter: str = ",",
        schema_infer_max_records: int = 1000,
        file_extension: str = ".csv",
        file_compression_type: str | None = None,
    ) -> None: ...
    def register_json(
        self,
        name: str,
        path: str,
        schema: pa.Schema | None = None,
        schema_infer_max_records: int = 1000,
        file_extension: str = ".json",
        table_partition_cols: list[tuple[str, str]] = ...,
        file_compression_type: str | None = None,
    ) -> None: ...
    def register_avro(
        self,
        name: str,
        path: str,
        schema: pa.Schema | None = None,
        file_extension: str = ".avro",
        table_partition_cols: list[tuple[str, str]] = ...,
    ) -> None: ...
    def register_dataset(self, name: str, dataset: dataset.Dataset) -> None: ...
    def register_udf(self, udf: ScalarUDF) -> None: ...
    def register_udaf(self, udaf: AggregateUDF) -> None: ...
    def catalog(self, name: str) -> Catalog: ...
    def tables(self) -> set[str]: ...
    def table(self, name: str) -> DataFrame: ...
    def table_exist(self, name: str) -> bool: ...
    def empty_table(self) -> DataFrame: ...
    def session_id(self) -> str: ...
    def read_json(
        self,
        path: str,
        schema: pa.Schema | None = None,
        schema_infer_max_records: int = 1000,
        file_extension: str = ".json",
        table_partition_cols: list[tuple[str, str]] = ...,
        file_compression_type: str | None = None,
    ) -> DataFrame: ...
    def read_csv(
        self,
        path: str,
        schema: pa.Schema | None = None,
        has_header: bool = True,
        delimiter: str = ",",
        schema_infer_max_records: int = 1000,
        file_extension: str = ".csv",
        table_partition_cols: list[tuple[str, str]] = ...,
        file_compression_type: str | None = None,
    ) -> DataFrame:
        """Create a `DataFrame` for reading a CSV data source.

        Parameters
        ----------
        path : str
            Path to the CSV file
        schema : pa.Schema | None, optional
            An optional schema representing the CSV files. If None, the CSV reader will try to infer it based on data in file, by default None
        has_header : bool, optional
            Whether the CSV file have a header. If schema inference is run on a file with no headers, default column names are created, by default True
        delimiter : str, optional
            An optional column delimiter, by default ","
        schema_infer_max_records : int, optional
            Maximum number of rows to read from CSV files for schema inference if needed, by default 1000
        file_extension : str, optional
            File extensions; only files with this extension are selected for data input, by default ".csv"
        table_partition_cols : list[tuple[str, str]], optional
            Partition columns, by default ...
        file_compression_type : str | None, optional
            File compression type, by default None

        Returns
        -------
        DataFrame
            DataFrame representation of the read CSV files
        """
        ...

    def read_parquet(
        self,
        table_partition_cols: list[tuple[str, str]] = ...,
        parquet_pruning: bool = True,
        file_extension: str = ".parquet",
        skip_metadata: bool = True,
        schema: pa.Schema | None = None,
        file_sort_order: list[list[Expr]] | None = None,
    ) -> DataFrame: ...
    def read_avro(
        self,
        path: str,
        schema: pa.Schema | None = None,
        file_partition_cols: list[tuple[str, str]] = ...,
        file_extension: str = ".avro",
    ) -> DataFrame: ...
    def read_table(self, table: Table) -> DataFrame: ...
    def __repr__(self) -> str: ...
    def execute(self, plan: ExecutionPlan, part: int) -> RecordBatchStream: ...
