from typing import Any, Optional
from . import base

class TLConnection(base.Connection):
    def __init__(self, *arg, **kw) -> None: ...
    def close(self): ...

class TLEngine(base.Engine):
    def __init__(self, *args, **kwargs) -> None: ...
    def contextual_connect(self, **kw): ...
    def begin_twophase(self, xid: Optional[Any] = ...): ...
    def begin_nested(self): ...
    def begin(self): ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback): ...
    def prepare(self): ...
    def commit(self): ...
    def rollback(self): ...
    def dispose(self): ...
    @property
    def closed(self): ...
    def close(self): ...