from typing import List
import os
DAYONE_INPUT = os.path.join(os.path.dirname(__file__), 'day_1_input.txt')
class DayOne():
    def count_depth_increases(self, depths: List[int]) -> int:
        num_of_increasing_depths: int = 0
        for i in range(len(depths)-1):
            if depths[i] < depths[i+1]:
                num_of_increasing_depths += 1
        return num_of_increasing_depths

    def convert_input_file_to_list(self, input_file_path: str) -> List[int]:
        file_data = self.get_file_input(input_file_path=input_file_path)
        return [ int(x) for x in file_data.splitlines() ]
    
    def get_file_input(self, input_file_path: str) -> str:
        with open(input_file_path, 'r') as f:
            file_data = f.read()
        return file_data

def main():
    day_1 = DayOne()
    day_one_input_list = day_1.convert_input_file_to_list(DAYONE_INPUT)
    print(day_1.count_depth_increases(day_one_input_list))

if __name__ == '__main__':
    main()