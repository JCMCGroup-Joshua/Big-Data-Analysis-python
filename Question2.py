def Run():
    print("Starting Question 2")
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from tqdm import tqdm
    # Load your dataset
    df = pd.read_csv('Question2Data.csv')

    # Calculate the correlation between age range and time spent in the hospital
    corr = None
    with tqdm(total=2) as pbar:
        pbar.set_description("Calculating correlation...")
        corr = df['admission_source_id'].astype('category').cat.codes.corr(
            df['time_in_hospital'])
        pbar.update()

    # Create a heatmap
    with tqdm(total=1) as pbar:
        pbar.set_description("Creating heatmap...")
        data = pd.pivot_table(df, values='time_in_hospital', index='admission_source_id',
                              aggfunc=np.mean)
        fig, ax = plt.subplots(figsize=(10, 6))
        im = ax.imshow(data, cmap='viridis')

        # Create colorbar
        cbar = ax.figure.colorbar(im, ax=ax)
        cbar.ax.set_ylabel("Time Spent in Hospital", rotation=-90, va="bottom")

        # Set tick labels and title
        ax.set_xticklabels(data.columns)
        ax.set_yticklabels(data.index)
        ax.set_xlabel('Referal Sauce')
        ax.set_ylabel('Admission Source ID')
        ax.set_title(f'Correlation: {corr:.2f}')

        plt.show()
        pbar.update()


Run()
