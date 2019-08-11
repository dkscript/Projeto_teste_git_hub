from pyembroidery import *

for file_stream in os.listdir("convert"):
    print(file_stream)
    convert_file = os.path.join("convert", file_stream)
    new_path="/home/flavio/PycharmProjects/Projeto_teste_git_hub/convert/"+file_stream
    print(convert_file)
    pattern = read(convert_file)
    print( str(pattern.count_stitches()) + "  " + file_stream)
    print(str(pattern.count_color_changes() + 1) + "  " + "Troca de linha")
    write_png(pattern,new_path + "." + "png")

