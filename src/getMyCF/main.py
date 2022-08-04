from getmycf.runner import Extractor
import argparse

def print_intro():
    print("#########################################")
    print("#                                       #")
    print("#         FISCAL CODE GENERATOR         #")
    print("#                                       #")
    print("#########################################\n")

def main():
    print_intro()

    parser = argparse.ArgumentParser(description="Get your Italian Fiscal Code")
    parser.add_argument("-i", "--input", type=str, required=False, help="Pass an input file with data")

    args = parser.parse_args()

    ex = Extractor()

    if args.input:
        ex.parse_data_txt(args.input)
    else:
        ex.parse_data()
    CF = ex.run()

    print("Il tuo codice fiscale è: {}".format(CF))

if __name__ == '__main__':

    main()

    