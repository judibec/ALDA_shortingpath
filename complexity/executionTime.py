import time
from complexity import constants
from complexity import dataGenerator
from functions import shortingPath as s


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


def take_times(size, samples_by_size):
    samples = []
    samplesfloyd = []
    for _ in range(samples_by_size):
        samples.append(dataGenerator.generar_grafo_con_pesos(size, size))
        samplesfloyd.append(dataGenerator.generar_grafo_con_pesos(size // 10, size // 10))
    return [
        take_time_for_algorithm(samples, s.dijkstra),
        take_time_for_algorithm(samples, s.bellman_ford),
        take_time_for_algorithm(samplesfloyd, s.floyd_warshall),
    ]


def take_time_for_algorithm(samples_array, sorting_approach):
    times = []
    for sample in samples_array:
        start_time = time.time()
        n = "0"
        sorting_approach(sample.copy(), n)
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return times[len(times) // 2]
