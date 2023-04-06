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

    # Create a scatter plot
    with tqdm(total=1) as pbar:
        pbar.set_description("Creating scatter plot...")
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.scatter(df['admission_source_id'],
                   df['time_in_hospital'], color='blue')
        ax.set_xlabel('Referal Sauce')
        ax.set_ylabel('Time Spent in Hospital')
        ax.set_title(f'Correlation: {corr:.2f}')

        plt.show()
        pbar.update()


Run()
