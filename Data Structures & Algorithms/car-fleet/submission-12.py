class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        iterations_left: list[int] = []
        stack: tuple[int, int] = []
        speed_table: dict[int, int] = {}

        # When a car joins a fleet it can be removed, and the head car will 
        # remain as the fleet identifier

        # When a fleet reaches the destination it is also removed

        # Perhaps use a monotonic decreasing stack?

        # Scratch that, no need to iterate
        # Find out how many iterations left and with a sort you can then see
        # where fleets will form

        for index, pos in enumerate(position):
            speed_table[pos] = speed[index]

        # Sort the list (use the built-in for now)
        position.sort(reverse=True)
        
        # for i in range(len(position) - 1):
        #     for j in range(i + 1, 0, -1):
        #         if position[j] > position[j - 1]:    
        #             temp: tuple[int, int] = position[j], speed[j]
        #             position[j], speed[j] = position[j - 1], speed[j - 1]
        #             position[j - 1], speed[j - 1] = temp

        for index, pos in enumerate(position):
            current_speed: int = speed_table[pos]
            remainder: int = (target - pos) % current_speed
            iterations_needed: int = int((target - pos) / current_speed)
            iterations_left.append(iterations_needed + (1 if remainder else 0))

        for index, current_iterations in enumerate(iterations_left):

            current_position: int = position[index]
            current_speed: int = speed_table[current_position]

            if not stack:
                stack.append((current_iterations, current_position, current_speed))
                continue

            # Check if it catches up
            fleet_leader: tuple[int, int, int] = stack[-1]
            fl_iterations: int
            fl_position: int
            fl_speed: int
            fl_iterations, fl_position, fl_speed = fleet_leader

            if fl_iterations > current_iterations:
                # Joins the fleet leader
                continue
            elif fl_iterations < current_iterations:
                # New leader!
                stack.append((current_iterations, current_position, current_speed))
                continue

            fleet_leader_dist: int = fl_iterations * fl_speed + fl_position
            current_car_dist: int = current_iterations * current_speed + current_position
            
            if fleet_leader_dist == current_car_dist == target:
                # Joins the fleet leader
                continue
            
            # Check the distance before the last iteration and check the distance left
            fl_last_iteration_dist: int = fleet_leader_dist - fl_speed
            current_last_iteration_dist: int = current_car_dist - current_speed

            # When do they reach the finish line in the same iteration?
            fl_time_left: float = (target - fl_last_iteration_dist) / fl_speed
            current_time_left: float = (target - current_last_iteration_dist) / current_speed
            
            if current_time_left <= fl_time_left:
                # They join the fleet leader!
                continue
        
            stack.append((current_iterations, current_position, current_speed))
            
        # print(iterations_left)
        # print(position)
        # print(speed)
        # print(speed_table)
        # print(stack)

        return len(stack)