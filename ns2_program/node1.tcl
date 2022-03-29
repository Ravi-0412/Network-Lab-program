set ns [new Simulator]

set nf [open node1.nam w]
$ns namtrace-all $nf

proc finish {} {
global ns nf
$ns flush-trace
close $nf
exec nam node1.nam &
exit 0
}



set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]

$ns duplex-link $n0 $n1 10mb 10ms DropTail
$ns duplex-link $n0 $n2 10mb 10ms DropTail
$ns duplex-link $n0 $n3 10mb 10ms DropTail
$ns duplex-link $n1 $n2 10mb 10ms DropTail
$ns duplex-link $n1 $n3 10mb 10ms DropTail
$ns duplex-link $n2 $n3 10mb 10ms DropTail

$ns duplex-link-op $n0 $n1 orient right
$ns duplex-link-op $n0 $n2 orient right
$ns duplex-link-op $n0 $n3 orient right
$ns duplex-link-op $n1 $n2 orient right
$ns duplex-link-op $n1 $n3 orient right
$ns duplex-link-op $n2 $n3 orient right

$ns at 1.0 "finish"

$ns run
