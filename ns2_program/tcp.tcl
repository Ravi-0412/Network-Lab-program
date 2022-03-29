# set ns [new Simulator]

# set nf [open node1.nam w]
# $ns namtrace-all $nf

# proc finish {} {
# global ns nf
# $ns flush-trace
# close $nf
# exec nam node1.nam &
# exit 0
# }

# set n0 [$ns node]
# set n1 [$ns node]
# set n2 [$ns node]
# set n3 [$ns node]

# $ns duplex-link $n0 $n1 10mb 10ms DropTail
# $ns duplex-link $n0 $n2 10mb 10ms DropTail
# $ns duplex-link $n0 $n3 10mb 10ms DropTail
# $ns duplex-link $n1 $n2 10mb 10ms DropTail
# $ns duplex-link $n1 $n3 10mb 10ms DropTail
# $ns duplex-link $n2 $n3 10mb 10ms DropTail

# # $ns duplex-link-op $n0 $n1 orient right
# # $ns duplex-link-op $n0 $n2 orient right-down
# # $ns duplex-link-op $n0 $n3 orient right-down
# # $ns duplex-link-op $n1 $n2 orient right-down
# # $ns duplex-link-op $n1 $n3 orient left-down
# # $ns duplex-link-op $n2 $n3 orient left

# set tcp [new Agent/TCP]
# $ns attach-agent $n0 $tcp

# set sink [new Agent/TCPSink]
# $ns attach-agent $n3 $sink
# $ns connect $tcp $sink

# set ftp [new Application/FTP]
# $ftp attach-agent $tcp

# $ns at 0.5 "$ftp start"
# $ns at 4.5 "$ftp stop"



# $ns at 5.0 "finish"

# $ns run





set ns [new Simulator]
set nf [open out.nam w]
$ns namtrace-all $nf
set tf [open out.tr w]
set tf [open out.tr w]
$ns trace-all $tf
proc finish {} {
	global ns nf tf
	$ns flush-trace
	close $nf
close $tf
exec nam out.nam &
exit 0
}
set n0 [$ns node] 
set n1 [$ns node]

$ns duplex-link $n0 $n1 1Mb 10ms DropTail

set tcp0 [new Agent/TCP]

$ns attach-agent $n0 $tcp0

set sink0 [new Agent/TCPSink]

$ns attach-agent $n1 $sink0

$ns connect $tcp0 $sink0

set ftp [new Application/FTP]

$ftp attach-agent $tcp0

$ns at 0.5 "$ftp start"

$ns at 4.5 "$ftp stop"

$ns at 5.0 "finish"
$ns run







