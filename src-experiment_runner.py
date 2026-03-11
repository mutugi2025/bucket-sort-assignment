import time
import csv
from data.dataset_generator import generate_dataset
from src.bucket_sort import bucket_sort

sizes = [1,2,3,4,5,10,250,999,9999,89786,789300,1780000]

def run_experiments():

    with open("results/experiment_results.csv","w",newline="") as file:

        writer = csv.writer(file)
        writer.writerow(["Size","Time"])

        for size in sizes:

            print("Running test for size:", size)

            data = generate_dataset(size)

            start = time.time()

            bucket_sort(data)

            end = time.time()

            runtime = end - start

            writer.writerow([size,runtime])

            print("Completed:", size)
            print("Time:", runtime)
            print("----------------------")