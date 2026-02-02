import cocotb
from cocotb.triggers import Timer
import random
from cocotb.types import LogicArray

async def set_unknown(dut):
    # Set all input to unknown before each test
    await Timer(1, unit="ns")
    dut.op.value = LogicArray("XXXXXXX")
    await Timer(1, unit="ns")

@cocotb.test()
async def control_test(dut):
    await set_unknown(dut)
    # TEST CONTROL SIGNALS FOR LW
    await Timer(1, unit="ns")
    dut.op.value = 0b0000011 #lw
    await Timer(1, unit="ns")
    assert dut.alu_ctrl.value == "000"
    assert dut.imm_src.value == "00"
    assert dut.mem_write.value == "0"
    assert dut.reg_write.value == "1"