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

# $ns duplex-link-op $n0 $n1 orient right
# $ns duplex-link-op $n0 $n2 orient right-down
# $ns duplex-link-op $n0 $n3 orient right-down
# $ns duplex-link-op $n1 $n2 orient right-down
# $ns duplex-link-op $n1 $n3 orient left-down
# $ns duplex-link-op $n2 $n3 orient left

set udp0 [new Agent/UDP]
$ns attach-agent $n0 $udp0

set null0 [new Agent/Null]
$ns attach-agent $n3 $null0
$ns connect $udp0 $null0

set cbr0 [new Application/Traffic/CBR]
$cbr0 attach-agent $udp0


set udp1 [new Agent/UDP]
$ns attach-agent $n0 $udp1

set null1 [new Agent/Null]
$ns attach-agent $n2 $null1
$ns connect $udp1 $null1

set cbr1 [new Application/Traffic/CBR]
$cbr1 attach-agent $udp1

$ns at 0.5 "$cbr0 start"
$ns at 4.5 "$cbr0 stop"

$ns at 0.5 "$cbr1 start"
$ns at 4.5 "$cbr1 stop"

$ns at 5.0 "finish"

$ns run