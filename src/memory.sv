
module memory #(
    parameter WORDS = 64,
    parameter mem_init = ""
) (
    input logic clk,
    input logic [31:0] address,
    input logic [31:0] write_data,
    input logic write_enable,
    input logic reset_n,

    output logic [31:0] read_data
);

reg [31:0] mem [0:WORDS-1];  // Memory array of words (32-bits)

localparam INDEX_BITS = $clog2(WORDS);
logic [INDEX_BITS-1:0] internal_addr;
assign internal_addr = address[INDEX_BITS+1 : 2];

always @(posedge clk) begin
    if (reset_n == 1'b0) begin
        for (int i = 0; i < WORDS; i++) begin
            mem[i] <= 32'b0;  
        end
    end
    else if (write_enable) begin
        if (address[1:0] == 2'b00) begin 
            mem[internal_addr] <= write_data;
        end
    end
end

always_comb begin
    read_data = mem[internal_addr]; 
end

initial begin
    $readmemh(mem_init, mem);  // Load memory for simulation
end
endmodule
