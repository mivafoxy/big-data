import csv
import pandas as pd

def main():
    data_red = pd.read_csv('database.csv', sep=',')

    data_red.head()

    colsToDrop = ['UNIQUE KEY', 'BOROUGH', 'ZIP CODE', 'LATITUDE', 'LONGITUDE', 'ON STREET NAME', 'CROSS STREET NAME',
                  'OFF STREET NAME']
    new_data_red = data_red.drop(colsToDrop, axis=1)
    new_data_red.to_csv('restructured.csv', encoding='utf-8', index=False)
    # data_cor = data_red['DATE','TIME','LOCATION', 'PERSONS INJURED','PERSONS KILLED','PEDESTRIANS INJURED','PEDESTRIANS KILLED','CYCLISTS INJURED','CYCLISTS KILLED','MOTORISTS INJURED','MOTORISTS KILLED','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE','VEHICLE 1 FACTOR','VEHICLE 2 FACTOR','VEHICLE 3 FACTOR','VEHICLE 4 FACTOR','VEHICLE 5 FACTOR']

    # data_cor.corr()


if __name__ == '__main__':
    main()
