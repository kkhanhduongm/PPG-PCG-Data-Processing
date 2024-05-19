# This code processes the data from the PPG and PCG sensors to find the systolic and diastolic peaks and calculate the ET and VTT values.
ppg_data = []
pcg_data = []
fs=500
fs1 = 250
fs2 = 4000
import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np
# from scipy.signal import find_peaks
#file_name = "pvs_manh_nhe.txt"
# file_name = "pcg_ppg.txt"
file_name1 = "240511/1715415199_114_65_90_khanh_0/PPG.TXT"
file_name2 = "240511/1715415199_114_65_90_khanh_0/PCG.TXT"

import csv
import pandas as pd
windowsize = int(fs1/8)
# with open(file_name1, mode='r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # Duyệt qua từng dòng trong tệp CSV
#     for row in csv_reader:
#         if len(row) >= 2:  # Đảm bảo có ít nhất 2 cột trong mỗi dòng
#             column_0_data = float(row[0])
#             pcg_data.append(column_0_data)
with open(file_name2, 'r') as file:
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
ppg_data = ppg_data[4000:]
pcg_data = pcg_data[(2500+4000):]
# Mở tệp văn bản
# with open(file_name1, 'r') as file:
#     # Đọc tất cả các dòng trong tệp và chuyển đổi thành một danh sách các số nguyên
#     pcg_data.append([int(line.strip()) for line in file])

