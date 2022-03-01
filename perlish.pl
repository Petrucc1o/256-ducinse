#!/usr/bin/perl -w
use strict;

my (%hash,$key);

open (READ, "./tron.json") || die "cannot open file: $!";
while (<READ>){
    if (/^    (\S+):/) {
        $key=$1;       
    }
    if (/^        (\S+): (\S+)/){
        $hash{$key}{$1}=$2;
    }
}
close(READ);

foreach my $c (sort keys %hash) {
    foreach my $d (sort keys %{$hash{$c}}){
       print $c,"\t",$d,"\t",$hash{$c}{$d},"\n"; 
    }
}