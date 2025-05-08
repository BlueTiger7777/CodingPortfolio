from websocket_server import WebsocketServer
clients = []

# Called when client connects
def new_client(client, server):
    print("New client connected and was given id %d" % client['id'])
    clients.append(None)

# Called when client disconnects
def client_left(client, server):
    print("Client(id: %d) disconnected" % client['id'])

# Called when a client sends a message
def message_received(client, server, message):
    print("Client(id: %d) said: %s" % (client['id'], message))
    if clients[client['id']-1] == None:
        clients[client['id']-1] = message
        return
    if message != "ACK" or message != "FIN":
        server.send_message_to_all(message)

# Sets and runs a local websocket
PORT=9001
server = WebsocketServer(port = PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
