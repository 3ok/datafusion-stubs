from __future__ import annotations

class LocalFileSystem:
    def __init__(self, prefix: str) -> None: ...

class MicrosoftAzure:
    def __init__(
        self,
        container_name: str,
        account: str | None = None,
        access_key: str | None = None,
        bearer_token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        tenant_id: str | None = None,
        sas_query_pairs: list[tuple[str, str]] | None = None,
        use_emulator: bool | None = None,
        allow_http: bool | None = None,
    ) -> None: ...

class GoogleCloud:
    def __init__(
        self, bucket_name: str, service_account_path: str | None = None
    ) -> None: ...

class AmazonS3:
    def __init__(
        self,
        bucket_name: str,
        region: str | None,
        access_key_id: str | None,
        secret_access_key: str | None,
        endpoint: str | None,
        allow_http: bool = False,
        imdsv1_fallback: bool = False,
    ) -> None: ...
