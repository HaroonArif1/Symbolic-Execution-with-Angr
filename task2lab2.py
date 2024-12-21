import angr
import sys
proj = angr.Project("test", load_options={"auto_load_libs" : False})
cfg = proj.analyses.CFGFast()
nodelist1 = list(cfg.graph.nodes)
edgelist1 = list(cfg.graph.edges)
for node in nodelist1:
	if node.block is None:
		continue
	for insn in node.block.capstone.insns:
		mne = insn.mnemonic
		if mne == 'call':
			#print("op str "+ insn.op_str)
			#print("addr: " + str(hex(insn.address))+ "\n")
		
			if insn.op_str.endswith("1070"): #Put call address
				addr_target = insn.address
				#print(hex(addr_target))
				
				initial_state = proj.factory.entry_state(add_options = {angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
				angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS}
				)
				
				sm = proj.factory.simulation_manager(initial_state) #handling
				sm.explore(find=addr_target)
				
				if sm.found: 
					solution_state = sm.found[0]
					print(solution_state.posix.dumps(sys.stdin.fileno()).decode())
				else:
					raise Exception ("could not found")
				
