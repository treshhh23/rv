
`timescale 1ns/100ps
`default_nettype none

module memory (
    input logic clk,
    input logic [31:0] address,
    input logic [31:0] write_data,
    input logic write_enable,
    input logic reset_n,
    
    output logic [31:0] read_data
);

parameter mem_words = 64;
logic [31:0] mem [mem_words-1:0];

always_ff@(posedge clk) begin
    if(~reset_n) begin
        read_data <= 32'b0;
    end else begin
        if(write_enable) begin
            if(address[1:0] == 2'b00) begin
               mem[address[7:2]] <= write_data;     
            end
        end

        read_data <= mem[address[7:2]];

    end
end

initial begin
    $readmemh("util/memory_init.hex", mem);
end
endmodule

`default_nettype wire