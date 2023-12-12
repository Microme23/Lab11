import os
import csv

def display_csv(file_name):
    desired_columns = [0, 1, 2, 3, 62, 63]
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > max(desired_columns):
                selected_data = [row[i] for i in desired_columns]
                print(selected_data)
            else:
                print("Не достатньо колонок в рядку")

def search_and_write_csv(input_countries, input_file, output_file):
    result_rows = []

    file_path = os.path.join(os.getcwd(), input_file)
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        
        desired_columns = [0, 1, 62, 63]

        result_header = ["Country Name", "Country Code", "2018", "2019"]

        for row in reader:
            if len(row) > max(desired_columns):
                country = row[0]
                if country in input_countries:
                    country_code = row[1]
                    year_2018 = row[62] if 62 < len(row) else "N/A"
                    year_2019 = row[63] if 63 < len(row) else "N/A"
                    result_rows.append([country, country_code, year_2018, year_2019])

    if not result_rows:
        print("Немає даних для введених країн.")
        return

    output_path = os.path.join(os.getcwd(), output_file)
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(result_header)
        writer.writerows(result_rows)

csv_file_name = 'API_NE.EXP.GNFS.ZS_DS2_en_csv_v2_5995190.csv'
display_csv(csv_file_name)

search_countries = input("Введіть назви країн для пошуку (розділені пробілом та повні назви англійською): ").split()
output_csv_file = 'result.csv'

search_and_write_csv(search_countries, csv_file_name, output_csv_file)
print(f"Результати пошуку збережено у файлі: {output_csv_file}")