import pandas as pd
from progressbar import progressbar
import os
from PIL import Image


def generate_single_image(filepaths, output_filename=None):
    # for item in filepaths:
    #     if "sunglasses" in item:
    #         print(filepaths)
    #         for item2 in filepaths:
    #             if "bandana" in item2:
    #                 filepaths = filepaths.remove(item2)
    #                 print(filepaths)

    # Treat the first layer as the background
    bg = Image.open(os.path.join("assets", filepaths[0]))

    # Loop through layers 1 to n and stack them on top of another
    for filepath in filepaths[1:]:
        if filepath.endswith(".png"):
            img = Image.open(os.path.join("assets", filepath))
            bg.paste(img, (0, 0), img)

    # Save the final image into desired location
    if output_filename is not None:
        bg.save(output_filename)
    else:
        # If output filename is not specified, use timestamp to name the image and save it in output/single_images
        if not os.path.exists(os.path.join("output", "single_images")):
            os.makedirs(os.path.join("output", "single_images"))
        bg.save(os.path.join("output", "single_images", str(int(time.time())) + ".png"))
    # rarity_table = pd.DataFrame(rarity_table).drop_duplicates()


def main():
    count = 999
    data = pd.read_excel("/home/strix/xtz/pyscripts/nft/1000.xlsx")
    op_path = os.path.join("output", "edition_" + str("afk"), "images")
    zfill_count = len(str(count - 1))

    # print(data)

    # for n in progressbar(range(count)):

    for i in range(count):
        image_name = str(i).zfill(zfill_count) + ".png"
        trait_paths = []

        row = data.loc[[i]]
        # print(row)
        # print(row["Mouth"][i])
        if row["Backgrounds "][i] is not None:
            bg = "Backgrounds/" + row["Backgrounds "][i].strip() + ".png"
            trait_paths.append(bg)

        if row["Skin "][i] is not None:
            skn = "Elephants Skin/" + row["Skin "][i].strip() + ".png"
            trait_paths.append(skn)

        if row["Clothing"][i] is not None:
            cloth = "Clothing/" + row["Clothing"][i].strip() + ".png"
            trait_paths.append(cloth)

        if row["Eyes"][i] is not None:
            eye = "Eyes/" + row["Eyes"][i].strip() + ".png"
            trait_paths.append(eye)

        if row["Eyewear"][i] is not None:
            eyewr = "Eyewear/" + row["Eyewear"][i].strip() + ".png"
            trait_paths.append(eyewr)

        if row["Head"][i] is not None:
            hd = "Head/" + row["Head"][i].strip() + ".png"
            trait_paths.append(hd)

        if row["Tusks"][i] is not None:
            tsk = "Tusks/" + row["Tusks"][i].strip() + ".png"
            trait_paths.append(tsk)

        if row["Mouth"][i] is not None:
            mth = "Mouth/" + row["Mouth"][i].strip() + ".png"
            trait_paths.append(mth)

        print(trait_paths)
        generate_single_image(trait_paths, os.path.join(op_path, image_name))
        trait_paths = []

        rarity_table = pd.DataFrame(data)
        rarity_table.to_csv(
            os.path.join("output", "edition_" + str("afk"), "metadata.csv")
        )


main()
