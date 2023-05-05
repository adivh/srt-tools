import zipfile
import xml.etree.ElementTree

class SRT_Document:

    def __init__(self, path):
        self.items = []
        self._load(path)

    def print(self):
        for n in range(0, len(self.items)):
            print("{}: {}".format(n + 1, self.items[n]))
        
    def __str__(self):
        return self.items.__str__()

    def __len__(self):
        return len(self.items)

    def _load(self, path):
        file_type = path.split(".")[-1].lower()

        if file_type == "docx":
            WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
            PARA = WORD_NAMESPACE + 'p'
            TEXT = WORD_NAMESPACE + 't'
            TABLE = WORD_NAMESPACE + 'tbl'
            ROW = WORD_NAMESPACE + 'tr'
            CELL = WORD_NAMESPACE + 'tc'

            with zipfile.ZipFile(path) as docx:
                tree = xml.etree.ElementTree.XML(docx.read('word/document.xml'))

            for table in tree.iter(TABLE):
                for row in table.iter(ROW):
                    for cell in row.iter(CELL):
                        self.items.append(''.join(node.text for node in cell.iter(TEXT)))
        else:
            raise ValueError("File type {} not yet supported\r\nUse\r\n\r\n\tlowriter --convert-to docx documentname.doc\r\n\r\nto convert.".format(file_type))


if __name__ == "__main__":
    print('ran srt_document.py')
