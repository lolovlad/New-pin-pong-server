import argparse
import router as rout

parser = argparse.ArgumentParser(description="Server Game")
parser.add_argument("ip", type=str)
parser.add_argument("port", type=str)

