# montage.py - Jim Lawless
# create montage images of like-sized sub-images (like comic book covers)
# https://github.com/jimlawless/montage
# MIT license
#
import argparse
from PIL import Image
from os import listdir
import random

def montage(listfile,rows,cols,xmax,ymax,imgfile,bgcolor):
    images=[]
    width = 0
    height = ymax*rows+((rows+2)*2)
    width=xmax*cols+((cols+2)*2)
    if bgcolor == "white":
        bg=(255,255,255)
    else:
        bg=(0,0,0)
    img = Image.new("RGB", (width, height), bg)

    with open(listfile, "r") as file:
        filenames = file.readlines()
        for fname in filenames:
            fname=fname.strip()
            print(fname)
            tmp_img=Image.open(fname)
            tmp_img = tmp_img.resize((xmax,ymax))
            images.append(tmp_img)
    pos=3
    y=3
    count=0
    for tmp_img in images:
        img.paste(tmp_img,(pos,y))
        count=count+1
        if count == cols:
            count = 0
            y=y + ymax +2
            pos=3
        else:
            pos+=xmax+2

    img.save(imgfile)

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.description="Generate a montage image from separate images"
    parser.add_argument("-listfile",required=True,help="text file with list of images")
    parser.add_argument("-rows",required=True,type=int,help="number of vertical image rows")
    parser.add_argument("-cols",required=True,type=int,help="number of horizontal image columns")
    parser.add_argument("-xmax",required=True,type=int,help="max individual img width in pixels")
    parser.add_argument("-ymax",required=True,type=int,help="max individual img height in pixels")
    parser.add_argument("-imgfile",required=True,help="name of output image file")
    parser.add_argument("-bgcolor",required=False,help="specify black or white for the background color")
    args=parser.parse_args()
    bg="black"
    if args.bgcolor:
        bg=args.bgcolor.lower()
    montage(args.listfile,args.rows,args.cols,args.xmax,args.ymax,args.imgfile,bg)    
