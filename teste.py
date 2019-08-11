from pyembroidery import *
file_stream = "Bordado_raidan.PES.dst"
convert_file = os.path.join("convert", file_stream)

print(convert_file)

pattern = read(convert_file)
print(str(pattern.count_stitches()) + "  " + file_stream)
print(str(pattern.count_color_changes() + 1) + "  " + "Troca de linha")