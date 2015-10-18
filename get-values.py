#!/usr/bin/env python
#---------------------------------------------------------------------------# 
# loading pymodbus modules
#---------------------------------------------------------------------------# 
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

#---------------------------------------------------------------------------# 
# client logging
#---------------------------------------------------------------------------# 
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

#---------------------------------------------------------------------------# 
# Connect info KW/H meter
#---------------------------------------------------------------------------# 
#client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600, timeout=1)
client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600, timeout=0.5)
client.connect()

#---------------------------------------------------------------------------# 
# 
#---------------------------------------------------------------------------# 
builder = BinaryPayloadBuilder(endian=Endian.Big)
builder.add_string('abcdefgh')
builder.add_32bit_float(22.34)
builder.add_16bit_uint(0x1234)
builder.add_8bit_int(0x12)
builder.add_bits([0,1,0,1,1,0,1,0])
payload = builder.build()
address = 0x01
result  = client.write_registers(address, payload, skip_encode=True)

#---------------------------------------------------------------------------# 
# Read data and convert to float and creating output files
#---------------------------------------------------------------------------# 

print "L1\n",
result  = client.read_input_registers(0x00, 2)
decoder = BinaryPayloadDecoder.fromRegisters(result.registers, endian=Endian.Big)
print decoder.decode_32bit_float(), "V \n",

result  = client.read_input_registers(0x06, 2)
decoder = BinaryPayloadDecoder.fromRegisters(result.registers, endian=Endian.Big)
print decoder.decode_32bit_float(), "A \n",

result  = client.read_input_registers(0x0C, 2)
decoder = BinaryPayloadDecoder.fromRegisters(result.registers, endian=Endian.Big)
print decoder.decode_32bit_float(), "W \n",

print "L2\n",
result  = client.read_input_registers(0x02, 2)
decoder = BinaryPayloadDecoder.fromRegisters(result.registers, endian=Endian.Big)
print decoder.decode_32bit_float(), "V \n",

result  = client.read_input_registers(0x08, 2)
decoder = BinaryPayloadDecoder.fromRegisters(result.registers, endian=Endian.Big)
print decoder.decode_32bit_float(), "A \n",

result  = client.read_input_registers(0x0E, 2)
decoder = BinaryPayloadDecoder.fromRegisters(result.registers, endian=Endian.Big)
print decoder.decode_32bit_float(), "W \n",

print "L3\n",
result  = client.read_input_registers(0x04, 2)
decoder = BinaryPayloadDecoder.fromRegisters(result.registers, endian=Endian.Big)
print decoder.decode_32bit_float(), "V \n",

result  = client.read_input_registers(0x0A, 2)
decoder = BinaryPayloadDecoder.fromRegisters(result.registers, endian=Endian.Big)
print decoder.decode_32bit_float(), "A \n",

result  = client.read_input_registers(0x10, 2)
decoder = BinaryPayloadDecoder.fromRegisters(result.registers, endian=Endian.Big)
print decoder.decode_32bit_float(), "W \n",


#---------------------------------------------------------------------------# 
# close the client
#---------------------------------------------------------------------------# 
client.close()

