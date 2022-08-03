from runner import Extractor

def print_intro():
    print("#########################################")
    print("#                                       #")
    print("#            CF GENERATOR               #")
    print("#                                       #")
    print("#########################################")


if __name__ == '__main__':

    print_intro()
    ex = Extractor()
    CF = ex.run()

    print("\nIl tuo codice fiscale è: {}".format(CF))