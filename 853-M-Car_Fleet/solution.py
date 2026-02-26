from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = sorted(zip(position, speed), reverse=True)
        groups_counter = 0
        current_group = []
        print(pos_spd)
        
        for pos, spd, in pos_spd:
            time = (target - pos) / spd
            if not current_group:
                current_group.append(time)
                groups_counter += 1
                continue

            if current_group[-1] < time:
                current_group.clear()
                current_group.append(time)
                groups_counter += 1

            print(str(pos), str(spd), str(time), str(groups_counter))

        return groups_counter
    
        
            
