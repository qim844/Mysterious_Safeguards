def main():
    # Read input and put data into a list
    input_file = open('1.in','r')
    lines = input_file.readlines()

    N = int(lines[0])
    lifeguard_list = []

    for i in range(1, N+1):
        time_interval = lines[i].split(" ")
        start = int(time_interval[0])
        end = int(time_interval[1])

        lifeguard_shift = [start,end]
        lifeguard_list.append(lifeguard_shift)

    # Calcuate the max coverage with 1 lifeguard fired
    total_coverage_set = set()
    each_coverage_list = []

    for i in range(0,len(lifeguard_list)):
        lifeguard = lifeguard_list[i]
        for x in range(lifeguard[0], lifeguard[1]):
            total_coverage_set.add(x)

        if i == 0:
            actual_coverage = len(total_coverage_set)
            prev_coverage = len(total_coverage_set)
        else:
            actual_coverage = len(total_coverage_set) - prev_coverage
            prev_coverage = len(total_coverage_set)

        each_coverage_list.append(actual_coverage)

    max_coverage = len(total_coverage_set) - min(each_coverage_list)

    # Generate output file
    output_file = open("1.out", "w")
    output_file.write(str(max_coverage))
    output_file.close()

main()
