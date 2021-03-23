def Log(file, text):
    log = open(file, 'a+')##open a file
    log.write(text)##write the text
    log.close()##close the file
