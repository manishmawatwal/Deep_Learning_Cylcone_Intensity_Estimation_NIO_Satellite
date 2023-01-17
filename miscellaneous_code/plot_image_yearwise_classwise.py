import os
import glob

years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011']
classes = ['CS', 'D', 'DD', 'SevereCS', 'VSCS']
yearly_count = {year: {cls: 0 for cls in classes} for year in years}

for year in years:
    print('\n')
    for cls in classes:
        path = f'/content/drive/MyDrive/Multiclass_Yearwise/data/{year}/{cls}/*.jpg'
        image_count = len(glob.glob(path))
        yearly_count[year][cls] = image_count
        print(f'{year}/{cls}: {image_count}')

fig, axs = plt.subplots(len(years), 1, figsize=(15, 5*len(years)))
for i, year in enumerate(years):
    axs[i].barh(list(yearly_count[year].keys()), yearly_count[year].values())
    axs[i].set_title(year)
plt.show()

fig, axs = plt.subplots(len(classes), 1, figsize=(15, 5*len(classes)))
for i, cls in enumerate(classes):
    data = [yearly_count[year][cls] for year in years]
    axs[i].plot(years, data)
    axs[i].set_title(cls)
plt.show()

fig, ax = plt.subplots(figsize=(15,5))
colors = ['b', 'g', 'r', 'c', 'm']
for i, cls in enumerate(classes):
    data = [yearly_count[year][cls] for year in years]
    ax.plot(years, data, color=colors[i], label=cls, alpha = 0.5)
    ax.set_xlabel("Years")
    ax.set_ylabel("Number of Images")
    ax.legend()
plt.show()