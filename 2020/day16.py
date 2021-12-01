import itertools
import re
import math
import copy

rules = """
departure location: 40-261 or 279-955
departure station: 33-375 or 394-963
departure platform: 39-863 or 877-970
departure track: 30-237 or 256-955
departure date: 47-731 or 741-950
departure time: 38-301 or 317-954
arrival location: 26-598 or 623-969
arrival station: 50-835 or 854-971
arrival platform: 44-535 or 549-958
arrival track: 36-672 or 685-967
class: 34-217 or 236-974
duration: 29-469 or 483-970
price: 45-111 or 120-965
route: 32-751 or 760-954
row: 25-321 or 339-954
seat: 38-423 or 438-958
train: 45-798 or 813-954
type: 40-487 or 503-954
wagon: 46-916 or 938-949
zone: 25-160 or 184-957
""".strip()

my_ticket = [73,59,83,127,137,151,71,139,67,53,89,79,61,109,131,103,149,97,107,101]

with open('input.txt', 'r') as f:
  nearby_tickets = [[int(num) for num in line.strip().split(',')] for line in f]

rulesd = {}
for rule in rules.split("\n"):
    matches = re.match(r"^([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)$", rule)
    
    rulesd[matches.group(1)] = ((int(matches.group(2)), int(matches.group(3))), (int(matches.group(4)), int(matches.group(5))))

# Part A ..ish

invalid_sum = 0

invalid_tickets = []

for ticket in nearby_tickets:
    for ticket_num in ticket:
        valid_somewhere = False
        for rule in rulesd:
            range1, range2 = rulesd[rule]
        
            if ticket_num >= range1[0] and ticket_num <= range1[1]:
                valid_somewhere = True
                break
        
            elif ticket_num >= range2[0] and ticket_num <= range2[1]:
                valid_somewhere = True
                break
        
        if not valid_somewhere:
            invalid_sum += ticket_num
            invalid_tickets.append(ticket)
            break

print(invalid_sum)

# Part B
            
valid_tickets = [x for x in nearby_tickets if x not in invalid_tickets]

possibilites = {}
for rule in rulesd:
    possibilites[rule] = [False for x in range(len(my_ticket))]


for rule in rulesd:
    range1, range2 = rulesd[rule]
    for col_idx in range(len(my_ticket)):
        col_match = True
        for ticket in valid_tickets:
            ticket_num = ticket[col_idx]
            if not ((ticket_num >= range1[0] and ticket_num <= range1[1]) or
                (ticket_num >= range2[0] and ticket_num <= range2[1])):
                col_match = False
                break
        
        possibilites[rule][col_idx] = col_match

results = {}
while len(results) < len(possibilites):
    for p in possibilites:
        if len([x for x in possibilites[p] if x]) == 1:
            col_idx = possibilites[p].index(True)
            results[p] = col_idx
            for p1 in possibilites:
                possibilites[p1][col_idx] = False

product  = 1
for r in results:
    if 'departure' in r:
        product *= my_ticket[results[r]]

print(product)