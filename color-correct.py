from plantcv import plantcv as pcv
import cv2
import matplotlib.pyplot as plt
class options:
    def __init__(self):
        self.debug = "plot"
        self.writeimg= False
        self.result = "color_tutorial_results.json"
        self.outdir = "."
        
# Get options
args = options()

# Set debug to the global parameter 
pcv.params.debug = args.debug

# Read in source and target images 

# Inputs:
#   filename - Image file to be read in 
#   mode - Return mode of image; either 'native' (default), 'rgb', 'gray', or 'csv' 
target_img, t_path, t_filename = pcv.readimage(filename="./img/target_image.png")
source_img, s_path, s_filename = pcv.readimage(filename="./img/source_image.png")

# Create a labeled color card mask, first use color card finder function 

# This won't print anything out but you can look at the dataframe output 
# to see the chips that the function found. 

# Inputs:
#   rgb_img - RGB image data containing color card 
#   threshold - Optional threshold method; either 'adaptgauss' (default), 'normal', or 'otsu'
#   threshvalue - Optional threhsolding value (default threshvalue = 125) 
#   blurry - Optional boolean; False (default) or if True then image sharpening is applied 
#   background - Optional type of image background; 'dark' (default) or 'light'
dataframe1, start, space = pcv.transform.find_color_card(rgb_img=target_img, background='dark')

# Make the labeled mask of the target image 

# Inputs: 
#   rgb_img - RGB image data containing color card 
#   radius - Radius of color card chips (masks make circles on chips)
#   start_coord - Two-element tuple of the first chip mask, (starting x, starting y) 
#   spacing - Two-element tuple of the horizontal and vertical spacing between chip masks
#   nrows - Number of chip rows
#   ncols - Number of chip columns 
#   exclude - Optional list of chips to exclude. List largest to smallest index 
target_mask = pcv.transform.create_color_card_mask(target_img, radius=15, start_coord=start, 
                                                   spacing=space, nrows=6, ncols=4)

# Our color card chip appears to be in relatively the same position in both the source and target images 
# Try using the same parameters and check to make sure it's appropriate for the source image

source_mask = pcv.transform.create_color_card_mask(source_img, radius=10, start_coord=start, 
                                                   spacing=space, nrows=6, ncols=4)

# Run color correction 

# Inputs:
#   target_img - RGB image with color chips
#   target_mask - Grayscale image with color chips and background each represented with unique values 
#   source_img - RGB image with color chips 
#   source_mask - Grayscale image with color chips and background each represented with unique values 
#   output_directory - File path to which the target_matrix, source_matrix, and tranformation_matrix will be saved
tm, sm, transformation_matrix, corrected_img = pcv.transform.correct_color(target_img=target_img, 
                                                                           target_mask=target_mask, 
                                                                           source_img=source_img, 
                                                                           source_mask=source_mask, 
                                                                           output_directory=args.outdir)

cv2.imwrite('Color-corrected-test-sample-image.png', corrected_img)
plt.imshow(corrected_img)
plt.title('Color-corrected-test-sample-image')
plt.show()