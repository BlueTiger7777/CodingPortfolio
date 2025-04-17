-- Setup
local ws = http.websocket("0.0.0.0:9001")
local bat = peripheral.wrap("back")
local ME = bat.getMaxEnergy()
local CE = bat.getEnergy()
local EI = bat.getLastInput()
local EO = bat.getLastOutput()
local msg = ME.." "..CE.." "..EI.." "..EO

-- Tells the websocket that this client is a tracker
ws.send("Tracker")

-- Update Loop
while true do
  ws.send(msg)
  os.sleep(5)
  ME = bat.getMaxEnergy()
  CE = bat.getEnergy()
  EI = bat.getLastInput()
  EO = bat.getLastOutput()
  msg = ME.." "..CE.." "..EI.." "..EO
end
