#!/bin/sh

cat code | grep SSD_Single | sed 's/^[ \t]*//g' > 2
#cat 1 | sed 's/^R//g' > 2 #| sed 's/[ \t]*$//g' > 2
#cat 2 | awk '{print "{0x"$1",1,{0x"$2"}},"}' 
#cat 2 | awk '{n=1; for(;n<(NF);n++) {if($n ~ /SET_CMD/) printf("\n");printf("%s;", $n)}}' > 3
cat 2 | sed 's/SSD_Single(//g' | sed 's/;/,/g' | sed 's/[()]//g' > 3
cat 3 | awk -F, '{print "{"$1",1,{"$2"}},"}' 
#cat 4 | awk -F ";" '{printf("\t{%s,%d,{", $1, NF-2);if(NF>2){i=2; for(;i<NF;i++) {printf("%s", $i);if(i!=NF-1) printf(",");};}printf("}},\n")}'  > last_ccc.c

#cat 3 | awk -F "\n" '{ if ($0 ~ /^WriteCommand*/) printf("\n"); print $1}'
#cat 1 | sed 's/WriteCommand//g' | sed 's/WriteData//g' | sed 's/[()]//g' > 2
#cat 2 | sed 's/^ *//g' | sed 's/ *$//'> 3
#cat 3 | awk -F ";" '{ 
#if (NF==1) printf("\t{%s, 0,{}},\n",$1);
#if (NF==2) printf("\t{%s, 0,{}},\n",$1);
#if (NF==3) printf("\t{%s, %d,{%s}},\n", $1, NF-2, $2);
#if (NF==4) printf("\t{%s, %d,{%s,%s}},\n", $1, NF-2, $2, $3);
#if (NF==5) printf("\t{%s, %d,{%s,%s}},\n", $1, NF-2, $2, $3, $4);}' > 4
#printf("%d: {%s, %s, {%s, %s}},\n",NR, $1, NF-2, $2, $3)}'
