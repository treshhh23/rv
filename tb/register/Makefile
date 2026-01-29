# defaults
SIM ?= verilator
TOPLEVEL_LANG ?= verilog
EXTRA_ARGS += --trace --trace-structs
WAVES = 1

VERILOG_SOURCES += $(PWD)/../../src/register.sv

TOPLEVEL = register
MODULE = test_register

include $(shell cocotb-config --makefiles)/Makefile.sim