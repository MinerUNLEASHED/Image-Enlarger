from PIL import Image, ImageEnhance

# Image.MAX_IMAGE_PIXELS = 10000000000000000000

#'../CreatePT/WhatsApp Image 2023-03-16 at 12.04.06 PM.jpeg'
file_path_for_image = input('File Path: ')
image_to_enhance = Image.open(file_path_for_image)
unenhanced_pixels = open('unenhanced_pixels.txt', 'w')


def right_location(x, y):
    if x == 0 and y == 0:
        return x, y
    elif x == 0:
        return x, y*3
    elif y == 0:
        return x*3, y
    else:
        return x*3, y*3


for x in range(width_unenhanced_image := image_to_enhance.width):
    for y in range(height_unenhanced_image := image_to_enhance.height):
        input_pixel = image_to_enhance.getpixel((x, y))
        unenhanced_pixels.write(str((x, y)+input_pixel)+'   ')
    unenhanced_pixels.write('\n')

Image.new('RGB', (width_unenhanced_image*3, height_unenhanced_image*3), color=(255,255,255)).save('enhanced_image.png')
enhanced_image = Image.open('enhanced_image.png')


unenhanced_pixels.close()
unenhanced_pixels = open('unenhanced_pixels.txt', 'r')


pixels_location_list = unenhanced_pixels.read().strip('\n').split('   ')
for location, pixel_element in enumerate(pixels_location_list):
    if len(pixel_element) == 0:
        pixels_location_list.remove(pixel_element)
    else:
        pixels_location_list[location] = eval(pixel_element)


enhanced_image_pixel_map = enhanced_image.load()

ct_of_how_far = 0
def one_to_three():
    global ct_of_how_far
    for x in range(width_unenhanced_image):
        for y in range(height_unenhanced_image):
            x_to_put, y_to_put = right_location(x, y)
            return_pix = pixels_location_list[ct_of_how_far][-3] + pixels_location_list[ct_of_how_far][-2] + pixels_location_list[ct_of_how_far][-1]
            enhanced_image_pixel_map[x_to_put, y_to_put] = (int(pixels_location_list[ct_of_how_far][-3]), int(pixels_location_list[ct_of_how_far][-2]), int(pixels_location_list[ct_of_how_far][-1]))
            enhanced_image_pixel_map[x_to_put+1, y_to_put] = (int(pixels_location_list[ct_of_how_far][-3]), int(pixels_location_list[ct_of_how_far][-2]), int(pixels_location_list[ct_of_how_far][-1]))
            enhanced_image_pixel_map[x_to_put, y_to_put+1] = (int(pixels_location_list[ct_of_how_far][-3]), int(pixels_location_list[ct_of_how_far][-2]), int(pixels_location_list[ct_of_how_far][-1]))
            enhanced_image_pixel_map[x_to_put+2, y_to_put] = (int(pixels_location_list[ct_of_how_far][-3]), int(pixels_location_list[ct_of_how_far][-2]), int(pixels_location_list[ct_of_how_far][-1]))
            enhanced_image_pixel_map[x_to_put+2, y_to_put+1] = (int(pixels_location_list[ct_of_how_far][-3]), int(pixels_location_list[ct_of_how_far][-2]), int(pixels_location_list[ct_of_how_far][-1]))
            enhanced_image_pixel_map[x_to_put, y_to_put+2] = (int(pixels_location_list[ct_of_how_far][-3]), int(pixels_location_list[ct_of_how_far][-2]), int(pixels_location_list[ct_of_how_far][-1]))
            enhanced_image_pixel_map[x_to_put+1, y_to_put+2] = (int(pixels_location_list[ct_of_how_far][-3]), int(pixels_location_list[ct_of_how_far][-2]), int(pixels_location_list[ct_of_how_far][-1]))
            enhanced_image_pixel_map[x_to_put+2, y_to_put+2] = (int(pixels_location_list[ct_of_how_far][-3]), int(pixels_location_list[ct_of_how_far][-2]), int(pixels_location_list[ct_of_how_far][-1]))
            enhanced_image_pixel_map[x_to_put+1, y_to_put+1] = (int(pixels_location_list[ct_of_how_far][-3]), int(pixels_location_list[ct_of_how_far][-2]), int(pixels_location_list[ct_of_how_far][-1]))

            ct_of_how_far += 1
