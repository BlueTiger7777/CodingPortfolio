-- Peripherals
m = peripheral.find("monitor")
l = peripheral.find("Create_DisplayLink")

-- Vars
deafultAddr("<addres>")
shiftState = false
entredAddr = ""

-- Monitor setup
m.setBackgroundColor(32768)
m.clear()
m.setTextScale(0.5)

-- Stationary Graphics
-- Light gray pass
m.setBackgroundColor(256)
m.setCursorPos(3, 4)
m.write("                           ")
m.setCursorPos(3, 6)
m.write("                           ")
m.setCursorPos(3, 5)
m.write(" ")
m.setCursorPos(29, 5)
m.write(" ")
-- Light blue pass
m.setBackgroundColor(8)
m.setCursorPos(1,1)
m.write("Rev09-03-2025")
-- Red pass
m.setBackgroundColor(16384)
m.setCursorPos(29, 16)
m.write("<-")
m.setCursorPos(29, 17)
m.write("  ")
-- Green pass
m.setBackgroundColor(8192)
m.setCursorPos(26, 19)
m.write("ENTER")
m.setCursorPos(26, 20)
m.write("     ")
-- Gray pass
m.setBackgroundColor(128)
-- Num Row
m.setCursorPos(2, 10)
m.write("1 ")
m.setCursorPos(5, 10)
m.write("2 ")
m.setCursorPos(8, 10)
m.write("3 ")
m.setCursorPos(11, 10)
m.write("4 ")
m.setCursorPos(14, 10)
m.write("5 ")
m.setCursorPos(17, 10)
m.write("6 ")
m.setCursorPos(20, 10)
m.write("7 ")
m.setCursorPos(23, 10)
m.write("8 ")
m.setCursorPos(26, 10)
m.write("9 ")
m.setCursorPos(29, 10)
m.write("0 ")
m.setCursorPos(2, 11)
m.write("  ")
m.setCursorPos(5, 11)
m.write("  ")
m.setCursorPos(8, 11)
m.write("  ")
m.setCursorPos(11, 11)
m.write("  ")
m.setCursorPos(14, 11)
m.write("  ")
m.setCursorPos(17, 11)
m.write("  ")
m.setCursorPos(20, 11)
m.write("  ")
m.setCursorPos(23, 11)
m.write("  ")
m.setCursorPos(26, 11)
m.write("  ")
m.setCursorPos(29, 11)
m.write("  ")
-- QWERTY Row
m.setCursorPos(2, 13)
m.write("Q ")
m.setCursorPos(5, 13)
m.write("W ")
m.setCursorPos(8, 13)
m.write("E ")
m.setCursorPos(11, 13)
m.write("R ")
m.setCursorPos(14, 13)
m.write("T ")
m.setCursorPos(17, 13)
m.write("Y ")
m.setCursorPos(20, 13)
m.write("U ")
m.setCursorPos(23, 13)
m.write("I ")
m.setCursorPos(26, 13)
m.write("O ")
m.setCursorPos(29, 13)
m.write("P ")
m.setCursorPos(2, 14)
m.write("  ")
m.setCursorPos(5, 14)
m.write("  ")
m.setCursorPos(8, 14)
m.write("  ")
m.setCursorPos(11, 14)
m.write("  ")
m.setCursorPos(14, 14)
m.write("  ")
m.setCursorPos(17, 14)
m.write("  ")
m.setCursorPos(20, 14)
m.write("  ")
m.setCursorPos(23, 14)
m.write("  ")
m.setCursorPos(26, 14)
m.write("  ")
m.setCursorPos(29, 14)
m.write("  ")
-- ASDFGH Row
m.setCursorPos(2, 16)
m.write("A ")
m.setCursorPos(5, 16)
m.write("S ")
m.setCursorPos(8, 16)
m.write("D ")
m.setCursorPos(11, 16)
m.write("F ")
m.setCursorPos(14, 16)
m.write("G ")
m.setCursorPos(17, 16)
m.write("H ")
m.setCursorPos(20, 16)
m.write("J ")
m.setCursorPos(23, 16)
m.write("K ")
m.setCursorPos(26, 16)
m.write("L ")
m.setCursorPos(2, 17)
m.write("  ")
m.setCursorPos(5, 17)
m.write("  ")
m.setCursorPos(8, 17)
m.write("  ")
m.setCursorPos(11, 17)
m.write("  ")
m.setCursorPos(14, 17)
m.write("  ")
m.setCursorPos(17, 17)
m.write("  ")
m.setCursorPos(20, 17)
m.write("  ")
m.setCursorPos(23, 17)
m.write("  ")
m.setCursorPos(26, 17)
m.write("  ")
-- ZXCVBN Row
m.setCursorPos(5, 19)
m.write("Z ")
m.setCursorPos(8, 19)
m.write("X ")
m.setCursorPos(11, 19)
m.write("C ")
m.setCursorPos(14, 19)
m.write("V ")
m.setCursorPos(17, 19)
m.write("B ")
m.setCursorPos(20, 19)
m.write("N ")
m.setCursorPos(23, 19)
m.write("M ")
m.setCursorPos(5, 20)
m.write("  ")
m.setCursorPos(8, 20)
m.write("  ")
m.setCursorPos(11, 20)
m.write("  ")
m.setCursorPos(14, 20)
m.write("  ")
m.setCursorPos(17, 20)
m.write("  ")
m.setCursorPos(20, 20)
m.write("  ")
m.setCursorPos(23, 20)
m.write("  ")
-- Space bar row
m.setCursorPos(5, 22)
m.write("- ")
m.setCursorPos(5, 23)
m.write("  ")
m.setCursorPos(26, 22)
m.write("_ ")
m.setCursorPos(26, 23)
m.write("  ")
m.setCursorPos(8, 22)
m.write(" [_____________] ")
m.setCursorPos(8, 23)
m.write("                 ")

