import time
import dis

def writing(task, delay):
    while task:
        print("function1")
        time.sleep(delay)
        task -= 1

def reading(task, delay):
    while task:
        print("function2")
        time.sleep(delay)
        task -= 1

# Run functions
writing(3, 1)
reading(3, 1)

# Bytecode
print("Bytecode for writing:")
dis.dis(writing)
print("\nBytecode for reading:")
dis.dis(reading)

# Instruction count
w_instr = list(dis.get_instructions(writing))
r_instr = list(dis.get_instructions(reading))

print("Writing Instructions:", len(w_instr))
print("Reading Instructions:", len(r_instr))
print("Total Instructions:", len(w_instr) + len(r_instr))

# Variable lookups (local-only)
def count_load_fast(instrs):
    return sum(1 for instr in instrs if instr.opname == "LOAD_FAST")

print("Writing LOAD_FAST lookups:", count_load_fast(w_instr))
print("Reading LOAD_FAST lookups:", count_load_fast(r_instr))
print("Variables used:", ["task", "delay"])