one_to_three()

enhanced_image.save('enhanced_image_real', format='png')

real_enhanced_image = Image.open('enhanced_image_real')
real_enhanced_image_pixel_map = real_enhanced_image.load()

blend_val = 47
def pixel_manipulator():
    for x in range(real_enhanced_image.width):
        for y in range(real_enhanced_image.height):
            current_pixel_value = real_enhanced_image.getpixel((x, y))
            current_code = ''
            current_r = current_pixel_value[0]
            current_g = current_pixel_value[1]
            current_b = current_pixel_value[2]
            howmany_r = 1
            howmany_g = 1
            howmany_b = 1
            try:
                pixel_ahead_value = real_enhanced_image.getpixel((x+1, y))
            except:
                pass
            try:
                pixel_behind_value = real_enhanced_image.getpixel((x-1, y))
            except:
                pass
            try:
                pixel_ontop_value = real_enhanced_image.getpixel((x, y+1))
            except:
                pass
            try:
                pixel_under_value = real_enhanced_image.getpixel((x, y-1))
            except:
                pass
            try:
                current_code += 'ahead'
                if abs(pixel_ahead_value[0] - current_pixel_value[0]) >= blend_val:
                    current_code += 'r'
                    current_r += pixel_ahead_value[0]
                    howmany_r += 1
                if abs(pixel_ahead_value[1] - current_pixel_value[1]) >= blend_val:
                    current_code += 'g'
                    current_g += pixel_ahead_value[1]
                    howmany_g += 1
                if abs(pixel_ahead_value[2] - current_pixel_value[2]) >= blend_val:
                    current_code += 'b'
                    current_b += pixel_ahead_value[2]
                    howmany_b += 1
                current_code += '   '
            except:
                current_code += '   '
            try:
                current_code += 'behind'
                if abs(pixel_behind_value[0] - current_pixel_value[0]) >= blend_val:
                    current_code += 'r'
                    current_r += pixel_behind_value[0]
                    howmany_r += 1
                if abs(pixel_behind_value[1] - current_pixel_value[1]) >= blend_val:
                    current_code += 'g'
                    current_g += pixel_behind_value[1]
                    howmany_g += 1
                if abs(pixel_behind_value[2] - current_pixel_value[2]) >= blend_val:
                    current_code += 'b'
                    current_b += pixel_behind_value[2]
                    howmany_b += 1
                current_code += '   '
            except:
                current_code += '   '
            try:
                current_code += 'ontop'
                if abs(pixel_ontop_value[0] - current_pixel_value[0]) >= blend_val:
                    current_code += 'r'
                    current_r += pixel_ontop_value[0]
                    howmany_r += 1
                if abs(pixel_ontop_value[1] - current_pixel_value[1]) >= blend_val:
                    current_code += 'g'
                    current_g += pixel_ontop_value[1]
                    howmany_g += 1
                if abs(pixel_ontop_value[2] - current_pixel_value[2]) >= blend_val:
                    current_code += 'b'
                    current_b += pixel_ontop_value[2]
                    howmany_b += 1
                current_code += '   '
            except:
                current_code += '   '
            try:
                current_code += 'under'
                if abs(pixel_under_value[0] - current_pixel_value[0]) >= blend_val:
                    current_code += 'r'
                    current_r += pixel_under_value[0]
                    howmany_r += 1
                if abs(pixel_under_value[1] - current_pixel_value[1]) >= blend_val:
                    current_code += 'g'
                    current_g += pixel_under_value[1]
                    howmany_g += 1
                if abs(pixel_under_value[2] - current_pixel_value[2]) >= blend_val:
                    current_code += 'b'
                    current_b += pixel_under_value[2]
                    howmany_b += 1
                current_code += '   '
            except:
                current_code += '   '
            real_enhanced_image_pixel_map[x, y] = (int(current_r/howmany_r), int(current_g/howmany_g), int(current_b/howmany_b))
            # print(x, y, int(current_r/howmany_r), int(current_g/howmany_g), int(current_b/howmany_b))


pixel_manipulator()

real_enhanced_image.save('REAL_enhanced_image', format='png')

actual_enhanced_image = Image.open('REAL_enhanced_image')
actual_enhanced_image.show()



