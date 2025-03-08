local modem = peripheral.wrap("back")
 
write("Channel to open: ")
local openChannel = tonumber(read())
 
modem.open(openChannel)
 
local event, modemSide, senderChannel, replyChannel, message, senderDistance = os.pullEvent("modem_message")
 
print("I just received a message on channel: "..senderChannel)
print("I should apparently reply on channel: "..replyChannel)
print("The modem reciving this is located on my "..modemSide.." side")
print("The message was: "..message)
print("The sender is: "..(senderDistance or "an unknown number of").." blocks away from me.")
