# tycoer han
import pandas as pd
if __name__ == '__main__':
    batch = 80
    csv = pd.read_csv('./fyx_chinamoney.csv')
    csv_np = csv.to_numpy().flatten() # shape (499, 1)

    csv_batch = [csv_np[i * batch : i * batch + batch] for i in range(len(csv_np) // batch)]
    csv_batch.append(csv_np[(len(csv_np) - len(csv_np) % batch): len(csv_np)])

    for i in range(len(csv_batch)):
        print(f'shape: {csv_batch[i].shape}')
        print(csv_batch[i])