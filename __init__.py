import gui
import calibration
import argparse
import glob
import cv2 as cv
import os


def print_red(string):
    print(f"\033[91m{string}\033[0m")
def print_blue(string):
    print(f"\033[44m{string}\033[0m")

# * Parse command line arguments

parser = argparse.ArgumentParser(description='Camera Calibration Tool.')
parser.add_argument('-d', '--image_dir', type=str, help='Directory with calibration images.')
parser.add_argument('-s','--size', type=float, help='Size of the chessboard/charuco squares in meters.')
parser.add_argument('--vertical', type=int, help='Number of squares in height on the chessboard/charuco.')
parser.add_argument('--horizontal', type=int, help='Number of squares in width on the chessboard/charuco.')
parser.add_argument('-m','--marker_dict', type=int, help="""Index of charuco marker dict. 
                    | 01: DICT_4X4_50
                    | 02: DICT_4X4_100
                    | 03: DICT_4X4_250
                    | 04: DICT_4X4_1000
                    | 05: DICT_5X5_50
                    | 06: DICT_5X5_100
                    | 07: DICT_5X5_250
                    | 08: DICT_5X5_1000
                    | 09: DICT_6X6_50
                    | 10: DICT_6X6_100
                    | 11: DICT_6X6_250
                    | 12: DICT_6X6_1000
                    | 13: DICT_7X7_50
                    | 14: DICT_7X7_100
                    | 15: DICT_7X7_250
                    | 16: DICT_7X7_1000""")

try:
    args = parser.parse_args()
except:
    print_red("Error parsing arguments. Please check your input.")
    exit()


# * Read command line arguments
if args.image_dir is not None:
    image_dir = args.image_dir
else:
    image_dir = os.getcwd()
    
if args.size is not None:
    square_size = args.size
else:
    square_size = 10            # in cm

if args.vertical is not None and args.horizontal is not None:
    marker_no = (args.horizontal, args.vertical)
else:
    marker_no = (7, 5)

# * Create calibration settings
if args.marker_dict is not None:
    calibration_settings = calibration.CharucoCalibrationSettings(square_size, marker_no, calibration.get_charuco_marker_dict(args.marker_dict))
else:
    calibration_settings = calibration.ChessboardCalibrationSettings(square_size, marker_no)

# * Create calibration parameters
calibration_parameters = calibration.CalibrationParameters()

# * Create & Start GUI
gui = gui.GUI(calibration_settings=calibration_settings, calibration_parameters=calibration_parameters, image_dir=image_dir)