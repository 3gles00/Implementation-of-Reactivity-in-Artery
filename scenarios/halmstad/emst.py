import traci
import sys

def detect_emergency_stops(sumo_cmd, deceleration_threshold=-4.5, min_speed=0.5, output_file="emergency_stops.txt"):
    """
    Detects emergency stops in a SUMO simulation.
    
    :param sumo_cmd: Command list to start SUMO with TraCI support.
    :param deceleration_threshold: Minimum deceleration (m/s^2) to consider as an emergency stop.
    :param min_speed: Minimum speed (m/s) to consider for checking deceleration.
    :param output_file: File to log emergency stops.
    """
    traci.start(sumo_cmd)
    last_speeds = {}
    vehicle_stopped = set()

    with open(output_file, 'w') as f:
        while traci.simulation.getMinExpectedNumber() > 0:
            traci.simulationStep()
            vehicles = traci.vehicle.getIDList()
            for veh_id in vehicles:
                current_speed = traci.vehicle.getSpeed(veh_id)
                if veh_id in last_speeds:
                    speed_diff = last_speeds[veh_id] - current_speed
                    # Convert speed difference to deceleration (m/s^2)
                    deceleration = speed_diff / traci.simulation.getDeltaT()
                    if deceleration >= deceleration_threshold and current_speed <= min_speed and veh_id not in vehicle_stopped:
                        f.write(f"Emergency stop detected for vehicle {veh_id} at time {traci.simulation.getTime()}\n")
                        vehicle_stopped.add(veh_id)
                last_speeds[veh_id] = current_speed

    traci.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python this_script.py <Slott.sumo.cfg>")
        sys.exit(1)

    sumo_config = sys.argv[1]
    sumo_cmd = ["sumo-gui", "-c", sumo_config]  # or use 'sumo' for non-GUI mode
    detect_emergency_stops(sumo_cmd)