import { Controller } from '@nestjs/common';
import { GrpcMethod } from '@nestjs/microservices';
import { buildRgbppLockArgs } from '@rgbpp-sdk/ckb';

interface RgbppLockParams {
  outIndex: number;
  btcTxId: string;
}

@Controller()
export class RgbppController {
  @GrpcMethod('RgbppSdkService', 'BuildRgbppLockArgs')
  async buildRgbppLockArgs({ outIndex, btcTxId }: RgbppLockParams) {
    console.log('outIndex:', outIndex, 'btcTxId:', btcTxId);
    const rgbppLockArgs = buildRgbppLockArgs(outIndex, btcTxId);
    return {
      args: rgbppLockArgs,
    };
  }
}
