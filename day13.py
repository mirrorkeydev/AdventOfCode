import math

with open('input.txt', 'r') as f:
  input = [line.strip() for line in f]

min_time = int(input[0])

# Part A

busses = [int(num) for num in input[1].split(',') if num != 'x']

cur_time = min_time
while True:
    for bus in busses:
        if cur_time % bus == 0:
            print(bus* (cur_time-min_time))
            exit()
    cur_time += 1

# Part B

bus_list = [(int(num), i) for i, num in enumerate(input[1].split(',')) if num != 'x']
bus_list = sorted(bus_list, key= lambda x: -x[0])
print(bus_list)

# stolen from https://math.stackexchange.com/questions/2218763/how-to-find-lcm-of-two-numbers-when-one-starts-with-an-offset
# as if I know the math hahaha
def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    """Combine two phased rotations into a single phased rotation

    Returns: combined_period, combined_phase

    The combined rotation is at its reference point if and only if both a and b
    are at their reference points.
    """
    gcd, s, _ = extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase


def arrow_alignment(red_len, green_len, advantage):
    """Where the arrows first align, where green starts shifted by advantage"""
    period, phase = combine_phased_rotations(
        red_len, 0, green_len, -advantage % green_len
    )
    return -phase % period


def extended_gcd(a, b):
    """Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

cur_phase = bus_list[0][1]
cur_period = bus_list[0][0]
for i, (num, offset) in enumerate(bus_list, 1):
    period, phase = combine_phased_rotations(cur_period, cur_phase, num, offset)
    cur_phase = phase
    cur_period = period
    print(period, phase)

# print(bus_list)
