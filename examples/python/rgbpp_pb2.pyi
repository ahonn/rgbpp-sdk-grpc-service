from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RgbppLockParams(_message.Message):
    __slots__ = ("outIndex", "btcTxId")
    OUTINDEX_FIELD_NUMBER: _ClassVar[int]
    BTCTXID_FIELD_NUMBER: _ClassVar[int]
    outIndex: int
    btcTxId: str
    def __init__(self, outIndex: _Optional[int] = ..., btcTxId: _Optional[str] = ...) -> None: ...

class RgbppLockArgs(_message.Message):
    __slots__ = ("args",)
    ARGS_FIELD_NUMBER: _ClassVar[int]
    args: str
    def __init__(self, args: _Optional[str] = ...) -> None: ...
