`timescale 1ns/100ps
`default_nettype none

module control (
    // IN
    input logic [6:0] op,
    input logic [2:0] func3,
    input logic [6:0] func7,
    input logic alu_zero,

    // OUT
    output logic [2:0] alu_ctrl,
    output logic [1:0] imm_src,
    output logic mem_write,
    output logic reg_write
);

logic [1:0] alu_op;

always_comb begin
    case(op)
        7'b0000011: begin // lw
            reg_write = 1'b1;
            imm_src = 2'b00;
            mem_write = 1'b0;
            alu_op = 2'b00;
        end

        7'b0100011: begin // sw
            reg_write = 1'b0;
            imm_src = 2'b01;
            mem_write = 1'b1;
            alu_op = 2'b00;
        end

        default: begin
            reg_write = 1'b0;
            imm_src = 2'b00;
            mem_write = 1'b0;
            alu_op = 2'b00;
        end
    endcase
end

always_comb begin
    case(alu_op)
        2'b00: begin
            alu_ctrl = 3'b000;
        end

        default: begin
            alu_ctrl = 3'b111;
        end
    endcase
end

endmodule

`default_nettype wire