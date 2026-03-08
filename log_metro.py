# Импорт библиотек
import pandas as pd

# Объявление переменных для чтения и записи файла.
log_file_in = "result_output" # файл с результатами работы скрипта
log_file_out = "clear_log.txt" # Файл с данными после чистики.
# data_file_in = "clear_log_new.txt"
data_file_out = "dict_all.txt"

# Настройки вывода для DataFrame.
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 300)

# Словари для хранения данных.
list_all = []
list_dict = []
keys_mx = ['name', 'type', 'temp PEM_0', 'temp PEM_1', 'temp RE_0','temp RE_1', 's_fan_1', 's_fan_2', 's_fan_3', 's_fan_4', 's_fan_5']
keys_acx_4000 = ['name', 'type', 'temp PEM_0', 'temp PEM_1', 'temp RE_0', 's_fan_1', 's_fan_2']
keys_acx_2100 = ['name', 'type', 'temp RE_0']

# Функция первоначальной очистки логов и привидение данных к дальнейшей обработки.
def clear_log():
    with open(log_file_in, "r") as f_in, open(log_file_out, "w") as f_out:
        for line in f_in:
            if "-----Outputs" in line:
                f_out.write(line)
            elif "Chassis" in  line and len(line.split()) == 3 and "|match" not in line:
                f_out.write(line.split()[2])
                f_out.write("\n")
            elif ("Temp  PEM 0") in line:
                f_out.write(line.split()[4])
                f_out.write("\n")
            elif "PEM " in line and "|match" not in line:
                f_out.write(line.split()[3])
                f_out.write("\n")
            elif "Routing Engine" in line and "CPU" not in line:
                if len(line.split()) == 10:
                    f_out.write(line.split()[3])
                    f_out.write("\n")
                else:
                    f_out.write(line.split()[4])
                    f_out.write("\n")
            elif "Fan" in line:
                f_out.write(line.split()[3])
                f_out.write("\n")

# запуск функции clear log.
clear_log()