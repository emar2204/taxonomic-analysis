import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import os

def main(input_file, output_path):
    # Load the CSV file into a DataFrame
    data = pd.read_csv(input_file)
    #Select a taxonomic target and define count column
    column_to_group = 'phylum'
    count_column='count'
    # Find columns ignoring case sensitivity
    data.columns = data.columns.str.lower()
    matched_column_taxa = [col for col in data.columns if col == column_to_group.lower()]
    matched_column_count = [col for col in data.columns if col == count_column.lower()]

    #Check existence of the specified taxonomy, here "phylum"
    if not matched_column_taxa:
        print(f"\nERROR:\nColumn '{column_to_group}' not found.\nControl your input data file ({input_file}).\n")
        raise SystemExit    
    #Check existence of a count column, here "count"
    if not matched_column_count:
        print(f"\nERROR:\nColumn '{count_column}' not found.\nControl your input data file ({input_file}).\n")
        raise SystemExit    
    #Check if there are NA values and then removes rows from DF.
    if data[count_column].isna().any():
        print(f"\nWARNING:\nSome missing values detected in '{count_column}'. Rows with missing values were removed.\n")
        data = data.dropna(subset=[count_column]) 
    #Reassignment of data types to secure next control has updated data after removal of NA
    data = data.convert_dtypes()
    #Check if count column has only integer, here "count"
    if not pd.api.types.is_integer_dtype(data[count_column]):
        print(f"\nERROR:\nThe '{count_column}' column must contain only integers. Please, verify your input file ({input_file}).\n")
        raise ValueError

    # Group by choosed column and produce summary statistics 
    frequency_table = (
        data.groupby(column_to_group)
        .agg(
            TotalSpeciesCountPerPhylum=(count_column, 'sum'), #Total counts for species in each phylum
            MeanSpeciesCountPerPhylum=(count_column, 'mean'), #Average counts for species within each phylum
        )
        .reset_index()
        .sort_values(by="TotalSpeciesCountPerPhylum", ascending=False)
    )
    # Rename the columns for clarity
    frequency_table.rename(columns={count_column: "Total_Count"}, inplace=True)

    ## Since the input file contains unique species, the interpretation of point "Average species count per species within each phylum."
    ## can be challengins, as the results will mirror the input file. Nevertheless, I have written the code to compute the mean of a
    ## within each phylum and export the results to a CSV file.
    ##
    #species_average_per_phylum = data.groupby(['phylum', 'species'], as_index=False)[count_column].mean()
    #print(species_average_per_phylum)
    #output_file = os.path.join(output_path, f"species_average_for_each_phylum.csv")
    #species_average_per_phylum.to_csv(output_file, index=False)
    ##
    ##

    # Display the frequency table
    print(f"Frequency Table by {column_to_group}:\n")
    print(frequency_table)

    # Save the frequency table to a new CSV file
    output_file = os.path.join(output_path, f"frequency_table_by_{column_to_group}.csv")
    frequency_table.to_csv(output_file, index=False)
    print(f"\nFrequency table saved to {output_file}")


    colors = sns.color_palette("pastel", len(frequency_table))  # dynamically set colors for group

    # Bar chart showing the total species count for each phylum
    plt.figure(figsize=(8, 6))
    plt.bar(frequency_table[column_to_group], frequency_table["TotalSpeciesCountPerPhylum"], color=colors)
    plt.title("Total Species count for each Phylum", fontsize=16)
    plt.xlabel("Phylum", fontsize=14)
    plt.ylabel("Count", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "bar_chart.png"))
    print(f"Bar chart saved to {os.path.join(output_path, 'bar_chart.png')}")


    # 
    # Additional: for better visualization
    # Pie chart for a clear distribution of species count for each phylum within a sample
    #
    plt.figure(figsize=(8, 8))
    plt.pie(
        frequency_table["TotalSpeciesCountPerPhylum"],
        labels=frequency_table[column_to_group],
        autopct='%1.1f%%',
        startangle=90,
        colors=colors
    )
    plt.title("Proportion of Species for each Phylum", fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "pie_chart.png"))
    print(f"Pie chart saved to {os.path.join(output_path, 'pie_chart.png')}")

if __name__ == "__main__":
    #Guidelines for tool usage and arguments parsing
    parser = argparse.ArgumentParser(description="""Analyze a taxonomic dataset provided by a CSV file, representing species counts; 
                                     outputs include a summary CSV file ("frequency_table_by_phylum.csv"), a barplot ("bar_chart.png") for 
                                     species counts by phylum, and a pie chart ("pie_chart.png") for species count distribution.""")
    parser.add_argument("input", help="Path to the taxonomic input CSV file.")
    parser.add_argument("output", help="Path to the output directory.")
    args = parser.parse_args()
    # Run the main analysis function
    main(args.input, args.output)    
