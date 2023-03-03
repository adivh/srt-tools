import re

class SRT:

    def __init__(self, srt_document):
        self.times = []
        self.speakers = []
        self.original_texts = []
        self.translated_texts = []
        self.column_count = 0

        _times_found = 0
        for i in range(0, int(len(srt_document))):

            if self._convert_time(srt_document.items[i], test_only=True):
                _times_found = _times_found + 1

            if _times_found > 1:
                break

            self.column_count = self.column_count + 1
            

        print(self.column_count)
        
        if len(srt_document) % self.column_count != 0:
            raise Exception("Document has no valid structure: ({})".format(self.column_count))

        for i in range(0, int(len(srt_document) / self.column_count)):
            index = i * self.column_count
            self.times.append(self._convert_time(srt_document.items[index]))
            self.speakers.append(srt_document.items[index + 1])
            self.original_texts.append(srt_document.items[index + 2])
            self.translated_texts.append(srt_document.items[index + self.column_count - 1])

    def _convert_time(self, time, test_only=False):
        reg = re.compile("[0-9]{2}[:][0-9]{2}[:][0-9]{2}[:][0-9]*")
        values = time.split(" ")

        if len(values) < 2:
            if test_only:
                return False
            raise ValueError(time)

        res = reg.fullmatch(values[0])
        if res is None:
            if test_only:
                return False
            raise ValueError(time)

        res = reg.fullmatch(values[1])
        if res is None:
            if test_only:
                return False
            raise ValueError(time)

        if test_only:
            return True
        
        return "{},{:0<3} --> {},{:0<3}".format(values[0][:8], values[0][9:], values[1][:8], values[1][9:])

    def __str__(self):
        res = ""
        for i in range(0, len(self.times)):
            res = res + "\n\r" + str(i + 1) + "\n\r" + self.times[i] + "\n\r" + self.speakers[i] + "\n\r" + self.original_texts[i] + "\n\r" + self.translated_texts[i] + "\n\r"
        return res

    def format(self, index=True, time=True, speaker=False, original_text=False, translated_text=True):
        # if nothing is True
        if not index and not time and not speaker and not original_text and not translated_text:
            return ""
        
        res = ""
        for i in range(0, len(self.times)):
            res = res + "\n\r"
            if index:
                res = res + str(i + 1) + "\n\r"

            if time:
                res = res + self.times[i] + "\n\r"

            if speaker:
                res = res + self.speakers[i] + "\n\r"

            if original_text:
                res = res + self.original_texts[i] + "\n\r"

            if translated_text:
                res = res + self.translated_texts[i] + "\n\r"

        return res
