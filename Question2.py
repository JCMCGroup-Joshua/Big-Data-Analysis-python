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

    # Create a stacked bar chart
    with tqdm(total=1) as pbar:
        pbar.set_description("Creating stacked bar chart...")
        data = pd.pivot_table(df, values='time_in_hospital', index='admission_source_id',
                              columns='referral_source', aggfunc='mean')
        fig, ax = plt.subplots(figsize=(10, 6))
        data.plot(kind='bar', stacked=True, ax=ax)

        ax.set_xlabel('Admission Source ID')
        ax.set_ylabel('Time Spent in Hospital')
        ax.set_title(f'Correlation: {corr:.2f}')

        plt.show()
        pbar.update()


Run()
