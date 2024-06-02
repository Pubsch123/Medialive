import boto3

# Initialize AWS clients
medialive_client = boto3.client('medialive',region_name='eu-north-1')

# Define the ARN of your MediaLive channel and MediaConnect flow
medialive_channel_id = '5199999'


# Function to check if the MediaLive channel is active
def is_medialive_channel_active():
    try:
        response = medialive_client.describe_channel(ChannelId=medialive_channel_id)
        state = response['State']
        return state == 'RUNNING'
    except Exception as e:
        print("Failed to check MediaLive channel status:", e)
        return False


# Function to start a MediaLive channel
def start_medialive_channel():
    try:
        if is_medialive_channel_active():
            print("MediaLive channel is already running.")
        else:
            response = medialive_client.start_channel(ChannelId=medialive_channel_id)
            print("MediaLive channel started successfully.")
    except Exception as e:
        print("Failed to start MediaLive channel:", e)

# Function to stop a MediaLive channel
def stop_medialive_channel():
    try:
        if not is_medialive_channel_active():
            print("MediaLive channel is already stopped.")
        else:
            response = medialive_client.stop_channel(ChannelId=medialive_channel_id)
            print("MediaLive channel stopped successfully.")
    except Exception as e:
        print("Failed to stop MediaLive channel:", e)


# Main function
def main():
    # Start or stop MediaLive channel.. Check both the functions one by one.
    # start_medialive_channel()
    stop_medialive_channel()

if __name__ == "__main__":
    main()

