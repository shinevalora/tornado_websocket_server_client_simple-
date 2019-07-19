# _*_coding:utf-8_*_
#  创建时间: 2019/7/18  13:37


import logging
import asyncio

from tornado.websocket import websocket_connect
from server import date_time


logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)-8s: %(message)s")

async def main():
    url="ws://127.0.0.1:9991/ws"
    conn=await websocket_connect(url)

    while True:

        await conn.write_message(f"从server中获取到的时间为 ：{date_time}")


        msg=await conn.read_message()

        logging.info(f"msg is {msg}")


if __name__ == '__main__':
    asyncio.run(main())