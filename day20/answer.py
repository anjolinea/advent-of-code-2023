from collections import deque
from math import lcm

modules = {}
conj_module_inputs = []

with open("input.txt") as fhand:
    for line in fhand:
        line = line.strip()
        module_in, modules_out = tuple(line.split("->"))
        module_in = module_in.strip()
        # flip-flop
        if module_in[0] == "%":
            module_type = "F" 
            module_in = module_in[1:]
            module_status = "off"
        # conjunction
        elif module_in[0] == "&":
            module_type = "C" 
            module_in = module_in[1:]
            module_status = {}
            conj_module_inputs.append(module_in)
        # broadcast
        else:
            module_type = "B" 
            module_status = None
        modules_out = [x.strip() for x in modules_out.split(",")]
        modules[module_in] = {"module_type" : module_type, 
                              "modules_out": modules_out, 
                              "module_status" : module_status}
        
for k, v in modules.items():
    for k1 in conj_module_inputs:
        if k1 in v["modules_out"]:
            # True = high, False = low
            modules[k1]["module_status"][k] = False


def part_one():
    # (receiver, type of pulse, sender)
    num_high = 0
    num_low = 0

    for _ in range(1000):
        queue = deque([("broadcaster", False, None)])
        while queue:
            module_in, is_high, sender = queue.popleft()

            if is_high:
                num_high += 1
            else:
                num_low += 1

            if module_in not in modules:
                continue

            module_type, modules_out, module_status = tuple(modules[module_in].values())

            if module_type == "F": # flip flop
                if not is_high: # low
                    if module_status == "off":
                        modules[module_in]["module_status"] = "on"
                        send_out_high = True
                    else:
                        modules[module_in]["module_status"] = "off"
                        send_out_high = False
                    for mo in modules_out:
                        queue.append((mo, send_out_high, module_in))
            elif module_type == "C":
                # if sender sends a high or low
                if is_high:
                    modules[module_in]["module_status"][sender] = True
                else:
                    modules[module_in]["module_status"][sender] = False

                if all(modules[module_in]["module_status"].values()): # all high
                    send_out_high = False
                else:
                    send_out_high = True

                for mo in modules_out:
                    queue.append((mo, send_out_high, module_in))
            else:
                for mo in modules_out:
                    queue.append((mo, is_high, module_in))

    print(num_high * num_low)
                

def part_two():
    """
    Using the fact that the input looks similar to this: 
    https://www.reddit.com/r/adventofcode/comments/18mypla/2023_day_20_input_data_plot/

    WRT to graph above:
        Last pulses sent to qt must be all high pulses
        kk, gl, mr, bb are essentially NOT gates, thus need a low pulse from cr, jx, nl, and vj resp.
        Low pulses from cr, jx, nl, vj require last pulses to be all high.

    Within a cycle (say, the one with vj and cm):
        When the broadcaster ends low to cm, this is essentially a "plus one" operation
        Think of ON as carrying 1 and OFF as 0. When a low is sent, the "ONs" will send a low (plus one operation)
        and become OFF (0). When lows are send to OFFs, they turn on and don't send anything. Binary addition. 

        All inputs of vj will send highs when the ending status of the input nodes are ON (otherwise, one of the last pulses sent will be low). 
        To get to there, we need 111101111111 = 3967 button presses. When this happens, vj will send low to bb, cm, and qc.
            When sent to qc, qc, which was OFF, will be ON, so the status will be 111111111111
            When sent to cm (which will always be after qc), the plus one will cascade so the status will be now 000000000000 (reset)
            When sent to bb, bb will receive a low pulse and transform it to a high pulse to send to qt.

    This pattern is the same for all the other cycles.
    The only time we get all low pulses from vj, nl, cr, jx are the multiples of how many button presses it takes to have all their input nodes ON.
    Thus, we calculate the LCM of them.
    """

    ans = 1
    broadcaster_outputs = modules["broadcaster"]["modules_out"]
    for bo in broadcaster_outputs:
        end = list(filter(lambda x: modules[x]["module_type"] == "C", modules[bo]["modules_out"]))[0]
        current = bo
        num = ""
        while True:
            modules_out = modules[current]["modules_out"]
            if end in modules_out:
                num += "1"
            else:
                num += "0"

            if [end] == modules_out: # end
                break
            
            modules_out = list(filter(lambda x: x != end, modules_out))
            current = modules_out[0]
        num = int(num[::-1], 2)
        ans *= num
    print(ans)

part_one()