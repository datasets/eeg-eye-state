from urllib.request import urlopen

with open("../data/eeg-eye-state.csv", "w") as output_file:
    data_found = False
    attributes = []
    for line in urlopen("https://www.openml.org/data/download/1587924/phplE7q6h"):
        decoded_line = line.decode('UTF-8').lower().strip()
        if data_found:
            clazz = decoded_line.split(',')[-1]
            decoded_line = decoded_line[:-1] + str(int(clazz) - 1)
            decoded_line = decoded_line.replace("?", "")
            output_file.write(decoded_line.lower() + '\n')

        if decoded_line == "@data":
            # output_file.write(','.join(attributes).lower() + '\n')
            output_file.write('AF3,F7,F3,FC5,T7,P,O1,O2,P8,T8,FC6,F4,F8,AF4,class\n')
            data_found = True

    output_file.close()
