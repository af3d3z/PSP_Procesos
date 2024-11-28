from multiprocessing import Pool

def square(number):
    return number*number

if __name__ == '__main__':
    with Pool(processes=3) as pool:
        numbers = range(100000)
        results = pool.map(square, numbers)
    
    print("Results:", results)