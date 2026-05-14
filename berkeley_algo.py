def berkeley_algorithm(time_offsets):
    #Calculate the average time offset
    avg_offset = sum(time_offsets) / len(time_offsets)
    
    #Adjust the clocks
    adjusted_clocks = [time - avg_offset for time in time_offsets]
    
    return adjusted_clocks

time_offsets = [1.2, 0.5, -0.3, 2.1, -1.0]
adjusted_clocks = berkeley_algorithm(time_offsets)
print(adjusted_clocks)
    