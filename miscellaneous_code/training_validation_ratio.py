ratios = []

for i in range(len(train_counts)):
  ratio = (train_counts[i] / (train_counts[i] + val_counts[i])) * 100
  ratios.append(ratio)

for i in range(len(ratios)):
  print(f'{ratios[i]:.0f}:{100-ratios[i]:.0f}')