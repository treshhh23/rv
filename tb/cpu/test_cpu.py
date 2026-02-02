import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.types import LogicArray
from cocotb.clock import RisingEdge

def binary_to_hex(bin_str):
    # Convert binary string to hexadecimal
    hex_str = hex(int(str(bin_str), 2))[2:]
    hex_str = hex_str.zfill(8)
    return hex_str.upper()

def hex_to_bin(hex_str):
    # Convert hex str to bin
    bin_str = bin(int(str(hex_str), 16))[2:]
    bin_str = bin_str.zfill(32)
    return bin_str.upper()

async def cpu_reset(dut):
    dut.reset_n.value = 0
    await RisingEdge(dut.clk)     # Wait for a clock edge after reset
    dut.reset_n.value = 1           # De-assert reset
    await RisingEdge(dut.clk)     # Wait for a clock edge after reset

@cocotb.test()
async def cpu_insrt_test(dut):
    cocotb.start_soon(Clock(dut.clk, 1, unit='ns').start())
    await RisingEdge(dut.clk)
    await cpu_reset(dut)
    await RisingEdge(dut.clk)

    assert binary_to_hex(dut.reg_unit.registers[18].value) == "CAFEFACE" 
    print(binary_to_hex(dut.reg_unit.registers[18].value))

    # First, let's check the inital value
    assert binary_to_hex(dut.data_memory.mem[3].value) == "F2F2F2F2"

    # Wait a clock cycle for the instruction to execute
    await RisingEdge(dut.clk)
    # Check the value of mem[0xC]
    assert binary_to_hex(dut.data_memory.mem[3].value) == "CAFEFACE"
    

