import typer


class RiskDetector:
    location_depth: list[list[int]] = []
    location_lowest_point: list[list[int]] = []
    total_risk: int = 0

    def __init__(self, input_location: str):
        self.load_input(input_location)
        self.init_lowest_points()
        self.total_risk = 0

    def __str__(self):
        result = "Risk Detector\n"
        result += f" - total risk = {self.total_risk}"
        return result

    def load_input(self, input_location: str):
        with open(input_location, "r") as f:
            lines = f.readlines()

        for line in lines:
            int_array = []
            for element in line.strip():
                int_array.append(int(element))
            self.location_depth.append(int_array)

    def init_lowest_points(self):
        for i in range(len(self.location_depth)):
            new_array = []
            for j in range(len(self.location_depth[i])):
                new_array.append(0)
            self.location_lowest_point.append(new_array)

    def find_lowest_points(self):
        self.total_risk = 0
        max_value: int = 10

        input_rows = len(self.location_depth)
        input_columns = len(self.location_depth[0])
        typer.echo(f"Input is {input_rows} rows and {input_columns} columns")

        for i, row in enumerate(self.location_depth):
            for j, item in enumerate(row):
                if i > 0:
                    top_value = self.location_depth[i - 1][j]
                else:
                    top_value = max_value

                if i < input_rows - 1:
                    bottom_value = self.location_depth[i + 1][j]
                else:
                    bottom_value = max_value

                if j > 0:
                    left_value = self.location_depth[i][j - 1]
                else:
                    left_value = max_value

                if j < input_columns - 1:
                    right_value = self.location_depth[i][j + 1]
                else:
                    right_value = max_value

                if item < top_value and item < bottom_value and item < left_value and item < right_value:
                    self.location_lowest_point[i][j] = 1
                    risk = 1 + item
                    self.total_risk += risk
                    typer.echo(f" - found a lowest point at {i}. {j} with a depth of {item} (risk of {risk})")
