import sys

sys.path.insert(0, "../")

from scripts import alesp_parser, alesp_tamitacao_parser

if __name__ == "__main__":
    deputados = alesp_parser.parse_deputados(True)