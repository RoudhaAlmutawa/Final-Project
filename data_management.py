import pickle    # Importing the pickle module for serialization

# Define the DataManager class for saving and loading data
class DataManager:
    def save_data(filename, data):
        with open(filename, 'wb') as file:    # Open file in binary write mode
            pickle.dump(data, file)     # Serialize and write data to the file

    def load_data(filename):
        try:
            with open(filename, 'rb') as file:  # Open file in binary read mode
                return pickle.load(file)    # Deserialize and return data from the file
        except FileNotFoundError:
            return []     # Return an empty list if the file is not found