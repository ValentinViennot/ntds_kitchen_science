# A Network Tour of Kitchen Science: Innovative Ingredient Replacer using Network Science
Network Tour of Data Science, Fall 2019, EPFL

## Context

Have you ever invited vegetarian / vegan friends over for diner and didn't know how to replace the meat in your favorite dish? Or you had to prepare food for dinner with your in-laws and a crucial ingredient suddently has disapeared from your kitchen? Or you wanted your significant other to taste the only recipe you know well but they are allergic to one of the ingredients? **This project is for you!**

In the context of the EPFL Network Tour of Data Science course (Fall 2019), we proposed to create a **tool to remove certain ingredients from a recipe and output the best ingredients to replace them, and suggest ingredients to add to make your recipes even tastier**.
Our data comes from the Recipe1M+ dataset -- containing over 50,000 recipes from various cooking websites, including ingredients, nutrition facts, preparation instructions, and health scores -- as well as the USDA Nutritional Info dataset.

## [Live Demo](http://kitchen-science.eu-gb.mybluemix.net/)
Quick and minimalistic demo UI to show our final results - *Provided without any warranty and subject to updates until the final project presentation date.*

## Project structure

- `data`: contains needed data to execute all notebooks independently (adjacency matrices, dataset...). *Warning: the main dataset is too big for a Github upload and needs to be downloaded separately, please refer to the 'How to get started' section.*

- `graphics`: graph visualizations saved from [GraphCommunities.ipynb](notebooks/03_GraphCommunities.ipynb) notebook, useful to zoom in and see more details than in the Jupyter interface.

- `notebooks`: all the code ordered (numerated) in a comprehensive and readable way.
  1. [CreateAdjacencyMatrices.ipynb](notebooks/01_CreateAdjacencyMatrices.ipynb): Explore the dataset, combine it with other data sources (USDA database for nutrition information), create different adjacency matrices using given data and combinations. Trying to obtain desirable properties (connected graph, sparse matrix, uniform degree distribution...)

  2. [StudyingGraphProperties.ipynb](notebooks/02_StudyingGraphProperties.ipynb): For each adjacency matrix obtained in notebook (1), study some insightful graph properties such as the number of nodes, number of edges, number of connected components, network diameter, sparsity, hub nodes/ingredients...

  3. [GraphCommunities.ipynb](notebooks/03_GraphCommunities.ipynb): Visualize and compare different graph options from previously built adjacency matrices.

  4. [GraphFiltering.ipynb](notebooks/04_GraphFiltering.ipynb): Project a recipe over the ingredient graph and do label propagation with graph filtering (smoothing).

  5. [kNNIngredientReplacement.ipynb](notebooks/05_kNNIngredientReplacement.ipynb): Find ingredient replacements from different graphs with a version of the kNN algorithm.

  6. [Veganize.ipynb](notebooks/06_Veganize.ipynb): Same as notebook (6) using a mask for vegan ingredients, achieving one of our main motivations.

  7. [CombinedIngredientReplacement.ipynb](notebooks/07_CombinedIngredientReplacement.ipynb): Combining kNN and graph filtering into an efficient ingredient replacement method using graph properties.

- `reports`: initial and final reports, explaining our work and methodology.

## How to get started

### Requirements

- `Python 3.7.5+`
- `Conda`

To run python scripts (we recommend using `venv`):
```bash
pip3 install -r requirements.txt # install dependencies if needed, using python3
```

To install/activate conda environment:
```bash
conda create --name ntds_kitchen_science --file conda_requirements.txt
jupyter-notebook
```


### Download missing dataset file

Because of github size limitations, we have uploaded the full dataset **needed for notebook (1) execution** to a public Google Drive. The file can be automatically downloaded to the right folder using the given python script [download_dataset.py]().

```python
python3 download_dataset.py
```

The [required file](https://drive.google.com/open?id=1LFu2qxOlWYR3_07LvQYe_ydS3nkinK4S) will then be downloaded to `data/recipes_with_nutritional_info_fixed_qty.json`.


### Playing with the notebooks!

> All notebooks may be executed independently. However, we recommend to follow the order (from 1 to 7) to ensure that all of the necessary files are created in the first notebooks. Notebooks are saved with their execution to save you some time and to direct visualization from github repository.

## Authors
- Maraz Zuniga, Erick Antero
- Orlandic, Lara
- Stefanini, Niccolò
- Viennot, Valentin

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
