# test_alu.py

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
import random
import numpy as np

@cocotb.test()
async def random_add(dut):
    for i in range(1000):
       source_1 = random.randint(0, 0x10000000)
       source_2 = random.randint(0, 0x0FFFFFFF)
       await Timer(1, unit='ns')
       dut.src_1.value = source_1
       dut.src_2.value = source_2
       await Timer(1, unit='ns')
       assert dut.result.value == source_1 + source_2


@cocotb.test()
async def zero_flag(dut):
    await Timer(1, unit='ns')
    dut.src_1.value = 0
    dut.src_2.value = 0
    await Timer(1, unit='ns')
    assert dut.zero.value == 1

@cocotb.test()
async def default_test(dut):
    await Timer(1, unit="ns")
    dut.control.value = 0b111
    src1 = random.randint(0,0xFFFFFFFF)
    src2 = random.randint(0,0xFFFFFFFF)
    dut.src_1.value = src1
    dut.src_2.value = src2
    expected = 0
    await Timer(1, unit="ns")
    assert int(dut.result.value) == expected
    
