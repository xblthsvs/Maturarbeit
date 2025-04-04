import librosa
import csv
import matplotlib.pyplot as plt
import mido

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

# get metadata from piece and field indeces in maestro csv table
def getPieceMetadata(piece, field):
    global maestroMetadata

    with open(maestroMetadata, newline='') as maestroMetadata:
        reader = csv.reader(maestroMetadata)
        i = 0
        for row in reader:
            if i == piece:
                metadata = row[field]
                pass
            else:
                i += 1
                continue
        return metadata


# get audio of piece from index in maestro csv
def getAudio(piece):
    global maestro
    filepath = maestro + getPieceMetadata(piece, 5)
    y, x = librosa.load(maestro + filepath)
    return y

def getMIDI(piece):
    filepath = maestro + getPieceMetadata(piece, 4)
    midi = mido.MidiFile(filepath, clip=True)
    return midi


print(len(getMIDI(1).tracks))

