import name_handler
import srt
import srt_document
import writer

import argparse
import math
import os

def main():
    parser = argparse.ArgumentParser(
        prog= "SRT Converter for GOETHE",
        description= "Converts docx to srt",
        epilog= "No support info provided, yet.")

    parser.add_argument("source_dir")
    parser.add_argument("destination_dir")
    parser.add_argument("-n", "--names")
    parser.add_argument("-l", "--language")
    args = parser.parse_args()

    src = args.source_dir
    dst = args.destination_dir

    if src[-1] != "/":
        src = src + "/"
    if dst[-1] != "/":
        dst = dst + "/"

    if not os.path.exists(src):
        print("{} is not a valid path".format(src))

    if not os.path.exists(dst):
        print("{} is not a valid path".format(dst))

    if not os.path.exists(src) or not os.path.exists(dst):
        exit()

    if args.names != None:
        name_handler.initialize ( args.names )

    dir = os.listdir(args.source_dir)

    docx_files = [file for file in dir if file.split(".")[-1].lower() == "docx"]
    printed_digits_count = int (math.log(len (docx_files), 10)) + 1

    for i in range (0, len (docx_files)):
        print ("[{:0>{length}}/{}] {}".format (i + 1, len (docx_files), src + docx_files[i], length=printed_digits_count))
        srt_doc = srt_document.SRT_Document(src + docx_files[i])
        srt_val = srt.SRT(srt_doc)
        output = srt_val.format()

        file_name = dst + name_handler.change_name(docx_files[i][:-5])

        if args.language != None:
            file_name = file_name + "-" + args.language + ".srt"
        else:
            file_name = file_name + ".srt"
        writer.Writer.save_output(file_name, output)
        

if __name__ == "__main__":
    main()
