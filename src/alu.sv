
`timescale 1ns/100ps
`default_nettype none

module alu (
    input logic [31:0] src_1,
    input logic [31:0] src_2,
    input logic [2:0] control,

    output logic [31:0] result,

    // Flags

    output logic zero
);

always_comb begin
    case (control)
        3'b000: 
            result = src_1 + src_2;
        default: 
            result = 32'b0;

    endcase
end

assign zero = (result == 32'b0);

endmodule

`default_nettype wire