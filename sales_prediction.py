def sales_prediction():
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import ColumnTransformer

    # Load and preprocess the data
    sales_data = pd.read_csv('sales_data.csv')
    sales_data['Date'] = pd.to_datetime(sales_data['Date'])

    # Extract features from 'Date'
    sales_data['Year'] = sales_data['Date'].dt.year
    sales_data['Month'] = sales_data['Date'].dt.month
    sales_data['Day'] = sales_data['Date'].dt.day

    # Drop 'Date' column
    sales_data = sales_data.drop('Date', axis=1)

    # Define X (features) and y (target)
    X = sales_data.drop('Total_Revenue', axis=1)
    y = sales_data['Total_Revenue']

    # Handle categorical variables
    categorical_columns = ['Store_Location', 'Austrian_City', 'Customer_Name', 'Solar_Panel_Model', 'Solution_Type']
    numeric_columns = ['Year', 'Month', 'Day', 'Quantity']
    preprocessor = ColumnTransformer(transformers=[
        ('num', 'passthrough', numeric_columns),
        ('cat', OneHotEncoder(drop='first'), categorical_columns)])
    X = preprocessor.fit_transform(X)

    # Perform train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Calculate the performance of the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Create a DataFrame for the next 12 weeks
    future_dates = pd.date_range(start='2023-08-01', periods=12, freq='W')

    X_future = pd.DataFrame({
        'Date': future_dates,
        'Store_Location': sales_data['Store_Location'].mode()[0], 
        'Austrian_City': sales_data['Austrian_City'].mode()[0], 
        'Customer_Name': sales_data['Customer_Name'].mode()[0], 
        'Solar_Panel_Model': sales_data['Solar_Panel_Model'].mode()[0], 
        'Solution_Type': sales_data['Solution_Type'].mode()[0], 
        'Quantity': [int(sales_data['Quantity'].mean())] * 12
    })

    # Preprocess the future dataset
    X_future['Year'] = X_future['Date'].dt.year
    X_future['Month'] = X_future['Date'].dt.month
    X_future['Day'] = X_future['Date'].dt.day
    X_future = X_future.drop('Date', axis=1)

    # Transform the future dataset using the same preprocessor
    X_future_encoded = preprocessor.transform(X_future)

    # Predict on the future dataset
    y_future = model.predict(X_future_encoded)

    # Create a DataFrame for future predictions
    future_predictions = pd.DataFrame({
        'Week Starting': future_dates,
        'Predicted Revenue': np.round(y_future),
        'Predicted Quantity Sold': X_future['Quantity']
    })
    
    return {'mse': mse, 'r2': r2, 'future_predictions': future_predictions}
