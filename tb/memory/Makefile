# defaults
SIM ?= verilator
TOPLEVEL_LANG ?= verilog
EXTRA_ARGS += --trace --trace-structs
WAVES = 1

# Go up 2 levels (out of 'memory', out of 'tb') to find 'src'
VERILOG_SOURCES += $(PWD)/../../src/memory.sv

TOPLEVEL = memory
MODULE = test_memory

include $(shell cocotb-config --makefiles)/Makefile.sim