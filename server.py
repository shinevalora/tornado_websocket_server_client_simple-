# _*_coding:utf-8_*_
#  创建时间: 2019/7/18  10:04

import logging
import asyncio
from datetime import datetime

from tornado import ioloop,web,websocket

date_time=None

logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)-8s: %(message)s")

class WSHandler(websocket.WebSocketHandler):
    def check_origin(self, origin: str):
        return True

    def open(self, *args: str, **kwargs: str):
        logging.info("WebSocket opened")


    async def on_message(self,message):
        await asyncio.sleep(1)

        date_time = datetime.now()

        await self.write_message(f" the server datetime now is {date_time}")


    def on_close(self):
        logging.info("WebSocket closed")


def make_up():
    router=[
        (r'/ws',WSHandler)
    ]

    app=web.Application(router)
    app.listen(9991)

    return app


if __name__ == '__main__':
    make_up()
    logging.info("The server is running now  ...... ")
    ioloop.IOLoop.current().start()
