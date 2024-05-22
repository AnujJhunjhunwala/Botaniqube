# UWR_DeepLearningProject

<img src="https://github.com/berayboztepe/UWR_DeepLearningProject/assets/150927210/2d019d2f-8b69-4c5f-ae1a-a4adce8f3949" alt="BotaniQube" width="512" height="512">

## Bigger project outline

The final target is to create a house plant incubator - a cube that would detect which plant was put in, what diseases it has, and introduce a protocol for its treatment. It will have multiple sensors (temperature, humidity, light, etc.) as well as a way of influencing those factors.

## Project: Deep Learning

Regarding the scope of our university "Project: Deep Learning" it would be creating software for this tool. This is setting up the server that the cube would be connected to, programming the Arduino/Raspberry Pi within the cube (if the hardware will be ready by the end of our project), and training the classification algorithms. Regarding the AI:

- training plant classification model based on camera input
- training plant diseases classification model based on camera input

We already found good datasets so the problem should be solvable. Exact information about data sources will be provided later.

## Tech stack

Repo - GitHub

Server - Weights and Biases

Model Architectures - fine-tuning VGG16 / VGG19

## Datasets

Plant classification:
- https://plantnet.org/open-data/

Disease classification:
- https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset/data
- https://paperswithcode.com/dataset/plantdoc
- https://universe.roboflow.com/learning-eri4b/plant-disease-tmyq8
- https://www.kaggle.com/datasets/sadmansakibmahi/plant-disease-expert
- https://www.kaggle.com/datasets/sadmansakibmahi/plant-disease-expert
- https://ieeexplore.ieee.org/document/10086516
- https://github.com/pratikkayal/PlantDoc-Dataset


## Team Members

1. Antoni Czapski - 317214
2. Anuj Jhunjhunwala - 348612
3. Emre Beray Boztepe - 350227
4. Valery Tarasenko - 348715

# KEDRO README

## Overview

This is your new Kedro project with Kedro-Viz and PySpark setup, which was generated using `kedro 0.19.3`.

Take a look at the [Kedro documentation](https://docs.kedro.org) to get started.

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://docs.kedro.org/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `requirements.txt` for `pip` installation.

To install them, run:

```
pip install -r requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the files `src/tests/test_run.py` and `src/tests/pipelines/test_data_science.py` for instructions on how to write your tests. Run the tests as follows:

```
pytest
```

To configure the coverage threshold, look at the `.coveragerc` file.

## Project dependencies

To see and update the dependency requirements for your project use `requirements.txt`. Install the project requirements with `pip install -r requirements.txt`.

[Further information about project dependencies](https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `catalog`, `context`, `pipelines` and `session`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can use tools like [`nbstripout`](https://github.com/kynan/nbstripout). For example, you can add a hook in `.git/config` with `nbstripout --install`. This will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://docs.kedro.org/en/stable/tutorial/package_a_project.html)



