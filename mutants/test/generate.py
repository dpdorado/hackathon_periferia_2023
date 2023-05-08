import csv
import random

def generate_data(num_records):
    data = []
    for _ in range(num_records):
        dna = [''.join(random.choices(['A', 'T', 'C', 'G'], k=6)) for _ in range(6)]
        is_mutant = random.choice([True, False])
        if len(dna) != 6 or any(len(seq) != 6 for seq in dna):
            status_code = 400  # Datos incorrectos
        elif is_mutant:
            status_code = 200  # Mutante
        else:
            status_code = 403  # No mutante
        data.append({'dna': dna, 'is_mutant': is_mutant, 'status_code': status_code})
    return data

def save_data_to_csv(data, filename):
    fieldnames = ['dna', 'is_mutant', 'status_code']
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

num_records = 1000
data = generate_data(num_records)
save_data_to_csv(data, 'datos_test.csv')
