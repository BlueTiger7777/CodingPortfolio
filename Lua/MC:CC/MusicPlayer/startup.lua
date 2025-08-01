-- Defineing Notes (asumes first 8 redstone intergrators are on this network and create is installed)
local function MP_HFs do
  local relay = peripheral.wrap("redstone_relay_0")
  local side = "front"
  if relay.getOutput(side) then
      relay.setOutput(side, False)
  else
      relay.setOutput(side. True)
  end
end

-- Main
MP_HFs()
