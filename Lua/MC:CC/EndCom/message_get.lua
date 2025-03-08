term.clear()

term.setCursorPos(1, 1)
write("Side of modem: ")
local modemSide = read()
local modem = peripheral.wrap(modemSide)

term.setCursorPos(1, 2)
write("Channel to read: ")
local channel = tonumber(read())

term.setCursorPos(1, 3)
write("Do you have a monitor connected? Y/N: ")
local haveMonitor = read()

if haveMonitor == "Y" or haveMonitor == "y" then
    term.setCursorPos(1, 4)
    write("Side of monitor: ")
    local monitorSide = read()
    local monitor = peripheral.wrap(monitorSide)
    monitor.setTextScale(0.5)
    monitor.clear()
    local mX = 1
    local mY = 0
	
	modem.transmit(channel, channel, "IsChannelUp?")
	modem.open(channel)
	local timeout = os.startTimer(10)
	local e, arg1, arg2, arg3, arg4, arg5 = os.pullEvent()
	if e == "timer" and arg1 == "timeout" then
		term.setCursorPos(1, 5)
		term.write("Channel "..channel.." is not up currently")
	elseif e == "modem_message" and arg4 == "ChannelUpYes" then
    
		term.setCursorPos(1, 6)
		term.write("Reading messages on channel "..channel)
    
		while true do
			modem.open(channel)
			local event, side, sender, reply, message, distance = os.pullEvent("modem_message")
			if message == "IsChannelUp?" or message == "ChannelUpYes" then
				os.sleep(0.1)
			else  
				mY = mY+1
				if mY > 24 then
					monitor.scroll(1)
					monitor.setCursorPos(1, 24)
					monitor.write(message)
				else
					monitor.setCursorPos(mX, mY)
					monitor.write(message)
				end
			end
		end
    end
	
else
	modem.transmit(channel, channel, "IsChannelUp?")
	modem.open(channel)
	local timeout = os.startTimer(10)
	local e, arg1, arg2, arg3, server, distance = os.pullEvent()
	if e == "timer" and arg1 == "timeout" then
		term.setCursorPos(1, 4)
		term.write("Channel "..channel.." is not up currently")
	elseif e == "modem_message" and server == "ChannelUpYes" then
		term.setCursorPos(1, 5)
		term.write("Reading messages on channel "..channel)
		os.sleep(1)
		term.clear()
		term.setCursorPos(1, 1)
		while true do
			modem.open(channel)
			local event, side, sender, reply, message, distance = os.pullEvent("modem_message")
			print(message)
		end
	end
end
