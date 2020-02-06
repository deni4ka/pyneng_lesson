def parse_cdp_neighbors(command_output):
    dict1 = {}
    list1 = [command_output[7].split(), command_output[8].split(), command_output[9].split(), command_output[10].split()]
    for r, eth, lnum, *_, rnum in list1:
        dict1['SW1', eth + lnum] = r, eth + rnum

    return dict1


f = open('sh_cdp_n_sw1.txt')
a = parse_cdp_neighbors(f.read().split('\n'))
print(a)
f.close()

{('SW1', 'Eth0/1'): ('R1', 'Eth0/0'), ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'), ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'), ('SW1', 'Eth0/5'): ('R6', 'Eth0/1')}
