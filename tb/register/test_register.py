# test_register.py

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
import random
import numpy as np

@cocotb.test()
async def register_data_test(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    await RisingEdge(dut.clk)

    # Reset
    dut.reset_n.value = 0
    dut.write_enable.value = 0
    dut.write_addr.value = 0
    dut.write_data.value = 0
    dut.read_addr_a.value = 0
    dut.read_addr_b.value = 0

    await RisingEdge(dut.clk)
    dut.reset_n.value = 1
    await RisingEdge(dut.clk)

    theoretical_regs = [0 for _ in range(32)]

    for _ in range(1000):
        write_addr = random.randint(1,31)
        write_data = random.randint(0, 0xFFFFFFFF)
        read_addr_a = random.randint(1,31)
        read_addr_b = random.randint(1,31)

        await Timer(1, unit='ns')
        dut.read_addr_a.value = read_addr_a
        dut.read_addr_b.value = read_addr_b
        await Timer(1, unit='ns')
        assert dut.read_data_a.value == theoretical_regs[read_addr_a]
        assert dut.read_data_b.value == theoretical_regs[read_addr_b]

        dut.write_addr.value = write_addr
        dut.write_enable.value = 1
        dut.write_data.value = write_data
        await RisingEdge(dut.clk)
        dut.write_enable.value = 0
        theoretical_regs[write_addr] = write_data
        await Timer(1, unit='ns')

    await Timer(1, unit='ns')
    dut.write_addr.value = 0
    dut.write_enable.value = 1
    dut.write_data.value = 0xFFFFFFFF
    await RisingEdge(dut.clk)
    dut.write_enable.value = 0

    await Timer(1, unit='ns')
    dut.read_addr_a.value = 0
    await Timer(1, unit='ns')
    assert int(dut.read_addr_a.value) == 0

    print("Random read/write completed")
    

