Examples
========

I added nine images that are each 244 pixels wide by 370 pixels high.  The input list of image files is covers.txt ( these are meant to represent magazine covers of the same size. )  The 3_by_3 batch file invokes the montage.py script with the following parameters:

    montage.py -listfile covers.txt -rows 3 -cols 3 -xmax 150 -ymax 225 -imgfile g.jpg -bgcolor black

The example width (xmax) and height (ymax) 150/225 are **about** in the same ratio as 244/370 (the original size of the image.) The images shouldn't look distorted in the montage.

The above invocation will only yield an output image ( g.jpg ) with six of the nine provided images.
