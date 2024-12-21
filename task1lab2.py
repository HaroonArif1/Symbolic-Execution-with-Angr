import angr
import os
import argparse
# from angrutils import *
import angrutils, subprocess #EXplain angru utilites why we use that

binary_input = angr.Project("test", load_options={"auto_load_libs" : False})

cfg = binary_input.analyses.CFGFast(data_references=True, normalize=True)

nodelist = list(cfg.graph.nodes) # declartion
edgelist = list(cfg.graph.edges)

nodelist1 = [node for node in list(cfg.graph.nodes) if node.block !=None] #call the list
print("number of nodges in the grapgh :",len(nodelist))
print("number of  edges in the grapgh :",len(edgelist))


allIns = set()
for node in nodelist1:
	for ins in ((node.block.disassembly.insns)):
	   allIns.update({ins.mnemonic})

print(allIns)
print(" number of differnt instruction types :" ,len(allIns))



angrutils.plot_cfg(cfg, "cfg", asminst=True, format="raw")
subprocess.run(['dot', '-Tpng', '-o', "cfg.png", "cfg.raw"]); # Define the type of require file
