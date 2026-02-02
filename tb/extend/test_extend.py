import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
import random
import numpy as np

@cocotb.test 
async def extend_test(dut):
    imm = 0x00F # positive 15
    imm <<= 13 # Shift into place
    source = 0b00

    await Timer(1, unit='ns')
    dut.imm_src.value = source
    dut.raw_code.value = imm | 0b000000000000_1010101010101 # combine with some random value
    await Timer(1, unit='ns')
    assert dut.extend_imm.value == "00000000000000000000000000001111"
    assert int(dut.extend_imm.value) == 15

    imm = 0xFFE # positive 15
    imm <<= 13 # Shift into place
    source = 0b00

    await Timer(1, unit='ns')
    dut.imm_src.value = source
    dut.raw_code.value = imm | 0b000000000000_1010101010101 # combine with some random value
    await Timer(1, unit='ns')
    assert dut.extend_imm.value == "11111111111111111111111111111110"
    assert int(dut.extend_imm.value) - (1 << 32) == -2


@cocotb.test()
async def signext_s_type_test(dut):
    await Timer(1, unit="ns")
    imm = random.randint(0,0b01111111111) 
    imm_11_5 = imm >> 5
    imm_4_0 = imm & 0b000000011111

    raw_data = ((imm_11_5) << 18 ) | imm_4_0
    source = 0b01
    dut.raw_code.value = raw_data
    dut.imm_src.value = source
    await Timer(1, unit='ns')
    assert dut.extend_imm.value == imm
    
    await Timer(1, unit="ns")
    imm = random.randint(0b100000000000,0b111111111111) - (1 << 12)
    imm_11_5 = imm >> 5
    imm_4_0 = imm & 0b000000011111

    raw_data = ((imm_11_5) << 18 ) | imm_4_0
    source = 0b01
    dut.raw_code.value = raw_data
    dut.imm_src.value = source
    await Timer(1, unit='ns')
    assert int(dut.extend_imm.value) - (1 << 32) == imm






