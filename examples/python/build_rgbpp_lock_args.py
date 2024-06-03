from __future__ import print_function

import asyncio
import logging

import grpc
import rgbpp_pb2
import rgbpp_pb2_grpc


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        print(channel)
        stub = rgbpp_pb2_grpc.RgbppSdkServiceStub(channel)
        response = await stub.BuildRgbppLockArgs(rgbpp_pb2.RgbppLockParams(
            outIndex=1,
            btcTxId="4ff1855b64b309afa19a8b9be3d4da99dcb18b083b65d2d851662995c7d99e7a"
        ))
    print("BuildRgbppLockArgs: " + response.args)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())
