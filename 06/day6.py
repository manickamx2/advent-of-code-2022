########## PART 1 ##########

with open('day6-input.txt') as f:
    lines = f.readlines()


def find_packet_marker_start_position(packet):
    window_size = 4
    s = 0
    for r, c in enumerate(packet):
        if r < window_size:
            continue

        window = set(packet[s:r])
        if len(window) == window_size:
            return r
        else:
            s += 1


for line in lines:
    start = find_packet_marker_start_position(line)
    print(f"packet start position: {start}")
