import librosa
import csv

maestro = "/Volumes/Seb Vun Stjärne +41-(0)782036569 2/maestro-v3.0.0/"
maestroMetadata = maestro + "maestro-v3.0.0.csv"


def getAudio(index):
    global maestroMetadata
    with open(maestroMetadata, newline='') as maestroMetadata:
        reader = csv.reader(maestroMetadata)
        i = 0
        for row in reader:
            if i == index:
                filepath = row[5]
                pass
            else:
                i += 1
                continue
        #filepath = reader[index][5]
        y, x = librosa.load(maestro + filepath)
        return y


librosa.display.waveshow(getAudio(1))

