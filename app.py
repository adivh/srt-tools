import srt
import srt_document
import writer

import argparse
import os

def main():
    parser = argparse.ArgumentParser(
        prog= "SRT Converter for GOETHE",
        description= "Converts docx to srt",
        epilog= "No support info provided, yet.")

    parser.add_argument("source_dir")
    parser.add_argument("destination_dir")
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

    dir = os.listdir(args.source_dir)
    for file in dir:
        f = file.split(".")
        if len(f) == 2:
            if f[1].lower() == "docx":
                srt_doc = srt_document.SRT_Document(src + file)
                srt_val = srt.SRT(srt_doc)
                writer.Writer.save_output(dst + f[0] + ".srt", srt_val.format())
        

if __name__ == "__main__":
    main()
