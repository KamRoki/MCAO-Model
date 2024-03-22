import nibabel as nib
import matplotlib.pyplot as plt

# Load the Bruker image file
img_file = '/Users/kamil/MCAO-Model/data/20240305_113058_GR24_CeO2_Gd_PAA_filtracja_i_sonifikacja_1_1/9/pdata/1/2dseq'
img_data = nib.load(img_file)

# Extract image data
image_array = img_data.get_fdata()

# Display the image
plt.imshow(image_array[:, :, 0], cmap='gray')
plt.axis('off')
plt.show()