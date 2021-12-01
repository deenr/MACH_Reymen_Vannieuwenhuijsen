# used for manipulating directory paths
import csv

# Scientific and vector computation for python

# Plotting library

# Optimization module in scipy


# Press the green button in the gutter to run the script.
from datetime import datetime

if __name__ == '__main__':
    data_header = []

    # load in the different holidays
    holidays = []
    file1 = open('holiday.txt', 'r')
    for line in file1.readlines():
        holiday = line.replace(" ", "_").lower()[:-1]
        data_header.append(holiday)
        holidays.append(holiday)

    data_header.append('temp')
    data_header.append('rain_1h')
    data_header.append('snow_1h')
    data_header.append('clouds_all')

    # load in the different weather descriptions
    # weather_descriptions = []
    file1 = open('weather_description.txt', 'r')
    for line in file1.readlines():
        weather_description = line.replace(" ", "_").lower()[:-1]
        data_header.append(weather_description)
        # weather_descriptions.append(weather_description)

    data_header.append('weekday')

    # load in the different weather descriptions
    # weather_descriptions = []
    file1 = open('weather.txt', 'r')
    for line in file1.readlines():
        weather_description = line.lower()[:-1]
        data_header.append(weather_description + "_and_weekday")
        # weather_descriptions.append(weather_description)

    data_header.append('working_hours')
    data_header.append('year')
    data_header.append('month')
    data_header.append('hour')
    data_header.append('traffic_volume')

    # print(data_header)

    # open the file in the write mode
    f = open('metro_traffic_data.csv', 'w')
    # clear file
    f.truncate()
    # create the csv writer
    writer = csv.writer(f, lineterminator='\n')

    # write header
    writer.writerow(data_header)

    with open('Metro_Interstate_Traffic_Volume.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        index = 0
        for row in csv_reader:
            new_row = []
            if index > 0:
                # holiday
                holiday = row[0]
                if holiday == "Columbus Day":
                    new_row.extend([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                elif holiday == "Veterans Day":
                    new_row.extend([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                elif holiday == "Thanksgiving Day":
                    new_row.extend([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
                elif holiday == "Christmas Day":
                    new_row.extend([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
                elif holiday == "New Years Day":
                    new_row.extend([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
                elif holiday == "Washingtons Birthday":
                    new_row.extend([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
                elif holiday == "Memorial Day":
                    new_row.extend([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
                elif holiday == "Independence Day":
                    new_row.extend([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
                elif holiday == "State Fair":
                    new_row.extend([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
                elif holiday == "Labor Day":
                    new_row.extend([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
                elif holiday == "Martin Luther King Jr Day":
                    new_row.extend([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
                else:
                    new_row.extend([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

                # temp
                new_row.append(row[1])

                # rain_1h
                new_row.append(row[2])

                # snow_1h
                new_row.append(row[3])

                # clouds_all
                new_row.append(row[4])

                # weather_description
                weather_description = row[6]
                if weather_description == "scattered clouds":
                    new_row.extend(
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "broken clouds":
                    new_row.extend(
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "overcast clouds":
                    new_row.extend(
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "sky is clear":
                    new_row.extend(
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "few clouds":
                    new_row.extend(
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "light rain":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "light intensity drizzle":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "mist":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "haze":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "fog":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "proximity shower rain":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "drizzle":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "moderate rain":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "heavy intensity rain":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "proximity thunderstorm":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "thunderstorm with light rain":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "proximity thunderstorm with rain":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "heavy snow":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "heavy intensity drizzle":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "snow":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "thunderstorm with heavy rain":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "freezing rain":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "shower snow":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "light rain and snow":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "light intensity shower rain":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "SQUALLS":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "thunderstorm with rain":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "proximity thunderstorm with drizzle":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "thunderstorm":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "very heavy rain":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "thunderstorm with light drizzle":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
                         0, 0, 0, 0, 0])
                elif weather_description == "light snow":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                         0, 0, 0, 0, 0])
                elif weather_description == "thunderstorm with drizzle":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         1, 0, 0, 0, 0])
                elif weather_description == "smoke":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 1, 0, 0, 0])
                elif weather_description == "shower drizzle":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 1, 0, 0])
                elif weather_description == "light shower snow":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 1, 0])
                elif weather_description == "sleet":
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 1, 0])
                else:
                    new_row.extend(
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0])

                # date-time
                date_time = datetime.strptime(row[7], '%Y-%m-%d %H:%M:%S')

                #   weekday
                weekday = 0
                if 0 <= date_time.weekday() <= 4:
                    new_row.append('1')
                    weekday = 1
                else:
                    new_row.append('0')

                #   weather_main_and_weekday
                weather_main = row[5]
                if weather_main == "Clouds":
                    new_row.extend([weekday, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                elif weather_main == "Clear":
                    new_row.extend([0, weekday, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                elif weather_main == "Rain":
                    new_row.extend([0, 0, weekday, 0, 0, 0, 0, 0, 0, 0, 0])
                elif weather_main == "Drizzle":
                    new_row.extend([0, 0, 0, weekday, 0, 0, 0, 0, 0, 0, 0])
                elif weather_main == "Mist":
                    new_row.extend([0, 0, 0, 0, weekday, 0, 0, 0, 0, 0, 0])
                elif weather_main == "Haze":
                    new_row.extend([0, 0, 0, 0, 0, weekday, 0, 0, 0, 0, 0])
                elif weather_main == "Fog":
                    new_row.extend([0, 0, 0, 0, 0, 0, weekday, 0, 0, 0, 0])
                elif weather_main == "Thunderstorm":
                    new_row.extend([0, 0, 0, 0, 0, 0, 0, weekday, 0, 0, 0])
                elif weather_main == "Snow":
                    new_row.extend([0, 0, 0, 0, 0, 0, 0, 0, weekday, 0, 0])
                elif weather_main == "Squall":
                    new_row.extend([0, 0, 0, 0, 0, 0, 0, 0, 0, weekday, 0])
                elif weather_main == "Smoke":
                    new_row.extend([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, weekday])
                else:
                    new_row.extend([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

                #   working_hours
                if 9 <= date_time.hour <= 17:
                    new_row.append('1')
                else:
                    new_row.append('0')

                #   year
                new_row.append(date_time.year)
                #   month
                new_row.append(date_time.month)
                #   hour
                new_row.append(date_time.hour)

                # traffic_volume
                new_row.append(row[8])

                # write new row
                writer.writerow(new_row)

            index = index + 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
