-- Setup
local ws = http.websocket("0.0.0.0:9001")
local bat = peripheral.wrap("back")
local ME = bat.getMaxEnergy() * 0.4
local CE = bat.getEnergy() * 0.4
local EI = bat.getLastInput() * 0.4
local EO = bat.getLastOutput() * 0.4
local msg = ME.." "..CE.." "..EI.." "..EO

-- Tells the websocket that this client is a tracker
ws.send("Tracker")

-- Update Loop
while true do
  ws.send(msg)
  os.sleep(5)
  ME = bat.getMaxEnergy() * 0.4
  CE = bat.getEnergy() * 0.4
  EI = bat.getLastInput() * 0.4
  EO = bat.getLastOutput() * 0.4
  msg = ME.." "..CE.." "..EI.." "..EO
end
