import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { RgbppController } from './rgbpp/rgbpp.controller';

@Module({
  imports: [],
  controllers: [AppController, RgbppController],
  providers: [AppService],
})
export class AppModule {}
