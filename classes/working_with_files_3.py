def merge_files(file_names, output_file):
    file_contents = []
    for file_name in file_names:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.readlines()
            file_contents.append((file_name, len(content), content))
    file_contents.sort(key=lambda x: x[1])
    with open(output_file, "w", encoding="utf-8") as file:
        for file_name, count, content in file_contents:
            file.write(f"\n{file_name}\n{count}\n")
            file.writelines(content)


file_names = ["1.txt", "2.txt", "3.txt"]
output_file = "4.txt"
merge_files(file_names, output_file)
