https://grpc.io/docs/languages/python/quickstart/

## Generate gRPC code

```
python -m grpc_tools.protoc -I../src/rgbpp --python_out=. --pyi_out=. --grpc_python_out=. ../src/rgbpp/rgbpp.proto
```
