class Writer:
    
    def save_output(path, output):
        with open(path, "w", encoding="utf-8") as file:
            file.write(output)