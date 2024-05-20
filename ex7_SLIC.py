import matplotlib.pyplot as plt

from skimage import data
from skimage import color
from skimage import morphology
from skimage import segmentation

# Input data
img = data.rocket()

# SLIC result
slic = segmentation.slic(img, n_segments=200, start_label=1)

# Display result
fig, ax_arr = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(15, 5))
ax1, ax2 = ax_arr.ravel()

ax1.imshow(img)
ax1.set_title('Original image')

ax2.imshow(segmentation.mark_boundaries(img, slic))
ax2.set_title('SLIC')


for ax in ax_arr.ravel():
    ax.set_axis_off()

plt.tight_layout()
plt.show()