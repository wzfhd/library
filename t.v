`timescale 1ns/1ps
module pulse_check (
    input clk,
    input rst_n,
    input in,

    output pulse);

    reg [1:0] delay;
    always @(posedge clk or posedge rst_n) begin
        if (!rst_n)
            delay <= 2'd0;
        else
            delay <= {delay[0] , in};
    end

    assign pulse = delay == 2'b01;

endmodule