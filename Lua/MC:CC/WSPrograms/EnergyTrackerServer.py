from websocket_server import WebsocketServer
import decimal
clientJob = []

# Called for every client connecting (after handshake)
def new_client(client, server):
    clientJob.append(None)
    print("New client connected and was given id %d" % client['id'])
    server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
    print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
    if len(message) > 200:
        message = message[:200]+'..'
    if clientJob[client['id']-1] == None:
        clientJob[client['id']-1] = message
        print("Client(%d) declared themself as a %s" % (client['id'], clientJob[client['id']-1]))
        return
    if clientJob[client['id']-1] == "Tracker":
        vals = message.split()
        for i in range(len(vals)):
            vals[i] = decimal.Decimal(round(float(vals[i]),-len(vals[i])+5)).normalize().to_eng_string().replace("E", "e")
        server.send_message_to_all(f'Webapp {vals[0]} {vals[1]} {vals[2]} {vals[3]} {vals[4]}')
    print("Client(%d) said: %s" % (client['id'], message))


PORT=9001
server = WebsocketServer(port = PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
