# defaults
SIM ?= verilator
TOPLEVEL_LANG ?= verilog
EXTRA_ARGS += --trace --trace-structs
WAVES = 1

VERILOG_SOURCES += $(PWD)/../../src/extend.sv

TOPLEVEL = extend
MODULE = test_extend

include $(shell cocotb-config --makefiles)/Makefile.sim