import os
import time
import sys

inf=open("code_lcm", "r");
lines=inf.readlines();
#print lines;

out_str=""
for cur_line in lines:
	if len(cur_line) < 6:
		continue;
	cc=cur_line.strip().strip("\t").replace("{"," ",100).replace("}"," ",100).replace(","," ",100)
	print cc;
	clist=cc.split();
	print clist;
	if clist[0].find("REGFLAG_DELAY") != -1:
		out_str = "%s\n<LCM_FUNC_UTIL LCM_UTIL_MDELAY 1 %s>," % (out_str, str(clist[1]));
	else:
		cur_str="<LCM_FUNC_CMD LCM_UTIL_WRITE_CMD_V2 %d" % len(clist)
		for idd in clist:
			cur_str = "%s %s" % (cur_str, str(idd));
		cur_str = "%s>," % cur_str;
		print cur_str;
		out_str = "%s\n%s" % (out_str, cur_str)

print out_str;
