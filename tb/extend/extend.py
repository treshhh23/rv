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




