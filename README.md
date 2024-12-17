# taxonomic-analysis
A Python script designed to analyze microbiome data by generating summary statistics and producing plots.
The script analyze a taxonomic dataset provided in CSV format, representing species counts.
    The output folder will contain:
    - CSV file with a summary statistics for Phylum and Species called "frequency_table_by_phylum.csv";
    - A barplot for Species counts in Phylum called "bar_chart.png"
    - A pie chart for distribution of Species counts in Phylum called "pie_chart.png"

Usage:
microbiome_analysis.py [-h] input output
positional arguments:
  input       Path to the taxonomic input CSV file.
  output      Path to the output directory.

Docker Container Usage:
The tool can be used with Docker, ensuring that all dependences are respected, avoiding manual installation.
Step 1: build docker image running the following command on your terminal in the project directory (ensure to see Dockerfile)
    docker build -t tax-analyzer .
Step 2: Run the tool in a contained
    docker run --rm -v "path_to_mount":/data tax-analyzer /data/"input.csv" /data/"output_folder"
All text in quotation marks must be changed with your data sources, where:
    - "path_to_mount" is the folder with your input data
    - "input.csv" is the input file with taxonomic data
    - "output_folder" is the output folder where results are saved, must be in "path_to_mount"