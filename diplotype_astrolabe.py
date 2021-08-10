#!/usr/bin/env python

import sys, getopt
from typing import BinaryIO, Dict, Any
from pprint import pprint
import pandas as pd
import numpy as np
import io
import re
import itertools
from itertools import combinations
import os

def create_diplotype(astrolabefile,mappingfile):

	########################astrolabe.out.txt############################
	##Called on: 2020/05/21 15:23:53
	##Astrolabe version: 0.8.7.0
	##Astrolabe author: Greyson Twist
	##Input File: /tarafs/biobank/data/home/pkaewpro/popgen/ver38/HS14003.vcf.gz
	#ROI_label    diplotype labels    diplotype activity    diplotype calling notes    jaccard    part    pValue    ROI notes    special case    nomenclature version
	#CYP2D6    CYP2D6*10/CYP2D6*10    ?/?        0.5652173913043478    0.7222222222222222    p: 0.0        possible gene duplication detected in BAM    PharmVar.v1.1.3
	#CYP2D6    CYP2D6*35/CYP2D6*39 or CYP2D6*39/CYP2D6*41    ?/? or ?/?    ,     0.4583333333333333    0.6285714285714286    p: 0.0            PharmVar.v1.1.3

	#######################CYP2D6_with_guideline.txt#############################
	#*1
	#*2
	#*9x2
	#*17x2
	#*27
	#*29x2
	#*33
	#*34

#### create dictionary of CYP2D6_with_guideline
	guideline ={}
	for line in mappingfile:
	   haplotype_guideline = line.strip()
	   guideline[haplotype_guideline] = 1

#### check astrolabe file
	guide_diplotype =[]
	print_diplotype =[]
	diplotype =[]

	for line in astrolabefile:
		line = line.strip()
		if re.search(r'##Input File:', line):
			path = line.split()[2]
			sampleid = os.path.splitext(os.path.basename(path))[0].split(".")[0]
		if not re.search(r'^#', line):
			diplotype_tmp = line.split("\t")[1] #diplotype
			if re.search(r'or', diplotype_tmp) :
				diplotype = diplotype_tmp.split(" or ")
			else:
				diplotype.append(diplotype_tmp)
			#print (f"from astrolabe = {diplotype}")
	
	for d in diplotype:
		if d == "./.": ## no diplotype
			guide_diplotype.append("Unknown/Unknown") #exit
			print_diplotype.append("?/?") #exit
		else: #has diplotype convert to alt
			d = re.sub(r'CYP2D6', '', d)
			#check each haplotype in diplotype
			haplist = d.split("/")
			guide_diplotype_tmp =[]
			guide_diplotype_tmp_2 =[]
			print_diplotype_tmp =[]
			print_diplotype_tmp_2 =[]
			for i in haplist:
				if re.search(r'[A-Za-z]', i): #hap has alphabet
					hap = re.sub(r'[A-Za-z]', '', i)
					guide_diplotype_tmp_2.append("?")
					print_diplotype_tmp_2.append(i)
				else:
					hap = i
					guide_diplotype_tmp_2.append(i)
					print_diplotype_tmp_2.append(i)
				if hap in guideline:
					print_diplotype_tmp.append(hap)
					guide_diplotype_tmp.append(hap)
				else:
					print_diplotype_tmp.append(hap)
					guide_diplotype_tmp.append("Unknown")
			#all hap
			#print (f"guide_diplotypetmp = {guide_diplotype_tmp}")
			#print (f"print_diplotypetmp = {print_diplotype_tmp}")
			
			print_diplotype.append(f"{print_diplotype_tmp[0]}/{print_diplotype_tmp[1]}")
			guide_diplotype.append(f"{print_diplotype_tmp[0]}/{print_diplotype_tmp[1]}")
			
			if print_diplotype_tmp_2 and guide_diplotype_tmp_2 :
				print_diplotype.append(f"{print_diplotype_tmp_2[0]}/{print_diplotype_tmp_2[1]}")
				guide_diplotype.append(f"{guide_diplotype_tmp_2[0]}/{guide_diplotype_tmp_2[1]}")

		
   # print (f"guide_diplotype = {guide_diplotype}")
   # print (f"print_diplotype = {print_diplotype}")
			
	#f= open(f"{sampleid}_diplotype_CYP2D6.tsv","w+")
	f= open(f"diplotype_CYP2D6.tsv","w+")
	f.write(f"sampleid\tgene\tguide_diplotype\tprint_diplotype\n")
	f.write(f"{sampleid}\tCYP2D6\t")
	f.write(f"{guide_diplotype}\t")
	f.write(f"{print_diplotype}\n")
	f.close()

	return


#input = hla_result.txt
astrolabedata = sys.argv[1]
mapping = sys.argv[2]
astrolabefile = open(astrolabedata, "r")
mappingfile = open(mapping, "r")

create_diplotype(astrolabefile,mappingfile)
