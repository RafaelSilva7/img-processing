from PIL import Image

def labeling(img_input):
    """Labeling objects in the image

    Args:
        img_input: Image to be labeled.

    Return:
        Labeled image and number of objects in labeled
    """

    labels = []
    pixel_dict = {}
    (width, height) = img_input.size

    for j in range(height):
        for i in range(width):
            p = (i,j)
            p_r = (i-1,j)
            p_s = (i,j-1)

            if img_input.getpixel(p) == 255:
                pass
            else:
                # without s and r: create new label
                if i == 0 and j == 0: 
                    pixel_dict[p] = len(labels)
                    labels.append(len(labels))
                # without s
                elif j == 0 and i > 0:
                    # create new label
                    if img_input.getpixel(p_r) != 0:
                        pixel_dict[p] = len(labels)
                        labels.append(len(labels))
                    # P <- r
                    else:
                        pixel_dict[p] = pixel_dict[p_r]
                # without r
                elif i == 0 and j > 0:
                    if img_input.getpixel(p_s) != 0:
                        pixel_dict[p] = len(labels)
                        labels.append(len(labels))
                    # P <- s
                    else:
                        pixel_dict[p] = pixel_dict[p_s]
                # with r and s
                else:
                    r = img_input.getpixel(p_r)
                    s = img_input.getpixel(p_s)
                    # create new label
                    if r != 0 and s != 0:
                        pixel_dict[p] = len(labels)
                        labels.append(len(labels))
                    # set correspondent label
                    elif r == 0 and s != 0:
                        # P <- r
                        pixel_dict[p] = pixel_dict[p_r]         
                    elif r != 0 and s == 0:
                        # P <- s
                        pixel_dict[p] = pixel_dict[p_s]
                    # equivalent label
                    elif labels[pixel_dict[p_r]] == labels[pixel_dict[p_s]]:
                        pixel_dict[p] = pixel_dict[p_s]
                    else:
                        # r <- index of s less then r
                        if pixel_dict[p_r] > pixel_dict[p_s]:
                            pixel_dict[p] = pixel_dict[p_s] # set label of s
                            labels[pixel_dict[p_r]] = labels[pixel_dict[p_s]]
                        # s <- index of r less then s
                        else:
                            pixel_dict[p] = pixel_dict[p_r] # set label of r
                            labels[pixel_dict[p_s]] = labels[pixel_dict[p_r]]

    img_output = Image.new('RGB', (width, height), (255,255,255))
    #img_output = Image.new('L', (width, height), 255)
    num_labels = len(set(labels))
    s_labels = set(labels)
    c = int(255/num_labels) # color contant
    for (pixel, color) in pixel_dict.items():
        i = 0
        for x in s_labels:
            if x == labels[color]:
                break
            else:
                i += 1
        img_output.putpixel(pixel, (i*c,0,(6*i)+c))
        #img_output.putpixel(pixel, i*c)

    return (img_output, num_labels)