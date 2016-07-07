import os
import time
import sys

inf=open("code_lcm_v1", "r");
lines=inf.readlines();
#print lines;

out_str=""
array_str="data_array";
v1cmd_str="dsi_set_cmdq"
cur_num_list=[];
for cur_line in lines:

	if len(cur_line) < 6:
		continue;
	#print cur_line
	cc=cur_line.strip().strip("\t");
	print cc;
	#skip the notions.
	if cc[0] == '/': 
		continue;

	#for delay


	if cc.find("MDELAY") != -1:
		clist=cc.split("(")[1].split(")");
		print clist
		out_str = "%s\n<LCM_FUNC_UTIL LCM_UTIL_MDELAY 1 %s>," % (out_str, str(clist[0]));

	#process: data_array[1] = 0x000063d4;
	if cc.find(array_str)!= -1 and cc.find("=") != -1:
		print cc.split("=")[1].split(";")[0];
		cur_data=cc.split("=")[1].split(";")[0].strip().strip("\t");
		cur_num=cur_data.split("0x")[1];
		if len(cur_num) != 8:
			print "error data_array len error, not 32bit !!! @@@@@@@@@@@@@@@@@@@@@@@@@@@"
			exit();
		else:
			print cur_num;
			cur_num_list.append(cur_num);
	#process: dsi_set_cmdq(data_array, 2, 1);
	if cc.find(v1cmd_str)!= -1 and cc.find(array_str) != -1:
		cur_num_len = len(cur_num_list);
		print cur_num_len
		out_str="%s\n<LCM_FUNC_CMD LCM_UTIL_WRITE_CMD_V1 %d %d" % (out_str, cur_num_len*4+1, cur_num_len);
		for cnum in cur_num_list:			
			out_str="%s 0x%s 0x%s 0x%s 0x%s" % (out_str, cnum[6:8], cnum[4:6], cnum[2:4], cnum[0:2]);
		out_str="%s>," % (out_str);
#		out_str="%s\n%s", (out_str, cur_str)
		cur_num_list=[];
		
	'''
	clist=cc.split();
	print clist;
	if len(clist) <= 0:
		continue;
	if clist[0].find("REGFLAG_DELAY") != -1:
		out_str = "%s\n<LCM_FUNC_UTIL LCM_UTIL_MDELAY 1 %s>," % (out_str, str(clist[1]));
	else:
		cur_str="<LCM_FUNC_CMD LCM_UTIL_WRITE_CMD_V2 %d" % len(clist)
		for idd in clist:
			cur_str = "%s %s" % (cur_str, str(idd));
		cur_str = "%s>," % cur_str;
		print cur_str;
		out_str = "%s\n%s" % (out_str, cur_str)
'''
print out_str;
