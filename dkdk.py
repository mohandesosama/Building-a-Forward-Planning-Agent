costs=[2,3,4,5,6,1,2,3,5,9,4,2,3,5]
max_level_cost=0
for cost in costs:
    #if cost > max_level_cost:
    #    max_level_cost = cost
    max_level_cost=max(cost,max_level_cost)
    break
print(max_level_cost)