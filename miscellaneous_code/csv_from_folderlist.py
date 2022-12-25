import glob
def get_files(directory):
  df = pd.DataFrame(columns = ['filepath', 'label'])

  d = glob.glob(directory + '/D(20-25)/*')
  dd = glob.glob(directory + '/DD(30-35)/*')
  cs = glob.glob(directory + '/CS(40-50)/*')
  scs = glob.glob(directory + '/SevereCS(55-65)/*')
  vscs = glob.glob(directory + '/VSCS(70+)/*')

  for f in d:
    df = df.append({'filepath': f, 'label': '1'}, ignore_index = True)

  for f in dd:
    df = df.append({'filepath': f, 'label': '2'}, ignore_index = True)

  for f in cs:
    df = df.append({'filepath': f, 'label': '3'}, ignore_index = True)
  
  for f in scs:
    df = df.append({'filepath': f, 'label': '4'}, ignore_index = True)

  for f in vscs:
    df = df.append({'filepath': f, 'label': '5'}, ignore_index = True)

  return df

df_train = get_files('/content/drive/MyDrive/multiclass_total')
df_train.reset_index(inplace = True, drop = True)
df_train
df_train.shape
df_train.to_csv('/content/drive/MyDrive/multiclass_total/data.csv', index = False)