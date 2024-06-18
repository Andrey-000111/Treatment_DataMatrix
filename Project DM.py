import os
import csv


def process_files(input_folder, output_folder):
    folder_path = os.path.join(os.path.expanduser('../input_folder'))
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    """Создаем новую папку для сохранения файлов без первого сивола"""
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    """Открываем отчет для записи"""
    report_file=open(os.path.join(output_folder,'report.txt'),'w')

    """Перебираем все файлы во входной папке"""
    for file_name in os.listdir(input_folder):
        if file_name.endswith(('.txt', '.xlsm', '.csv')):
            file_path = os.path.join(input_folder, file_name)

            """Открываем файл и обрабатываем его"""
            with open(file_path, 'r') as file:
                lines = file.readlines()
                processed_lines = 0
                lines_with_fist_symbol_removed = []


                for i, line in enumerate(lines):
                    """Удаляем первый символ, если он есть"""
                    if line[0] == '':
                        line = line[1:]
                    #if line and lines[0].isspace():
                        processed_lines += 1
                        lines_with_fist_symbol_removed.append(i)
                        lines[i] = line[i]
                #return lines


                """Сохраняем обработанный файл в новой папке"""
                output_file_path = os.path.join(output_folder, f'{os.path.splitext(file_name)[0]}_processed.txt')
                with open(output_file_path, 'w') as output_file:
                    output_file.writelines(lines)


                """Записываем отчет"""
                report_file.write(f'File: {file_name}\n')
                report_file.write(f'Lines processed: {processed_lines}\n')
                report_file.write(f'Lines with first symbol removed: ({' ,'.join(map(str, lines_with_fist_symbol_removed))}\n')
                report_file.write('Characters count per line: \n')
                for i, line in enumerate(lines, 1):
                    report_file.write(f'Line {i}: {len(line)}\n')
                report_file.write('\n')


    report_file.close()


"""Путь к входной и выходной папке"""
input_folder = os.path.join(os.path.expanduser('../input_folder'))
out_folder = 'out_folder_path'


process_files(input_folder, out_folder)