-- Changing
function shift(State)
	if State then
		m.setBackgroundColor(8)
		m.setCursorPos(2, 19)
		m.write("/\\")
		m.setCursorPos(2, 20)
		m.write("  ")
	else
		m.setBackgroundColor(128)
		m.setCursorPos(2, 19)
		m.write("/\\")
		m.setCursorPos(2, 20)
		m.write("  ")
	end
end

function text(addr)
	m.setBackgroundColor(256)
	m.setCursorPos(4, 5)
	if 25 - addr:len() > 0 then
		i = 25 - addr:len()
		while i > 0 do
			addr = addr .. " "
			i = i - 1
		end
	elseif 25 - addr:len() < 0 then
		i = (25 - addr:len()) * -1
		while i > 0 do
			addr = addr:sub(1, -2)
			i = i - 1
		end
	end
	m.write(addr)
end

function link(addr)
	l.clear()
	l.update()
	if addr:len() ~= 0 then
		addr = defaultAddr
	end
	l.setCursorPos(1,1)
	l.write(addr)
	l.update()
	redstone.setAnalogOutput("back", 15)
	os.sleep(1)
	redstone.setAnalogOutput("back", 0)
end

shift(shiftState)
text(entredAddr)
link(entredAddr)

-- Keyboard Typing
while true do
	event,side,x,y = os.pullEvent("monitor_touch")
	-- Shift
	if x >= 2 and x <= 3 and y >= 19 and y <= 20 then
		if shiftState then
			shiftState = false
			shift(shiftState)
		else
			shiftState = true
			shift(shiftState)
		end
	-- Backspace
	elseif x >= 29 and x <= 30 and y >= 16 and y <= 17 then
		if entredAddr:len() - 1 >= 0 then
			entredAddr = entredAddr:sub(1, -2)
			text(entredAddr)
		end
	-- Space
	elseif x >= 8 and x <= 24 and y >= 22 and y <= 23 then
		entredAddr = entredAddr .. " "
		text(entredAddr)
	-- Dash
	elseif x >= 5 and x <= 6 and y >= 22 and y <= 23 then
		entredAddr = entredAddr .. "-"
		text(entredAddr)
	-- Underscore
	elseif x >= 26 and x <= 27 and y >= 22 and y <= 23 then
		entredAddr = entredAddr .. "_"
		text(entredAddr)
	-- Enter
	elseif x >= 26 and x <= 30 and y >= 19 and y <= 20 then
		link(entredAddr)
	-- Alphabet
	elseif x >= 2 and x <= 3 and y >= 13 and y <= 14 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "Q"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "q"
			text(entredAddr)
		end
	elseif x >= 5 and x <= 6 and y >= 13 and y <= 14 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "W"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "w"
			text(entredAddr)
		end
	elseif x >= 8 and x <= 9 and y >= 13 and y <= 14 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "E"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "e"
			text(entredAddr)
		end
	elseif x >= 11 and x <= 12 and y >= 13 and y <= 14 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "R"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "r"
			text(entredAddr)
		end
	elseif x >= 14 and x <= 15 and y >= 13 and y <= 14 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "T"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "t"
			text(entredAddr)
		end
	elseif x >= 17 and x <= 18 and y >= 13 and y <= 14 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "Y"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "y"
			text(entredAddr)
		end
	elseif x >= 20 and x <= 21 and y >= 13 and y <= 14 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "U"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "u"
			text(entredAddr)
		end
	elseif x >= 23 and x <= 24 and y >= 13 and y <= 14 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "I"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "i"
			text(entredAddr)
		end
	elseif x >= 26 and x <= 27 and y >= 13 and y <= 14 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "O"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "o"
			text(entredAddr)
		end
	elseif x >= 29 and x <= 30 and y >= 13 and y <= 14 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "P"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "p"
			text(entredAddr)
		end
	elseif x >= 2 and x <= 3 and y >= 16 and y <= 17 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "A"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "a"
			text(entredAddr)
		end
	elseif x >= 5 and x <= 6 and y >= 16 and y <= 17 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "S"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "s"
			text(entredAddr)
		end
	elseif x >= 8 and x <= 9 and y >= 16 and y <= 17 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "D"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "d"
			text(entredAddr)
		end
	elseif x >= 11 and x <= 12 and y >= 16 and y <= 17 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "F"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "f"
			text(entredAddr)
		end
	elseif x >= 14 and x <= 15 and y >= 16 and y <= 17 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "G"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "g"
			text(entredAddr)
		end
	elseif x >= 17 and x <= 18 and y >= 16 and y <= 17 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "H"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "h"
			text(entredAddr)
		end
	elseif x >= 20 and x <= 21 and y >= 16 and y <= 17 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "J"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "j"
			text(entredAddr)
		end
	elseif x >= 23 and x <= 24 and y >= 16 and y <= 17 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "K"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "k"
			text(entredAddr)
		end
	elseif x >= 26 and x <= 27 and y >= 16 and y <= 17 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "L"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "l"
			text(entredAddr)
		end
	elseif x >= 5 and x <= 6 and y >= 19 and y <= 20 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "Z"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "z"
			text(entredAddr)
		end
	elseif x >= 8 and x <= 9 and y >= 19 and y <= 20 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "X"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "x"
			text(entredAddr)
		end
	elseif x >= 11 and x <= 12 and y >= 19 and y <= 20 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "C"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "c"
			text(entredAddr)
		end
	elseif x >= 14 and x <= 15 and y >= 19 and y <= 20 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "V"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "v"
			text(entredAddr)
		end
	elseif x >= 17 and x <= 18 and y >= 19 and y <= 20 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "B"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "b"
			text(entredAddr)
		end
	elseif x >= 20 and x <= 21 and y >= 19 and y <= 20 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "N"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "n"
			text(entredAddr)
		end
	elseif x >= 23 and x <= 24 and y >= 19 and y <= 20 then
		if shiftState then
			shiftState = false
			shift(shiftState)
			entredAddr = entredAddr .. "M"
			text(entredAddr)
		else
			entredAddr = entredAddr .. "m"
			text(entredAddr)
		end
	-- Numbers
	elseif x >= 2 and x <= 3 and y >= 10 and y <= 11 then
		entredAddr = entredAddr .. "1"
		text(entredAddr)
	elseif x >= 5 and x <= 6 and y >= 10 and y <= 11 then
		entredAddr = entredAddr .. "2"
		text(entredAddr)
	elseif x >= 8 and x <= 9 and y >= 10 and y <= 11 then
		entredAddr = entredAddr .. "3"
		text(entredAddr)
	elseif x >= 11 and x <= 12 and y >= 10 and y <= 11 then
		entredAddr = entredAddr .. "4"
		text(entredAddr)
	elseif x >= 14 and x <= 15 and y >= 10 and y <= 11 then
		entredAddr = entredAddr .. "5"
		text(entredAddr)
	elseif x >= 17 and x <= 18 and y >= 10 and y <= 11 then
		entredAddr = entredAddr .. "6"
		text(entredAddr)
	elseif x >= 20 and x <= 21 and y >= 10 and y <= 11 then
		entredAddr = entredAddr .. "7"
		text(entredAddr)
	elseif x >= 23 and x <= 24 and y >= 10 and y <= 11 then
		entredAddr = entredAddr .. "8"
		text(entredAddr)
	elseif x >= 26 and x <= 27 and y >= 10 and y <= 11 then
		entredAddr = entredAddr .. "9"
		text(entredAddr)
	elseif x >= 29 and x <= 30 and y >= 10 and y <= 11 then
		entredAddr = entredAddr .. "0"
		text(entredAddr)
	end
end
