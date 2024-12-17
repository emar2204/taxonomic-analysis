# Microbiome Data Analysis Tool

A Python script designed to analyze microbiome data by generating **summary statistics** and producing **visualizations**.

The script processes a taxonomic dataset provided in **CSV format**, representing species counts.

---

## **Output Files**
The output folder will contain the following results:
- **`frequency_table_by_phylum.csv`**: A CSV file with summary statistics for Phylum and Species.
- **`bar_chart.png`**: A bar plot of species counts per Phylum.
- **`pie_chart.png`**: A pie chart showing the distribution of species counts across Phylum.

---

## **Usage**

Run the script with the following syntax:

```bash
python microbiome_analysis.py [-h] input output
```

### **Positional Arguments**:
- **`input`**: Path to the taxonomic input CSV file.
- **`output`**: Path to the output directory.

### **Example**:
```bash
python microbiome_analysis.py input.csv output_folder/
```

---

## **Docker Container Usage**

The tool can also be executed using **Docker** to ensure that all dependencies are installed and no manual setup is needed.

### **Step 1: Build the Docker Image**
Run the following command in the project directory (ensure the Dockerfile is present):

```bash
docker build -t tax-analyzer .
```

### **Step 2: Run the Tool in a Container**
Execute the following command, replacing placeholders with your data sources:

```bash
docker run --rm -v "path_to_mount":/data tax-analyzer /data/"input.csv" /data/"output_folder"
```

### **Explanation**:
- **`path_to_mount`**: Path to the folder containing your input file.
- **`input.csv`**: Name of the taxonomic input CSV file.
- **`output_folder`**: Output directory where results will be saved (must exist in `path_to_mount`).

### **Example**:
```bash
docker run --rm -v /home/user/microbiome_data:/data tax-analyzer /data/input.csv /data/output_folder
```

---

## **Dependencies**
The script requires the following Python libraries:
- `pandas`
- `matplotlib`
- `argparse`
- Other dependencies can be installed via the Docker container.

---

## **Contributing**
Contributions are welcome! Feel free to open an issue or submit a pull request.
