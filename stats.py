from math import floor

def sqrt(num):
    return (num)**(1/2)

def mean(dataset: list):
    sum = 0
    for i in dataset:
        sum += i
    
    avg = sum / len(dataset)
    return avg

def sum(dataset: list):
    sum = 0
    for i in dataset:
        sum += i
    
    return sum

def median(dataset: list):
    ordered_list = sorted(dataset)

    if len(ordered_list) % 2 == 0:
        median = (ordered_list[int(len(ordered_list) / 2)] + ordered_list[int((len(ordered_list) / 2) - 1)]) / 2
        return median
    else:
        return ordered_list[int((len(ordered_list) // 2))]

def median_index(dataset: list):
    ordered_list = sorted(dataset)
    index = 0
    if len(ordered_list) % 2 == 0:
        index += ((int(len(ordered_list) / 2) + int((len(ordered_list) / 2) - 1)) / 2)
        return floor(index)
    else:
        return int((len(ordered_list) // 2))

def SD_population(dataset: list):
    N = len(dataset)
    summation = 0
    avg = mean(dataset)
    for i in range(len(dataset)):
        summation += ((dataset[i] - avg)**2)

    SD = sqrt(summation / N)

    return SD

def variance_population(dataset: list):
    return round(SD_population(dataset)**2, 6)

def mean_with_frequency(data_range: list, frequency: list):
    try:
        sum = 0
        sum_freq = 0
        if len(data_range) == len(frequency):
            for i in range(len(data_range)):
                x = data_range[i] * frequency[i]
                y = frequency[i]
                sum += x
                sum_freq += y
        
        avg = sum / sum_freq
        return avg
    except Exception as e:
        print(e)

def list_with_frequency(data_range: list, frequency: list):
    try:
        if len(data_range) == len(frequency):
            count = 0
            dataset = []
            for x, y in enumerate(frequency):
                while count < y:
                    dataset.append(data_range[x])
                    count += 1
                count = 0

            return dataset
    except Exception as e:
        print(e)

def summation_with_range(data_range: list, frequency: list):
    sum = 0
    for i in range(len(data_range)):
        x = data_range[i] * frequency[i]
        sum += x
    return sum

def mean_with_frequency(data_range: list, frequency: list):
    sum = summation_with_range(data_range, frequency)
    length = len(list_with_frequency(data_range, frequency))

    avg = sum / length
    return avg

def fx2(data_range: list, frequency: list):
    sum = 0
    for i in range(len(data_range)):
        x = frequency[i] * (data_range[i] ** 2)
        sum += x
    return sum

def variance_with_frequency(data_range: list, frequency: list):
    variance = (fx2(data_range, frequency) / len(list_with_frequency(data_range, frequency))) - (mean_with_frequency(data_range, frequency)**2)
    #print(list_with_frequency(data_range, frequency))
    #print(len(list_with_frequency(data_range, frequency)))
    return variance

def SD_with_frequency(data_range: list, frequency: list):
    return sqrt(variance_with_frequency(data_range, frequency))

def median_with_frequency(data_range: list, frequency: list):
    return median(list_with_frequency(data_range, frequency))

def IQR(dataset: list):
    ordered_list = sorted(dataset)
    first_half = []
    second_half = []
    # print(median_index(dataset))
    index1 = 0
    index2 = median_index(ordered_list)
    for i in range(len(ordered_list)):
        
        if index1 < median_index(ordered_list):
            first_half.append(ordered_list[i])
            index1 += 1
        else:
            second_half.append(ordered_list[i])
            index2 += 1

    # print(first_half, second_half)
    print(f'1st quartile: {median(first_half)}')
    print(f'3rd quartile: {median(second_half)}')

    IQR = median(second_half) - median(first_half)
    print(f'IQR: {IQR}')
    return IQR

def IQR_with_frequency(data_range: list, frequency: list):
    return IQR(list_with_frequency(data_range, frequency))