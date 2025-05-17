-- Setup
ws = http.websocket("ws://localhost:9001")
ws.send("Turtle: "..os.getComputerLabel())

-- Functions
function split(instr)
    t = {}
    for i in string.gmatch(instr, "%S+") do
        table.insert(t, i)
    end
    return t
end

-- Command check
while true do
    msg = ws.receive()
    msgS = split(msg, nil)
    if msgS[1] == os.getComputerLabel() then
        ws.send("ACK")
        cmd = msgS[2]
        -- Movement
        if cmd == "forward" then
            turtle.forward()
            ws.send("FIN")
        elseif cmd == "turnLeft" then
            turtle.turnLeft()
            ws.send("FIN")
        elseif cmd == "turnRight" then
            turtle.turnRight()
            ws.send("FIN")
        elseif cmd == "back" then
            turtle.back()
            ws.send("FIN")
        elseif cmd == "up" then
            turtle.up()
            ws.send("FIN")
        elseif cmd == "down" then
            turtle.down()
            ws.send("FIN")
        -- Inventory
        elseif cmd == "equipLeft" then
            turtle.equipLeft()
            ws.send("FIN")
        elseif cmd == "equipRight" then
            turtle.equipRight()
            ws.send("FIN")
        elseif cmd == "select" then
            turtle.select(tonumber(msgS[3]))
            ws.send("FIN")
        -- Block Interactions
        elseif cmd == "dig" then
            turtle.dig()
            ws.send("FIN")
        elseif cmd == "digUp" then
            turtle.digUp()
            ws.send("FIN")
        elseif cmd == "digDown" then
            turtle.digDown()
            ws.send("FIN")
        elseif cmd == "inspect" then
            x, ins = turtle.inspect()
            ws.send(ins["name"])
            --for i in pairs(ins["state"]) do
            --    print(ins["state"][i])
            --end
            ws.send("FIN")
        -- Turtle info
        elseif cmd == "locate" then
            x1, y1, z1 = gps.locate()
            i = 4
            while i > 0 then
                if not turtle.detect() then
                    turtle.forward()
                    x2, y2, z2 = gps.locate()
                    if x1 > x2 then
                        dire = "North"
                    elseif z1 < z2 then
                        dire = "East"
                    elseif x1 < x2 then
                        dire = "South"
                    else
                        dire = "West"
                    end
                    i = 0
                    turtle.back()
                else
                    turtle.turnRight()
                    i -= 1
                    if i == 0 then
                        dire = "Unable to get direction"
                    end
                end
            end
            ws.send(x1.." "..y1.." "..z1.." "..dire)
            ws.send("FIN")
        elseif cmd == "fuelCheck" then
            fuelMax = turtle.getFuelLimit()
            fuelLevel = turtle.getFuelLevel()
            ws.send(fuelMax.." "..fuelLevel)
            ws.send("FIN")
        end
    end
end
