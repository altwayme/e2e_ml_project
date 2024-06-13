### Information about source data and some statistics (maybe plots, tables, images)



### Information about Mdel, Choosen Framework, Hyperparameters

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


### How to run the App with Virtual Environment

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

### Information about Dockerfile and Description of it’s Content

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

### How to open the Port in remote VM

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

### How to run the App using Docker

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