with open(file_name1, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Duyệt qua từng dòng trong tệp CSV
    for row in csv_reader:
        if len(row) >= 2:  # Đảm bảo có ít nhất 2 cột trong mỗi dòng
            column_0_data = float(row[1])
            ppg_data.append(column_0_data)

indices_ppg = [i for i in range(0, len(ppg_data) * 16, 16)]

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
# plt.show()

ppg_data_filtered = pd.Series(ppg_data).rolling(window=windowsize, center=True).median()

# Define the filter parameters
lowcut = 25
highcut = 120
nyquist = 0.5 * fs2
low = lowcut / nyquist
high = highcut / nyquist

# Apply the bandpass filter to pcg_data
b, a = signal.butter(4, [low, high], btype='band')
pcg_data_filtered = signal.lfilter(b, a, pcg_data)
indices_pcg_data_filtered = [i for i in range(len(pcg_data_filtered))]

peaks_ppg, _ = signal.find_peaks(ppg_data_filtered, height=0, distance = 0.6*fs1)
peaks_pcg, _ = signal.find_peaks(pcg_data_filtered, height=0, prominence= 650, distance = 0.15*fs2)
# peaks_pcg_valley, _ = signal.find_peaks(-pcg_data_filtered, height=0, prominence= 500, distance = 0.3*fs2)

peaks_ppg_1 = [x * 16 for x in peaks_ppg]
print("pcg filer", ppg_data_filtered)
print("peak ppg multiply 16", peaks_ppg_1)
print("peak ppg",peaks_ppg)
print("peak pcg",peaks_pcg)

fig, axs = plt.subplots(2, 1, sharex=True)
axs[0].plot(indices_ppg, ppg_data_filtered)

for value in peaks_ppg:
    axs[0].plot(indices_ppg[value], ppg_data_filtered[value], "r*")
axs[0].set_xlabel("Indice")
axs[0].set_ylabel("Value adc from LED (Filtered)")
axs[0].set_title(f"Data from red LED (Filtered) - Total peaks: {len(peaks_ppg)}")

# Plot the filtered pcg_data
axs[1].plot(indices_pcg, pcg_data_filtered)
for value in peaks_pcg:
    axs[1].plot(value, pcg_data_filtered[value], "r*")
# for value in peaks_pcg_valley:
#     axs[1].plot(value, pcg_data_filtered[value], "g*")
axs[1].set_xlabel("Indice")
axs[1].set_ylabel("Value adc from speaker (Filtered)")
axs[1].set_title(f"Data from speaker (Filtered) - Total peaks: {len(peaks_pcg)}")

# plt.show()

indices_ppg_peak = [i for i in range(len(peaks_ppg))]
indices_pcg_peak = [i for i in range(len(peaks_pcg))]

VTT = []
# for value in indices_ppg_peak:
# #     nearest_peak_ppg = min(peaks_ppg, key=lambda x: abs(x - peak_pcg))
# #     VTT.append((nearest_peak_ppg - peak_pcg) / fs1)
# #
# # average_VTT = sum(VTT) / len(VTT)
#     VTT.append([(peaks_ppg[int(value)])] - (pcg_data_filtered[2 * value]))
# # print(ampl[int(value) ])
# # print(int(ampl1[2*value ]))
# indicesVTT = [i for i in range(len(VTT))]
# print(len(VTT))
# print(sum(VTT))
# averageVTT = sum(VTT) / len(VTT)
# plt.figure(" VTT ")
# plt.plot(indicesVTT, VTT)
# plt.xlabel('Số mẫu')
# plt.ylabel('Thời gian VTT')
# plt.title(f'Biểu đồ VTT, Giá trị VTT trung bình: {averageVTT/fs2}s' )
#plt.show()

ET = []
# for value in indices_pcg_data_filtered:
#     if value % 2 == 0 and value + 1 < len(peaks_pcg):
#         ET.append(peaks_pcg[value + 1] - peaks_pcg[value])
#
# averageET = sum(ET) / len(ET)
# indicesET = [i for i in range(len(ET))]

# plt.figure("ET")
# plt.plot(indicesET, ET)
# plt.xlabel('Sample Number')
# plt.ylabel('ET Value')
# plt.title(f'Biểu đồ ET, Giá trị ET trung bình: {averageET/fs2}s' )

# def find_closest_values(arr, target):
#     # Tính khoảng cách giữa mỗi giá trị trong mảng và giá trị mục tiêu
#     distances = [(abs(value - target), value) for value in arr]
#     # Sắp xếp các cặp (khoảng cách, giá trị) theo khoảng cách
#     sorted_distances = sorted(distances)

#     # Kiểm tra xem sorted_distances có rỗng không
#     if not sorted_distances:
#         return None, None

#     # Lấy ra giá trị gần nhất
#     closest_value = sorted_distances[0][1]

#     # Tìm giá trị gần thứ 2
#     second_closest_value = None
#     if len(sorted_distances) > 1:
#         second_closest_value = sorted_distances[1][1]

#     return closest_value, second_closest_value


systolic = []
diastolic = []
arr_i = []
arr_n = []

def find_closest_values(arr1, arr2):
    sys = []
    dia = []
    i = 0
    n = 0
    
    while i < len(arr1) - 1:
        while n < len(arr2) - 1:    
            if arr1[i] < arr2[n] < arr1[i+1]:
                if arr1[i] < arr2[n+1] < arr1[i+1]:
                    sys.append(arr2[n])
                    dia.append(arr2[n+1])
                    arr_i.append(i)
                    arr_n.append(n)
                    i += 1
                    n += 2
                else: 
                    n += 1
            else:
                n += 1
        i += 1
        if arr_n:
            n = arr_n[-1]
        else:
            n += 1
    return sys, dia

systolic, diastolic = find_closest_values(peaks_ppg_1, peaks_pcg)

print ('i ', arr_i)
print ('n ', arr_n)

print ('len ppg', len(peaks_ppg_1))
print ('len pcg', len(peaks_pcg))
print ('sys', systolic)
print ('dia', diastolic)
print ('len sys', len(systolic))
print ('len dia', len(diastolic))
            



# for value in peaks_ppg_1:
#     sys, dia = find_closest_values(peaks_pcg, value)
#     if sys is not None and dia is not None:
#         systolic.append(sys)
#         diastolic.append(dia)
#         print ('sys', sys)
#         print ('dia', dia)
#     else:
#         print("No closest values found.")
ET = [abs(s - d) / fs2 for s, d in zip(systolic, diastolic)]
averageET = sum(ET) / len(ET)
indicesET = [i for i in range(len(ET))]
plt.figure(" ET ")
plt.plot(indicesET, ET)
plt.xlabel('Số mẫu')
plt.ylabel('Thời gian ET')
plt.title(f'Biểu đồ ET, Giá trị ET trung bình: {averageET}s' )

VTT = [abs(a - s) / fs2 for a, s in zip(peaks_ppg_1, systolic)]
averageVTT = sum(VTT) / len(VTT)
indicesVTT = [i for i in range(len(VTT))]

plt.figure("VTT")
plt.plot(indicesVTT, VTT)
plt.xlabel('Sample Number')
plt.ylabel('VTT Value')
plt.title(f'Biểu đồ VTT, Giá trị VTT trung bình: {averageVTT}s' )

plt.show()



