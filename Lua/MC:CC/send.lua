local modem = peripheral.wrap("right")

write("Sender Channel: ")
local senderChannel = tonumber(read())

write("Reply Channel: ")
local replyChannel = tonumber(read())

write("Message: ")
local message = read()

modem.transmit(senderChannel, replyChannel, message)
