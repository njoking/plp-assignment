from ucimlrepo import fetch_ucirepo 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# fetch dataset 
iris = fetch_ucirepo(id=53) 

# combine features and target into one DataFrame
df = pd.concat([iris.data.features, iris.data.targets], axis=1)
df.columns = df.columns.str.replace(' ', '_')  # replaces spaces with underscores


  
# data (as pandas dataframes) 
X = iris.data.features
y = iris.data.targets

# Convert the features (X) to a DataFrame and add the target column (y)
df = pd.concat([X, y], axis=1)

df['species'] = y  # Add the target species column

# metadata
print(iris.metadata) 
  
# variable information 
print(iris.variables) 

def preview_dataset(df):
    print("📌 First 5 rows of the dataset:")
    print(df.head(), "\n")

def dataset_info(df):
    print("🔍 Dataset Info:")
    print(df.info(), "\n")

def check_missing_values(df):
    print("🧹 Missing values in each column:")
    print(df.isnull().sum(), "\n")

def basic_statistics(df):
    print("📊 Basic statistics:")
    print(df.describe(), "\n")  # No need to drop 'species' column anymore

def analyze_species(df):
    avg_petal_length = df.groupby("species")["petal_length"].mean()
    print("📈 Average petal length per species:")
    print(avg_petal_length, "\n")

    print("💡 Observation:")
    shortest_species = avg_petal_length.idxmin()
    print(f"{shortest_species.capitalize()} species has significantly shorter petals than the others.\n")


def create_visualizations(df):
    print("📊 Generating visualizations...")

    # Histogram of Sepal Length
    plt.figure(figsize=(6, 4))
    sns.histplot(df['sepal_length'], kde=True, color='skyblue')
    plt.title("Distribution of Sepal Length")
    plt.xlabel("Sepal Length")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # Boxplot of Petal Width by Species
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='species', y='petal_width', data=df)
    plt.title("Petal Width by Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Width")
    plt.tight_layout()
    plt.show()

    # Bar plot of average petal length per species
    plt.figure(figsize=(6, 4))
    sns.barplot(x="species", y="petal_length", data=df, estimator="mean", errorbar=None)  # ci=None deprecated
    plt.title("Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Average Petal Length")
    plt.tight_layout()
    plt.show()

def main():
    # Combine features and targets
    df = pd.concat([X, y], axis=1)
    df['species'] = y  # Add target variable to the dataframe

    # Clean column names AFTER full DataFrame is formed
    df.columns = df.columns.str.replace(' ', '_')

    preview_dataset(df)
    dataset_info(df)
    check_missing_values(df)
    basic_statistics(df)
    analyze_species(df)
    create_visualizations(df)


if __name__ == "__main__":
    main()
