ppg_data = []
pcg_data = []
fs1 = 125
fs2 = 4000
import matplotlib.pyplot as plt
# from scipy.signal import find_peaks
#file_name = "pvs_manh_nhe.txt"
# file_name = "pcg_ppg.txt"
file_name1 = "106/PCG.TXT"
import csv
windowsize = int(fs1/10)
# with open(file_name1, mode='r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # Duyệt qua từng dòng trong tệp CSV
#     for row in csv_reader:
#         if len(row) >= 2:  # Đảm bảo có ít nhất 2 cột trong mỗi dòng
#             column_0_data = float(row[0])
#             pcg_data.append(column_0_data)
with open(file_name1, 'r') as file:
    # Đọc từng dòng trong tệp
    for line in file:
        # Loại bỏ khoảng trắng ở đầu và cuối dòng
        stripped_line = line.strip()
        # Kiểm tra xem dòng có rỗng không
        if stripped_line:
            # Thử chuyển đổi dòng thành số nguyên
            try:
                number = int(stripped_line)
                pcg_data.append(number)
            except ValueError:
                print(f"Ignoring invalid literal: {stripped_line}")
# Mở tệp văn bản
# with open(file_name1, 'r') as file:
#     # Đọc tất cả các dòng trong tệp và chuyển đổi thành một danh sách các số nguyên
#     pcg_data.append([int(line.strip()) for line in file])
file_name2 = "PPG.TXT"
with open(file_name2, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Duyệt qua từng dòng trong tệp CSV
    for row in csv_reader:
        if len(row) >= 2:  # Đảm bảo có ít nhất 2 cột trong mỗi dòng
            column_0_data = float(row[1])
            ppg_data.append(column_0_data)        
indices_ppg = [i for i in range(0, len(ppg_data) * 14, 14)]
indices_pcg = [i for i in range(len(pcg_data))]
fig, axs = plt.subplots(2, 1, sharex = True)
axs[0].plot(indices_ppg, ppg_data)
# for value in ampl_ppg_data_filtered:
#     axs[0].plot(value, median_data[value], "r*")
axs[0].set_xlabel("Indice")
axs[0].set_ylabel("Value adc from LED")
axs[0].set_title("Data from red LED")

axs[1].plot(indices_pcg, pcg_data)
# for value in ampl_pcg_data_filtered:
#     axs[1].plot(value, pcg_filtered[value], "r*")
axs[1].set_xlabel("Indice")
axs[1].set_ylabel("Value adc from speaker")
axs[1].set_title("Data from speaker")
plt.show() 
####################################################  
# import matplotlib.pyplot as plt

# # File paths
# file_path1 = 'Sys_ppg_pcg//PPG_red_1.TXT'
# file_path2 = 'Sys_ppg_pcg//PCG_red_1(1).TXT'

# # Function to read data from file
# def read_data(file_path):
#     values = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             # Skip empty lines
#             if not line.strip():
#                 continue
#             # Split line and convert the first value to float
#             value = line.strip().split(',')[0]
#             try:
#                 values.append(float(value))
#             except ValueError:
#                 # Handle non-numeric values
#                 continue
#     return values

# # Read data from both files
# pcg_data = read_data(file_path1)
# ppg_data = read_data(file_path2)

# # Create subplots
# plt.figure(figsize=(12, 6))

# # Plot PPG data
# plt.subplot(2, 1, 1)
# plt.plot(ppg_data, color='red', linestyle='-', label='PPG data')
# plt.xlabel('Index')
# plt.ylabel('PPG Data')
# plt.title('PPG Data')
# plt.legend()
# plt.grid(True)

# # Plot PCG data with markers for all points
# plt.subplot(2, 1, 2)
# plt.plot(pcg_data, color='blue', linestyle='-', label='PCG data')
# plt.scatter(range(len(pcg_data)), pcg_data, color='blue', marker='o', label='PCG data points')  # Mark all points with circles
# plt.xlabel('Index')
# plt.ylabel('PCG Data')
# plt.title('PCG Data')
# plt.legend()
# plt.grid(True)

# # Adjust layout
# plt.tight_layout()

# # Show plots
# plt.show()