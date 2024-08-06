import os
from file_check import check_files
from process_files import read_csv_files
from data_quality_check import validate_and_clean_data

def main():
    folder_path = "D:/Zomato"
    invalid_folder = "C:/Users/akash/Zomato Daily/invalid_files"
    processed_folder = "C:/Users/akash/Zomato Daily/processed_files"
    bad_records_folder = "C:/Users/akash/Zomato Daily/bad_records"
    processed_files = set()

    if not os.path.exists(invalid_folder):
        os.makedirs(invalid_folder)

    if not os.path.exists(processed_folder):
        os.makedirs(processed_folder)

    if not os.path.exists(bad_records_folder):
        os.makedirs(bad_records_folder)

    valid_files = check_files(folder_path, processed_files, invalid_folder)

    if valid_files:
        all_data = read_csv_files(valid_files)
        if not all_data.empty:
            required_fields = ['address', 'reviews_list']
            cleaned_data, bad_records = validate_and_clean_data(all_data, required_fields)
            
            if not cleaned_data.empty:
                output_file = os.path.join(processed_folder, "cleaned_combined_data.csv")
                cleaned_data.to_csv(output_file, index=False)
                print(f"Cleaned data saved to {output_file}")
                
            if not bad_records.empty:
                bad_records_file = os.path.join(bad_records_folder, "bad_records.csv")
                bad_records.to_csv(bad_records_file, index=False)
                print(f"Bad records saved to {bad_records_file}")

        else:
            print("No valid data to display.")
    else:
        print("No valid files to process.")

if __name__ == "__main__":
    main()
