from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    testing: bool = False
    dev_mode: bool = False
    master_token: str = ""
    public_key: str = """-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAoIH8F1sqJmWlgMwfhAXW
NPIC0byhOj5Q/hkutQriten84rgBsXL0//lKufmez6zh8QWwR7/uGeE/EwEFRId1
R4gR+JWpLffhsILZkjQEzDPzhYQvPrqRVCeOxH70B85QSYaKlKNnWaFL5Oov9IKU
FE64zdXEGda9BHpZ4EBX57m5+whKg+iiRJEFdIHiXpVX56fLehH9opa7DiGpg8U7
/LTWDGOSpzCXpYa+DNVZ4oesCWIefzAxkFTkUisJmymnCmrgGUa0NdxGkaB2lpZs
I68gq5R3BOf6Gc8omeDqO5EyLB072cks8iVH/ZLfiIT6I0bCUkvZsD1KMAVfoMU+
5Z/SVo0tEumOj+GXvhBksZI03q6RUJvyIwWLkOBdl28TmStWa2b0FNhNQBzeICO6
Il1ovo3sZYS2Jqy6dnHLCwbR0sTCUXsQp1njo/UAlW6BnVHKoL3KfFnm9s2v6An7
tEBHHtm7hvHcq0zzYFUoExfFSNci4Sxvai7pGGkIl9omt8zoAGmaiCzSPE0PeY02
Dtu/C2i0euc+MKe5yZ45hHdDKLFEYltA+i/yLVNIJp6FgwzlboUn/wGApspMbDmz
dmCgNOR9KYCjpmX75DY00Exb64r+/Y7EJ4ER+Pru0BexcmGwfOOcWcZUbgt0JcpC
zznTozHbhYaWWIEX9kYHAccCAwEAAQ==
-----END PUBLIC KEY-----"""
    logfire_token: Optional[str] = None
    database_url: str = "postgresql://postgres@localhost:5432/onlybrands"
    world_app_id: str = "app_staging_36f4ed912bf5790caf5fdb754bc5bf3c"

    model_config = SettingsConfigDict(env_file=".env", extra="allow")
