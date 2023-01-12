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
parser.add_argument('-d', '--image_dir', type=str, help='Directory with calibration images. Default = current directory.')
parser.add_argument('-s','--size', type=float, help='Size of the chessboard/charuco squares in cm. Min = 5cm')
parser.add_argument('--vertical', type=int, help='Number of squares in height on the chessboard/charuco. Min = 5')
parser.add_argument('--horizontal', type=int, help='Number of squares in width on the chessboard/charuco. Min = 5')
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

args = parser.parse_args()

print("Camera Calibration Tool\n")

# * Read command line arguments
if args.image_dir is not None:
    image_dir = args.image_dir
else:
    image_dir = os.getcwd()
    
if args.size is not None:
    if args.size < 5:
        print_red("Square size must be greater than 5cm")
        exit()
    square_size = args.size * 10 # in mm
else:
    square_size = 100            # in mm

if args.vertical is None and args.horizontal is None:
    marker_no = (5, 5)
    
elif args.vertical is None or args.horizontal is None:
    print_red("Vertical and horizontal number must be specified together")
    marker_no = (5, 5)
else:
    if args.vertical < 5 or args.horizontal < 5:
        print_red("Vertical/Horizontal number must be greater than 5")
        exit()
    marker_no = (args.horizontal, args.vertical)

# * Create calibration settings
if args.marker_dict is not None:
    calibration_settings = calibration.CharucoCalibrationSettings(square_size, marker_no, calibration.get_charuco_marker_dict(args.marker_dict))
else:
    calibration_settings = calibration.ChessboardCalibrationSettings(square_size, marker_no)

# * Create calibration parameters
calibration_parameters = calibration.CalibrationParameters()

# * Create & Start GUI
gui = gui.GUI(calibration_settings=calibration_settings, calibration_parameters=calibration_parameters, image_dir=image_dir)