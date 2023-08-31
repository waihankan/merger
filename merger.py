from pypdf import PdfWriter
import argparse
import re
import os


def main():
    parser = argparse.ArgumentParser(description="description")
    parser.add_argument("-o", "--output", required=True, help="specify output file")
    parser.add_argument("input_files", nargs="*", help="input pdf files")
    args = parser.parse_args()

    process_pdfs(args.output, args.input_files)


def process_pdfs(output_file, files):
    if len(files) == 1:
        print("\033[91mInput is only one file: two or more files are expected.\033[91m")
        quit()

    if os.path.exists(output_file):
        print("\033[93mOutput file name is already occupied.\033[0m")
        quit()

    merger = PdfWriter()
    for file in files:
        assert validate_file_extension(file), "Only Pdf files are allowed"
        merger.append(os.path.abspath(file))

    merger.write(output_file)
    print(f"\033[92mThe merged file:\033[0m '{output_file}'" + "\033[92m is ready.\033[0m")
    merger.close()

def validate_file_extension(file):
    pattern = r".\.pdf$"
    return re.search(pattern, file)


if __name__ == "__main__":
    main()

