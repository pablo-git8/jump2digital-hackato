import random
import math
import pandas as pd
import time
import os
from supabase import create_client
from datetime import datetime

# Define your points 'a' and 'b'
a = (41.375715, 2.090579) 
b = (41.452426, 2.226904)


# Function to check if a point is within the area
def is_point_within_area(point, a, b):
    lat, lon = point
    return (a[0] <= lat <= b[0]) and (a[1] <= lon <= b[1])


# Function to generate a new point
def generate_new_point(current_position, distance=417):  # distance in meters
    lat_dist = distance / 111000  
    lon_dist = distance / (111000 * math.cos(math.radians(current_position[0])))
    new_lat = current_position[0] + random.uniform(-lat_dist, lat_dist)
    new_lon = current_position[1] + random.uniform(-lon_dist, lon_dist)
    return (new_lat, new_lon) if is_point_within_area((new_lat, new_lon), a, b) else current_position


# Function to simulate movement
def simulate_movement(row):
    new_position = generate_new_point((row['lat'], row['lon']))
    return pd.Series({'lat': new_position[0], 'lon': new_position[1]})


# Initial DataFrame setup (assuming this is done earlier in your script)
def generate_random_point(a, b):

    lat = random.uniform(a[0], b[0])
    lon = random.uniform(a[1], b[1])

    return {'lat': lat, 'lon': lon}


def main():

    # Supabase setup
    supabase_url = os.environ.get('URL_J2D')
    supabase_key = os.environ.get('SUPA_KEY_J2D')

    supabase = create_client(supabase_url, supabase_key)
    
    user_init_pos_df = pd.DataFrame([generate_random_point(a, b) for _ in range(200)])
    user_init_pos_df.reset_index(inplace=True)
    user_init_pos_df.rename(columns={'index': 'id'}, inplace=True)

    # Main loop to update positions every 20 seconds
    try:
        while True:
            # Generate new positions
            user_mov_df = user_init_pos_df.apply(simulate_movement, axis=1).reset_index()
            user_mov_df.columns = ['id', 'lat', 'lon']
            user_mov_pos = user_mov_df.to_dict('records')

            # Update data in the database
            for row in user_mov_pos:
                response = supabase.table("user").upsert(row, on_conflict="id").execute()
                
                trajectory_data = {
                    'user_id': row['id'],
                    'latitude': row['lat'],
                    'longitude': row['lon'],
                    'timestamp': datetime.now().isoformat()
                }

                response = supabase.table("user_trajectory").insert(trajectory_data).execute()

            user_init_pos_df = user_mov_df.copy()

            # Wait for 20 seconds before next iteration
            time.sleep(20)

    except KeyboardInterrupt:
        print("Script stopped by the user.")

if __name__ == '__main__':
    main()
