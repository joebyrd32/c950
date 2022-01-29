from model.Package import Package


class Truck:

    def __init__(self, packages, time, last_route, stop_time, name):
        self.packages = packages
        self.time = time
        self.location_id = 0
        self.total_distance = 0
        self.last_route = last_route
        self.stop_time = stop_time
        self.name = name

    # O(n^2)
    # This is used to deliver the packages.
    # It uses the nearest neighbor algorithm.
    # It does this by checking the distance to all packages that are
    # loaded in the truck and traveling to the closest one.
    # It does this until all packages are delivered and then travels
    # back to the hub if the current route is not the last route.
    # It will also stop at a certain time if it cannot deliver the last package
    def deliver_packages(self, distances):
        # Checks to see if current time is after stop time
        if self.time >= self.stop_time:
            return self.total_distance

        # Changes statues of all packages
        self.load_packages()
        last_package = None

        # Main loop for NN
        while len(self.packages) > 0:
            closest_package_id = None
            closest_package_distance = 100
            closest_package = None

            # Checks all packages for closest one
            for package in self.packages:
                # Error prevention
                if package is not None:
                    if distances[self.location_id][package.address_id] < closest_package_distance:
                        closest_package_distance = distances[self.location_id][package.address_id]
                        closest_package_id = package.address_id
                        closest_package = package

            # Adds time and checks to see if it has time to deliver package before stop time
            self.time.add_minutes(closest_package_distance / .3)
            if self.time >= self.stop_time:
                return self.total_distance

            # Removes package, changes location, updates total distance and updates package status
            self.packages.remove(closest_package)
            self.location_id = closest_package_id
            self.total_distance += closest_package_distance
            closest_package.delivery_status = 'delivered at ' + str(self.time) + ' by ' + self.name
            last_package = closest_package

        # Checks to see if this is the last route. If it isn't it returns to hub to get more packages
        if not self.last_route:
            self.total_distance += distances[0][last_package.address_id]
        return self.total_distance

    # Sets all package status' to en route
    def load_packages(self):
        for package in self.packages:
            package.delivery_status = 'En route on ' + self.name
