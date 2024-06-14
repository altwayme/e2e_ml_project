### I. Data Source Information and Data Statistics

##### Data Source:

The data used for the model in this repository is from Yandex.Realty, specifically for real estate listings for apartments in St. Petersburg and Leningrad Oblast. The data spans from 2016 to mid-August 2018.

- Total number of entries before data cleaning: `198257`
- Columns: `offer_id`, `first_day_exposition`, `last_day_exposition`, `last_price`, `floor`, `open_plan`, `rooms`, `studio`, `area`, `kitchen_area`, `living_area`, `agent_fee`, `renovation`, `offer_type`, `category_type`, `unified_address`, `building_id`

##### Median and Mean Rent Prices Calculation:

- Median Rent Price: 25,000 RUB
- Mean Rent Price: 33,390.56 RUB

##### Outlier Detection and Removal:

Detected and removed outliers from rent data where prices were unrealistic.
Example: Removed rent prices over 1 million RUB as they were considered user input errors.

##### Correlation Matrix of Features

![Picture](/pictures/correlation_heatmap.png)

### II. Information about Model, Choosen Framework, Hyperparameters

##### Model Information

This project involves predicting real estate prices in St. Petersburg using historical data from Yandex.Realty. The goal is to develop a machine learning model to accurately predict apartment prices, helping to identify fraud and assist users in making informed real estate decisions.

##### Chosen Framework

- **Framework**: `Scikit-learn`
- **Language**: `Python`

##### Data Preprocessing

- The dataset was cleaned and encoded.
- Irrelevant columns were dropped.
- The dataset was split into training and validation sets using a simple random split.
- Features were scaled using `StandardScaler` from Scikit-learn.

##### Model

- **Model Used**: Decision Tree Regressor
- **Reason**: The simplicity of the model and the limited number of features make the Decision Tree a suitable choice for this problem.

##### Hyperparameters

- **Max Depth**: 6
- **Random State**: 17

##### Evaluation Metrics

- **Mean Absolute Error (MAE)**: 0.34
- **Mean Squared Error (MSE)**: 0.40
- **Root Mean Squared Error (RMSE)**: 0.63
  
##### Saving the Model

The trained model and the scalers for the features and target variable were saved using `joblib` for future use in predictions.


### III. How to run the App with Virtual Environment

1. To run the app with the virtual environment you should first setup virtual environment and activate it by executions of these commands: 

```
python3 -m venv env
source venv/bin/activate
```

2. After that all the necessary libraries can be installed with this command:

```
pip install -r requirements.txt
```

3. After successful installation of libraries the application can be started:

```
python3 app.py
```

### IV. Information about Dockerfile and Description of it’s Content

Dockerfile stores all the necessary information for docker image.

Comments:

```
FROM ubuntu:22.04 (Base image for docker)
MAINTAINER Nikita Pronin (This is me, the author)
RUN apt-get update -y (Updates the package list to ensure the latest versions of packages are available and accepts all the choices)
COPY . /opt/gsom_project (Current directory is copied to this location)
WORKDIR /opt/gsom_project (This location is set as working directory)
RUN apt install -y python3-pip (Python and pip are installed)
RUN pip3 install -r requirements.txt (All the required libraries are installed for the )
CMD python3 app.py (Docker will run the only process with price predicitons for rent)
```

### V. How to open the Port in remote VM

Port 5444 is used by default. 

If it is closed and web-service is not availiable, then port can be opened in remote VM with the command.

```
ufw allow 5444
```

Port can be changed in app.py in the last lines of code.

```
if __name__ == '__main__':
    app.run(debug=True, **port=5444**, host='0.0.0.0')
```

### V. How to run the App using Docker

1. Docker imaged can be pulled with this command:

```
docker push altwayme/gsom_project:tagname
```

* Tagname should indicate the latest verions (e.g. "v.0.4").

---

2. After that application can be started with this command:

```
sudo docker run --network host -d altwayme/gsom_project:v.0.4
```
