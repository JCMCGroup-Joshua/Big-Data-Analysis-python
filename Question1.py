def Run():
    print("Starting Question 1 Alt")
    import pandas as pd
    import matplotlib.pyplot as plt
    from tqdm import tqdm
    # Load your dataset
    df = pd.read_csv('Question1DataAlt.csv')

    # Calculate the correlation between age range and time spent in the hospital
    corr = None
    with tqdm(total=2) as pbar:
        pbar.set_description("Calculating correlation...")
        corr = df['race'].astype('category').cat.codes.corr(
            df['time_in_hospital'])
        pbar.update()

    # Create a bar graph
    with tqdm(total=1) as pbar:
        pbar.set_description("Creating bar graph...")
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.bar(df['race'], df['time_in_hospital'], color='blue')
        ax.set_xlabel('Race')
        ax.set_ylabel('Time Spent in Hospital')
        ax.set_title(f'Correlation: {corr:.2f}')

        plt.show()
        pbar.update()


Run()
