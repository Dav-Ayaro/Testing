import asyncio

class ChatServer:
    def __init__(self):
        self.clients = []

    def register_client(self, client_writer):
        self.clients.append(client_writer)

    def unregister_client(self, client_writer):
        self.clients.remove(client_writer)

    def broadcast_message(self, sender, message):
        for client in self.clients:
            if client != sender:
                client.write(f'{sender}: {message}\n'.encode())

class ChatClient:
    def __init__(self, reader, writer, server):
        self.reader = reader
        self.writer = writer
        self.server = server

    def send_message(self, message):
        self.writer.write(message.encode())

    async def process_input(self):
        while True:
            message = (await self.reader.readline()).decode().strip()
            if not message:
                break
            self.server.broadcast_message(self.writer, message)

        self.server.unregister_client(self.writer)
        self.writer.close()

async def handle_client(reader, writer, server):
    client = ChatClient(reader, writer, server)
    server.register_client(writer)

    await client.process_input()

async def start_chat_server():
    server = ChatServer()
    chat_server = await asyncio.start_server(
        lambda r, w: handle_client(r, w, server),
        '127.0.0.1',
        8888
    )
    addr = chat_server.sockets[0].getsockname()
    print(f'Server running on {addr}')

    async with chat_server:
        await chat_server.serve_forever()

async def start_chat_client(name):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    writer.write(f'{name}\n'.encode())
    await writer.drain()

    async def send_message(message):
        writer.write(f'{message}\n'.encode())
        await writer.drain()

    async def receive_messages():
        while True:
            message = (await reader.readline()).decode()
            if not message:
                break
            print(message.strip())

    await asyncio.gather(send_message_loop(send_message), receive_messages())

async def send_message_loop(send_message):
    while True:
        message = input()
        await send_message(message)

async def main():
    tasks = [
        asyncio.create_task(start_chat_server()),
        asyncio.create_task(start_chat_client('Alice')),
        asyncio.create_task(start_chat_client('Bob')),
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
