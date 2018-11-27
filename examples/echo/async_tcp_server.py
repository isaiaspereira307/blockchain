#!/usr/bin/env python3

import asyncio

async def handle_echo(reader, writer):

    data = await reader.read(100)

    message = data.decode() 
    addr = writer.get_extra_info('peername')
    print("> 接收到数据 %r From %r" % (message, addr))

    print("> 发送数据: %r" % message)
    writer.write(data)
    await writer.drain()
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '127.0.0.1', 8888, loop=loop)
server = loop.run_until_complete(coro)
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass


server.close()
loop.run_until_complete(server.wait_closed())
loop.close()