term.clear()

term.setCursorPos(1, 1)
write("Side of modem: ")
local modem = peripheral.wrap(read())

term.setCursorPos(1, 2)
write("Channel to connect: ")
local channel = tonumber(read())

term.setCursorPos(1, 3)
write("Username: ")
local name = read()

term.setCursorPos(1, 4)
term.write("Checking if "..channel.." is up")

--checks to see if a channel is hosted, errors after 10secs
modem.transmit(channel, channel, "IsChannelUp?")
modem.open(channel)
local timeout = os.startTimer(10)
local e, arg1, arg2, arg3, server, distance = os.pullEvent()
if e == "timer" and arg1 == "timeout" then
    term.write("Channel "..channel.." is not up currently")
elseif e == "modem_message" and server == "ChannelUpYes" then
    modem.close(channel)

    term.setCursorPos(1, 5)
    term.write("Joining "..channel)
    os.sleep(1)
    term.clear()
    term.setCursorPos(1, 1)
    
    modem.transmit(channel, channel, name.." has joined the chat.")
    name="<"..name..">"
    
    while true do
        write("Message: ")
        local message = read()
        message=name.." "..message
        modem.transmit(channel, channel, message)
    end
end
