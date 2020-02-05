import sys


class MissionImpossible:

    def find_orbit_vehical(self, weather, orbit1_speed, orbit2_speed):
        # orbit parameters
        orbits = [{'name': 'ORBIT1', 'distance': 18, 'no_of_craters': 20},
                  {'name': 'ORBIT2', 'distance': 20, 'no_of_craters': 10}]

        # vehical parameters
        vehicles = [{'name': 'BIKE', 'speed': 10, 'time_to_travel_crater': 2, 'weather': ['SUNNY', 'WINDY']},
                    {'name': 'TUKTUK', 'speed': 12, 'time_to_travel_crater': 1, 'weather': ['SUNNY', 'RAINY']},
                    {'name': 'CAR', 'speed': 20, 'time_to_travel_crater': 3,
                     'weather': ['SUNNY', 'RAINY', 'WINDY']}]

        # weather parmeters
        weather_impact = {'SUNNY': 0.9, 'RAINY': 1.2, 'WINDY': 1}

        # vehicles allows to use as per weather condition
        eligible_vehicles = [vehicle for vehicle in vehicles for weh in vehicle['weather'] if weh == weather]

        # As weather is not useful anymore so removing it from dictionary
        for vehicle in eligible_vehicles:
            vehicle.pop('weather')

        for orbit in orbits:
            # Adding new value of craters according to weather condition
            orbit['no_of_craters'] = orbit['no_of_craters'] * weather_impact[weather]
            # Adding orbit limit speed to orbit list
            if orbit['name'] == 'ORBIT1':
                orbit['speed_limit'] = orbit1_speed
            if orbit['name'] == 'ORBIT2':
                orbit['speed_limit'] = orbit2_speed

        final_output = []
        for vehicle in eligible_vehicles:
            for orbit in orbits:
                # Restricting vehicle speed to orbit speed limit if its greater than orbit speed
                if vehicle['speed'] >= orbit['speed_limit']:
                    speed = orbit['speed_limit']
                else:
                    speed = vehicle['speed']

                mode_of_transport = {}
                # Time required to travel over craters
                time_to_overcome_craters = vehicle['time_to_travel_crater'] * orbit['no_of_craters']
                # Time required to travel orbit distance
                time_to_travel_orbit = 60 * orbit['distance'] / speed
                # Total time
                total_time = time_to_travel_orbit + time_to_overcome_craters

                mode_of_transport['name'] = vehicle['name']
                mode_of_transport['orbit_name'] = orbit['name']
                mode_of_transport['time'] = total_time

                final_output.append(mode_of_transport)

        # Sorting the list of dictionary according to time
        sorted_list = sorted(final_output, key=lambda i: i['time'])

        print(sorted_list[0]['name'], sorted_list[0]['orbit_name'])


if __name__ == '__main__':
    file_content = open(sys.argv[1], "r+").readline().split(" ")

    weather = file_content[0]
    orbit1_speed_limit = file_content[1]
    orbit2_speed_limit = file_content[2]

    o = MissionImpossible()
    o.find_orbit_vehical(weather, int(orbit1_speed_limit), int(orbit2_speed_limit))
