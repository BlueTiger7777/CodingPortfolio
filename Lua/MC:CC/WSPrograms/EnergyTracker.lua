# Setup
local ws = http.websocket("0.0.0.0:9001")
local bat = peripheral.wrap("back")
local ME = bat.getMexEnergy()
local CE = bat.getEnergy()
local EI = bat.getLastInput()
local EO = bat.getLastOutput()
local msg = ME.." "..CE.." "..EI.." "..EO

# Update Loop
while True do:
  ws.send(msg)
  os.sleep(10)
