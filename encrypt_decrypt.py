#!usr/bin/env python

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
import sys
import time


class Ui_Main_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 348)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1_EY50YzYGk9JkYo6K779u-A.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_enc_dec = QtWidgets.QLabel(self.centralwidget)
        self.label_enc_dec.setGeometry(QtCore.QRect(40, 60, 121, 17))
        self.label_enc_dec.setObjectName("label_enc_dec")
        self.Input_text_field = QtWidgets.QLineEdit(self.centralwidget)
        self.Input_text_field.setGeometry(QtCore.QRect(160, 60, 331, 25))
        self.Input_text_field.setClearButtonEnabled(True)
        self.Input_text_field.setObjectName("Input_text_field")
        self.Btn_Encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Encrypt.setGeometry(QtCore.QRect(200, 120, 89, 25))
        self.Btn_Encrypt.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Btn_Encrypt.setObjectName("Btn_Encrypt")

        self.Btn_Encrypt.clicked.connect(self.encrypt_btn)

        self.Btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_decrypt.setGeometry(QtCore.QRect(360, 120, 89, 25))
        self.Btn_decrypt.setObjectName("Btn_decrypt")

        self.Btn_decrypt.clicked.connect(self.decrypt_btn)

        self.Output_text_field = QtWidgets.QTextEdit(self.centralwidget)
        self.Output_text_field.setGeometry(QtCore.QRect(160, 170, 331, 70))
        self.Output_text_field.setObjectName("Output_text_field")
        self.labelOutput = QtWidgets.QLabel(self.centralwidget)
        self.labelOutput.setGeometry(QtCore.QRect(60, 190, 91, 31))
        self.labelOutput.setObjectName("labelOutput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encryption Decryption Technique Using Matrix"))
        self.label_enc_dec.setText(_translate("MainWindow", "Enter Your Data"))
        self.Btn_Encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.Btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.labelOutput.setText(_translate("MainWindow", "OutPut Data"))

    def encrypt_btn(self):
        time_start = time.perf_counter()

        data = self.Input_text_field.text()
        self.Output_text_field.setText("")
        try:
            if data.isdigit():
                data_l = []
                for i in range(0, len(data), 8):
                    d_ta = data[i:i + 8]
                    data_l.append(d_ta)

                array = []
                array_row_parity = []
                fifth_array = []
                parity_row_array = []
                int_value_of_arr_row1 = []
                int_value_of_arr_row2 = []
                int_value_of_arr_row3 = []
                int_value_of_arr_row4 = []
                en_cypher = []
                equalCount = 0
                dtb_list = []

                def list_equalizer(arr, eual_Count):
                    len_vlu = len(arr)
                    for i in range(1):
                        if len_vlu == 8:
                            pass
                        elif len_vlu < 8:
                            for i in range(len_vlu, 8):
                                arr.append('0')
                                eual_Count += 1

                    return arr, eual_Count

                def row_bit_adder(arr):
                    counter = 0
                    len_vlu = len(arr)
                    if len_vlu == 8:
                        for iNc in range(len_vlu):
                            if arr[iNc] == '1':
                                counter += 1
                        if counter % 2 == 0:
                            arr.append('0')
                        else:
                            arr.append('1')
                    return arr

                for i in range(len(data_l)):
                    first_arr, equal_counter_value = list_equalizer(list(data_l[i]), equalCount)
                    array.append(first_arr)

                def decimal_to_binary(n):
                    return bin(n).replace("0b", "0")

                dtb = decimal_to_binary(equal_counter_value)
                for i in range(len(dtb)):
                    dtb_list.append(dtb[i])

                def dtb_equilizer(dtb_list):
                    if len(dtb_list) == 4:
                        pass
                    elif len(dtb_list) == 3:
                        dtb_list.insert(0, "0")
                    elif len(dtb_list) == 2:
                        dtb_list.insert(0, "0")
                        dtb_list.insert(1, "0")
                    elif len(dtb_list) == 2:
                        dtb_list.insert(0, "0")
                        dtb_list.insert(1, "0")
                        dtb_list.insert(2, "0")
                    return dtb_list

                dtb_val = dtb_equilizer(dtb_list)

                for i in range(len(array)):
                    array_row_index_value = row_bit_adder(list(array[i]))
                    array_row_parity.append(array_row_index_value)

                def column_2_row_bit_adder(arr, arr1, f_array):
                    ln = len(arr)
                    for inc in range(ln):
                        array_index_value = arr[inc] + arr1[inc]
                        # print(array_index_value)
                        f_array.append(array_index_value)
                    return f_array

                def column_3_row_bit_adder(arr, arr1, arr2, f_array):
                    ln = len(arr)
                    for inc in range(ln):
                        array_index_value = arr[inc] + arr1[inc] + arr2[inc]
                        # print(array_index_value)
                        f_array.append(array_index_value)
                    return f_array

                def column_4_row_bit_adder(arr, arr1, arr2, arr3, f_array):
                    ln = len(arr)
                    for inc in range(ln):
                        array_index_value = arr[inc] + arr1[inc] + arr2[inc] + arr3[inc]
                        # print(array_index_value)
                        f_array.append(array_index_value)
                    return f_array

                for i in range(len(array_row_parity)):
                    array_row_index1_value = list(array_row_parity[i])
                    if i == 0:
                        int_value_of_arr_row1 = [int(i) for i in array_row_index1_value]
                    elif i == 1:
                        int_value_of_arr_row2 = [int(i) for i in array_row_index1_value]
                    elif i == 2:
                        int_value_of_arr_row3 = [int(i) for i in array_row_index1_value]
                    elif i == 3:
                        int_value_of_arr_row4 = [int(i) for i in array_row_index1_value]

                if len(data_l) == 4:
                    farray = column_4_row_bit_adder(int_value_of_arr_row1, int_value_of_arr_row2, int_value_of_arr_row3,
                                                    int_value_of_arr_row4, fifth_array)
                elif len(data_l) == 3:
                    farray = column_3_row_bit_adder(int_value_of_arr_row1, int_value_of_arr_row2, int_value_of_arr_row3,
                                                    fifth_array)
                elif len(data_l) == 2:
                    farray = column_2_row_bit_adder(int_value_of_arr_row1, int_value_of_arr_row2, fifth_array)
                elif len(int_value_of_arr_row2) == 0:
                    pass

                for i in range(len(fifth_array)):
                    if fifth_array[i] % 2 == 0:
                        parity_row_array.append(0)
                    else:
                        parity_row_array.append(1)

                for i in range(len(dtb_list)):
                    if i <= len(dtb_list):
                        en_cypher.append(dtb_list[i])

                for i in range(len(parity_row_array)):
                    if i <= len(parity_row_array):
                        en_cypher.append(parity_row_array[i])
                # adding 2nd part to final array
                for i in range(len(int_value_of_arr_row1)):
                    if i <= len(int_value_of_arr_row1):
                        en_cypher.append(int_value_of_arr_row1[i])
                # adding 3rd part to final array
                for i in range(len(int_value_of_arr_row2)):
                    if i <= len(int_value_of_arr_row2):
                        en_cypher.append(int_value_of_arr_row2[i])
                # adding 4th part to final array
                for i in range(len(int_value_of_arr_row3)):
                    if i <= len(int_value_of_arr_row3):
                        en_cypher.append(int_value_of_arr_row3[i])
                # adding 5th part to final array
                for i in range(len(int_value_of_arr_row4)):
                    if i <= len(int_value_of_arr_row4):
                        en_cypher.append(int_value_of_arr_row4[i])

                # print("Output data:")
                string_obj_data = ''.join(map(str, en_cypher))
                # print(string_obj_data)
                self.Output_text_field.setText(string_obj_data)
            else:
                self.Output_text_field.setText("Please Enter Binary Data")
            time_end = time.perf_counter()
            print(f"Encrypt time: {time_end - time_start:0.4f} seconds")
        except:
            pass

    def decrypt_btn(self):
        time_start = time.perf_counter()
        data = self.Input_text_field.text()
        self.Output_text_field.setText("")
        try:
            if data.isdigit():
                if len(data) < 13:
                    self.Output_text_field.setText("Please Enter Real Data")
                else:
                    binary_data = data[0:4]
                    data2 = data[4:len(data)]

                    def binary_to_decimal(n):
                        return int(n, 2)

                    decimal_value = binary_to_decimal(binary_data)

                    data_l = []
                    # this loop divide data into 9 bit and add those 9 bit to data_l.
                    for i in range(0, len(data2), 9):
                        d_ta = data2[i:i + 9]
                        data_l.append(d_ta)

                    parity_list_value = ""
                    if len(data_l) > 1:
                        parity_list_value = data_l.pop(0)

                    # removing data_l index values last digit.
                    fast_part_data = []
                    second_part_data = []
                    third_part_data = []
                    fourth_part_data = []
                    for i in range(len(data_l)):
                        if i == 0:
                            fpd = data_l[i]
                            fast_part_data.append(fpd)
                        elif i == 1:
                            second_part_data.append(data_l[i])
                        elif i == 2:
                            third_part_data.append(data_l[i])
                        elif i == 3:
                            fourth_part_data.append(data_l[i])

                    str_int_1st = []
                    str_int_2nd = []
                    str_int_3rd = []
                    str_int_4th = []

                    # first data list string to integer conversion.
                    for i in range(len(fast_part_data)):
                        for j in range(len(fast_part_data[i])):
                            a = fast_part_data[i][j]
                            str_int_1st.append(int(a))
                    # 2nd data list string to integer conversion.
                    for i in range(len(second_part_data)):
                        for j in range(len(second_part_data[i])):
                            a = second_part_data[i][j]
                            str_int_2nd.append(int(a))
                    # 3rd data list string to integer conversion.
                    for i in range(len(third_part_data)):
                        for j in range(len(third_part_data[i])):
                            a = third_part_data[i][j]
                            str_int_3rd.append(int(a))
                    # 4th data list string to integer conversion.
                    for i in range(len(fourth_part_data)):
                        for j in range(len(fourth_part_data[i])):
                            a = fourth_part_data[i][j]
                            str_int_4th.append(int(a))

                    for i in range(1):
                        if len(data_l) == 4:
                            str_int_1st.pop()
                            str_int_2nd.pop()
                            str_int_3rd.pop()
                            str_int_4th.pop()
                        elif len(data_l) == 3:
                            str_int_1st.pop()
                            str_int_2nd.pop()
                            str_int_3rd.pop()
                        elif len(data_l) == 2:
                            str_int_1st.pop()
                            str_int_2nd.pop()
                        elif len(data_l) == 1:
                            str_int_1st.pop()
                        elif len(data_l) == 0:
                            pass
                        else:
                            pass

                    dev = 0

                    dev = 8 - decimal_value
                    for i in range(len(data_l)):
                        if len(data_l) == 4:
                            del str_int_4th[dev:]
                        elif len(data_l) == 3:
                            del str_int_3rd[dev:]
                        elif len(data_l) == 2:
                            del str_int_2nd[dev:]
                        elif len(data_l) == 1:
                            del str_int_1st[dev:]
                        else:
                            pass

                    # now i need to add all those str data into a single list.
                    de_cypher = []
                    # first data value in to final array/list
                    for i in range(len(str_int_1st)):
                        if i <= len(str_int_1st):
                            de_cypher.append(str_int_1st[i])
                    # second data value in to final array/list
                    for i in range(len(str_int_2nd)):
                        if i <= len(str_int_2nd):
                            de_cypher.append(str_int_2nd[i])
                    # third data value in to final array/list
                    for i in range(len(str_int_3rd)):
                        if i <= len(str_int_3rd):
                            de_cypher.append(str_int_3rd[i])
                    # fourth data value in to final array/list
                    for i in range(len(str_int_4th)):
                        if i <= len(str_int_4th):
                            de_cypher.append(str_int_4th[i])

                    # print("Output data:")
                    final_output_data = ''.join(map(str, de_cypher))
                    # print(final_output_data)
                    self.Output_text_field.setText(final_output_data)
            else:
                self.Output_text_field.setText("Please Enter Binary Data")
            time_end = time.perf_counter()
            print(f"Decrypt time: {time_end - time_start:0.4f} seconds")
        except:
            pass

        # ----------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Main_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# test
# 0100111000001110011110011101011110010100100100000
# 1100111101110101110010101001
