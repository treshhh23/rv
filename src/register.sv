
`timescale 1ns/100ps
`default_nettype none

module register (
    input logic clk,
    input logic reset_n,

    input logic write_enable,
    input logic [4:0] write_addr,
    input logic [31:0] write_data,
    
    input logic [4:0] read_addr_a,
    input logic [4:0] read_addr_b,
    output logic [31:0] read_data_a,
    output logic [31:0] read_data_b
);

logic [31:0] registers [0:31];

always_ff@(posedge clk) begin
    if(~reset_n) begin
        for(int i = 0; i < 32; i++) begin
            registers[i] = 32'b0;
        end
    end else begin
        if(write_enable && write_addr != 5'd0) begin
            registers[write_addr] <= write_data;
        end
    end
end

assign read_data_a = registers[read_addr_a];
assign read_data_b = registers[read_addr_b];

endmodule

`default_nettype wire