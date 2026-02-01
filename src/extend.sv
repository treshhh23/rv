`timescale 1ns/100ps
`default_nettype none


module extend (
    input logic [24:0] raw_code,
    input logic [1:0] imm_src,
    output logic [31:0] extend_imm
);

logic [11:0] imm;

always_comb begin
    case(imm_src)
        2'b00 : imm = raw_code[24:13];
        default : imm = 12'b0;
    endcase
end

assign extend_imm = {{20{imm[11]}}, imm};

endmodule
`default_nettype wire