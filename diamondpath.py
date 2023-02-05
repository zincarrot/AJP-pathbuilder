from ajppathbuilder import ajpPathBuilder as apb

SQRT3=3**0.5

def inclined_path1(size):
    path=None
    return path

def inclined_path2(size):
    path=None
    return path

def vertical_path(size):
    path=None
    return path

def diamond_path(dest, len_h, len_v, size_h, size_v):
    """
    Parameters:
        len_h: horizontal (projection) length of the inclined pillars, in mm
        len_v: length of the vertical pillars (), in ratio to len_h
        size_h: repeat times of the tetragonal structure in x direction
        size_v: number of layers of tetragonal structures

    Output:
        
    """

    sqrt3len=SQRT3*len_h

    if size_v>size_h:
        raise ValueError(f"size_v ({size_v}) must not be larger than size_h ({size_h})")

    newpath=apb()
    newpath.build_header()
    for i in range(size_v):
        for j in range(size_h-i):
            for k in range (size_h-i-j):
                shift_x=sqrt3len*k+sqrt3len/2+j+sqrt3len/2*i
                shift_y=3/2*j+len_h+i/2*len_h
                endx=sqrt3len/2+shift_x
                endy=len_h/2+shift_y
                newpath.addpath((shift_x,shift_y),(endx,endy))
                newpath.addpath((shift_x+sqrt3len,shift_y),(endx,endy))
                newpath.addpath((shift_x+sqrt3len/2,shift_y+3*len_h/2),(endx,endy))
                newpath.addpath((endx,endy),(endx,endy))
    newpath.buildfile(dest)
    
if __name__=="__main__":

    diamond_path("./diamondtest.prg",1,1,3,2)