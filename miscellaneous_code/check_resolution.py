#checking the resolution of a random image to find desired target size
root = data_dir + "/VSCS(70-90)/"

imgs = [img.name for img in Path(root).iterdir() if img.suffix == ".jpg"]
img_meta = {}
for f in imgs: img_meta[str(f)] = imagesize.get(root+f)

# Convert it to Dataframe and compute aspect ratio
img_meta_df = pd.DataFrame.from_dict([img_meta]).T.reset_index().set_axis(['FileName', 'Size'], axis = 'columns', inplace = False)
img_meta_df[["Width", "Height"]] = pd.DataFrame(img_meta_df["Size"].tolist(), index = img_meta_df.index)
img_meta_df["Aspect Ratio"] = round(img_meta_df["Width"] / img_meta_df["Height"], 2)

print(f'Total number of images in the dataset: {len(img_meta_df)}')
img_meta_df.head()

#check if any image file height is more than 350
temp_df = img_meta_df[img_meta_df['Height'] > 350]
temp_df.head()

# Visualize Image Resolutions
fig = plt.figure(figsize = (5, 5))
ax = fig.add_subplot(111)
points = ax.scatter(img_meta_df.Width, img_meta_df.Height, color = 'blue', alpha = 0.5, s = img_meta_df["Aspect Ratio"]*100, picker=True)
ax.set_title("Image Resolution")
ax.set_xlabel("Width", size = 14)
ax.set_ylabel("Height", size = 14)