-- Defineing Notes (asumes first 8 redstone intergrators are on this network and create is installed)
local function MP_HFs()
  local relay = peripheral.wrap("redstone_relay_0")
  local side = "front"
  if relay.getOutput(side) then
      relay.setOutput(side, false)
  else
      relay.setOutput(side, true)
  end
end

local function MP_F()
  local relay = peripheral.wrap("redstone_relay_0")
  local side = "left"
  if relay.getOutput(side) then
      relay.setOutput(side, false)
  else
      relay.setOutput(side, true)
  end
end

local function MP_E()
  local relay = peripheral.wrap("redstone_relay_0")
  local side = "right"
  if relay.getOutput(side) then
      relay.setOutput(side, false)
  else
      relay.setOutput(side, true)
  end
end

local function MP_Ds()
  local relay = peripheral.wrap("redstone_relay_0")
  local side = "back"
  if relay.getOutput(side) then
      relay.setOutput(side, false)
  else
      relay.setOutput(side, true)
  end
end

local function MP_D()
  local relay = peripheral.wrap("redstone_relay_0")
  local side = "top"
  if relay.getOutput(side) then
      relay.setOutput(side, false)
  else
      relay.setOutput(side, true)
  end
end

local function MP_Cs()
  local relay = peripheral.wrap("redstone_relay_1")
  local side = "front"
  if relay.getOutput(side) then
      relay.setOutput(side, false)
  else
      relay.setOutput(side, true)
  end
end

local function MP_C()
  local relay = peripheral.wrap("redstone_relay_1")
  local side = "left"
  if relay.getOutput(side) then
      relay.setOutput(side, false)
  else
      relay.setOutput(side, true)
  end
end

local function MP_B()
  local relay = peripheral.wrap("redstone_relay_1")
  local side = "right"
  if relay.getOutput(side) then
      relay.setOutput(side, false)
  else
      relay.setOutput(side, true)
  end
end

local function MP_As()
  local relay = peripheral.wrap("redstone_relay_1")
  local side = "back"
  if relay.getOutput(side) then
      relay.setOutput(side, false)
  else
      relay.setOutput(side, true)
  end
end

local function MP_A()
  local relay = peripheral.wrap("redstone_relay_1")
  local side = "top"
  if relay.getOutput(side) then
      relay.setOutput(side, false)
  else
      relay.setOutput(side, true)
  end
end

local function MP_Gs()
  local relay = peripheral.wrap("redstone_relay_2")
  local side = "front"
  if relay.getOutput(side) then
      relay.setOutput(side, false)
  else
      relay.setOutput(side, true)
  end
end

local function MP_G()
  local relay = peripheral.wrap("redstone_relay_2")
  local side = "left"
  if relay.getOutput(side) then
      relay.setOutput(side, false)
  else
      relay.setOutput(side, true)
  end
end

local function MP_LFs()
  local relay = peripheral.wrap("redstone_relay_2")
  local side = "right"
  if relay.getOutput(side) then
      relay.setOutput(side, false)
  else
      relay.setOutput(side, true)
  end
end

-- Main
MP_HFs()
os.sleep(0.5)
MP_HFs()
os.sleep(0.5)
MP_F()
os.sleep(0.5)
MP_F()
os.sleep(0.5)
MP_E()
os.sleep(0.5)
MP_E()
os.sleep(0.5)
MP_Ds()
os.sleep(0.5)
MP_Ds()
os.sleep(0.5)
MP_D()
os.sleep(0.5)
MP_D()
os.sleep(0.5)
MP_Cs()
os.sleep(0.5)
MP_Cs()
os.sleep(0.5)
MP_C()
os.sleep(0.5)
MP_C()
os.sleep(0.5)
MP_B()
os.sleep(0.5)
MP_B()
os.sleep(0.5)
MP_As()
os.sleep(0.5)
MP_As()
os.sleep(0.5)
MP_A()
os.sleep(0.5)
MP_A()
os.sleep(0.5)
MP_Gs()
os.sleep(0.5)
MP_Gs()
os.sleep(0.5)
MP_G()
os.sleep(0.5)
MP_G()
os.sleep(0.5)
MP_HFs()
os.sleep(0.5)
MP_HFs()
