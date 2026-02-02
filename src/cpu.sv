`timescale 1ns/100ps
`default_nettype none

module cpu (
    input logic clk,
    input logic reset_n
);


// Program counter
logic [31:0] pc;
logic [31:0] pc_next;

assign pc_next = pc + 4;

always_ff @(posedge clk) begin
    if(reset_n == 0) begin
        pc <= 32'b0;
    end else begin  
        pc <= pc_next;
    end
end

// Instruction memory
logic [31:0] instruction;

memory #(
    .mem_init("./test_imemory.hex")
) instruction_memory (
    .clk(clk),
    .address(pc),
    .write_data(32'b0),
    .write_enable(1'b0),
    .reset_n(1'b1),

    .read_data(instruction)
);

// Control
logic [6:0] op;
logic [2:0] f3;
logic alu_zero;
logic [2:0] alu_ctrl;
logic [1:0] imm_src;
logic mem_write;
logic reg_write;

assign op = instruction[6:0];
assign f3 = instruction[14:12];

control control_unit(
    .op(op),
    .func3(f3),
    .func7(7'b0),
    .alu_zero(alu_zero),

    // OUT
    .alu_ctrl(alu_ctrl),
    .imm_src(imm_src),
    .mem_write(mem_write),
    .reg_write(reg_write)
);

// Register
logic [4:0] source_reg1;
logic [4:0] source_reg2;
logic [4:0] dest_reg;
wire [31:0] read_reg1;
wire [31:0] read_reg2;
logic [31:0] write_back_data;

assign source_reg1 = instruction[19:15];
assign source_reg2 = instruction[24:20];
assign dest_reg = instruction[11:7];

always_comb begin : wbSelect
    write_back_data = mem_read;
end

register reg_unit(
    .clk(clk),
    .reset_n(reset_n),

    // Write
    .write_enable(reg_write),
    .write_addr(dest_reg),
    .write_data(write_back_data),

    .read_addr_a(source_reg1),
    .read_addr_b(source_reg2),
    .read_data_a(read_reg1),
    .read_data_b(read_reg2)
);

logic [24:0] full_imm;
logic [31:0] imm;

assign full_imm = instruction[31:7];

extend ext_unit (
    .raw_code(full_imm),
    .imm_src(imm_src),
    .extend_imm(imm)
);

// ALU

logic [31:0] result;
logic [31:0] alu_src2;

always_comb begin : srcBSelect
    alu_src2 = imm;
end

alu alu (
    .src_1(read_reg1),
    .src_2(alu_src2),
    .control(alu_ctrl),
    .result(result),
    .zero(alu_zero)
);

// Memory

logic [31:0] mem_read;

memory #(
    .mem_init("./test_dmemory.hex")
) data_memory (
    // Memory inputs
    .clk(clk),
    .address(result),
    .write_data(read_reg2),
    .write_enable(mem_write),
    .reset_n(1'b1),

    // Memory outputs
    .read_data(mem_read)
);


endmodule
`default_nettype wire