def Run():
    print("Starting Question 2")
    import pandas as pd
    import matplotlib.pyplot as plt
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

    # Create a scatter line chart with subplots
    with tqdm(total=1) as pbar:
        pbar.set_description("Creating scatter line chart with subplots...")
        fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(12, 12))
        admission_types = sorted(df['admission_source_id'].unique())

        for i, admission_type in enumerate(admission_types):
            ax = axs[i // 2, i % 2]
            ax.set_title(f'Admission Type: {admission_type}')
            data = df[df['admission_source_id'] == admission_type]
            ax.plot(data['time_in_hospital'],
                    data['admission_source_id'], '-o', color='blue')
            ax.set_xlabel('Time Spent in Hospital')
            ax.set_ylabel('Referal Sauce')

        fig.suptitle(f'Correlation: {corr:.2f}')
        plt.tight_layout()

        plt.show()
        pbar.update()


Run()
